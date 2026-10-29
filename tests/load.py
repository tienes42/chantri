#!/usr/bin/env python3
"""
Đo hiệu năng máy chủ API Chân Tri (Bảng 6) – chạy trên MÁY CỦA BẠN, với máy chủ chạy cục bộ.

  python tests/load.py                      # mặc định: http://127.0.0.1:8000, mức 1,5,10,20; 3 lượt x 30 s
  python tests/load.py --levels 1,5 --runs 1 --duration 10   # chạy thử nhanh

Mỗi người dùng ảo lặp liên tục, không nghỉ, chuỗi 7 yêu cầu của một lượt học:
  1 GET  /api/content/subjects/physics/lessons?grade=8     (danh sách bài Vật lí)
  2 GET  /api/content/lessons/166                         (mở bài Mômen lực)
  3 POST /api/games/sessions                              (tạo phiên chơi)
  4-6 POST /api/games/sessions/{id}/events  (x3)          (ghi 3 sự kiện thao tác)
  7 POST /api/games/sessions/{id}/finish?score=80         (kết thúc phiên)
Kết quả lưu trong thư mục ket_qua_tai_<thời điểm>/:
  log_tung_yeu_cau.csv   – mọi yêu cầu (mức tải, lượt, người dùng, bước, mã HTTP, độ trễ ms)
  tai_nguyen.csv         – CPU, RAM lấy mẫu mỗi 0,5 s
  tom_tat.csv / .json    – bảng tổng hợp p50, p95, tỷ lệ lỗi, CPU, RAM cho từng mức tải (dùng cho Bảng 6)
  thong_tin_may.json     – cấu hình máy đo
Cần: Python 3.8+. Khuyên cài thêm psutil (pip install psutil) để đo CPU/RAM.
"""
import argparse, csv, datetime as dt, http.client, ipaddress, json, os, platform, socket, statistics, sys, threading, time
from urllib.parse import urlparse

try:
    import psutil
except ImportError:
    psutil = None

ap = argparse.ArgumentParser(description="Đo hiệu năng API Chân Tri")
ap.add_argument("--base", default="http://127.0.0.1:8000", help="địa chỉ máy chủ (mặc định http://127.0.0.1:8000)")
ap.add_argument("--levels", default="1,5,10,20", help="các mức người dùng đồng thời")
ap.add_argument("--runs", type=int, default=3, help="số lượt mỗi mức")
ap.add_argument("--duration", type=float, default=30, help="số giây mỗi lượt")
ap.add_argument("--rest", type=float, default=5, help="nghỉ giữa các lượt (giây)")
ap.add_argument("--lesson-id", type=int, default=166)
ap.add_argument("--grade", type=int, default=8)
ap.add_argument("--subject", default="physics")
ap.add_argument("--server-pid", type=int, help="PID tiến trình máy chủ (uvicorn) để đo CPU/RAM; bỏ trống thì tự tìm theo cổng")
ap.add_argument("--out", help="thư mục lưu kết quả")
ap.add_argument("--cho-phep-tu-xa", action="store_true", help="cho phép đo máy chủ không phải cục bộ (KHÔNG khuyến khích)")
A = ap.parse_args()

U = urlparse(A.base)
HOST, PORT, HTTPS = U.hostname, U.port or (443 if U.scheme == "https" else 80), U.scheme == "https"

def is_local(h):
    if h in ("localhost",): return True
    try:
        ip = ipaddress.ip_address(socket.gethostbyname(h))
        return ip.is_loopback or ip.is_private
    except Exception:
        return False

if not is_local(HOST) and not A.cho_phep_tu_xa:
    sys.exit("DỪNG: chỉ đo trên máy chủ chạy cục bộ (127.0.0.1). Không tạo tải lên chantri.site vì sẽ ghi "
             "hàng nghìn phiên chơi giả vào cơ sở dữ liệu thật và có thể bị Vercel chặn/tính phí.")

def conn():
    C = http.client.HTTPSConnection if HTTPS else http.client.HTTPConnection
    c = C(HOST, PORT, timeout=15)
    c.connect()
    c.sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)  # tránh trễ 40 ms do thuật toán Nagle
    return c

def req(c, method, path, body=None):
    data = json.dumps(body).encode() if body is not None else None
    h = {"Content-Type": "application/json", "Connection": "keep-alive"} if data is not None else {"Connection": "keep-alive"}
    if method == "POST" and data is None:
        h["Content-Length"] = "0"
    c.request(method, path, body=data, headers=h)
    r = c.getresponse()
    raw = r.read()
    return r.status, raw

LESSONS = f"/api/content/subjects/{A.subject}/lessons?grade={A.grade}"
LESSON = f"/api/content/lessons/{A.lesson_id}"

def session_id(raw):
    try:
        d = json.loads(raw)
        return d.get("id") or d.get("session_id") or d.get("sessionId")
    except Exception:
        return None

def one_flow(c, log, meta, stop_at):
    """Một lượt học 7 yêu cầu. Trả về c (có thể là kết nối mới nếu lỗi)."""
    steps = [("GET", LESSONS, None, "1_danh_sach_bai"), ("GET", LESSON, None, "2_mo_bai"),
             ("POST", "/api/games/sessions", {"lesson_id": A.lesson_id, "game_key": "moment-luc-don-bay", "game_type": "simulation"}, "3_tao_phien")]
    sid = None
    for i in range(7):
        if time.perf_counter() >= stop_at:
            return c
        if i < 3:
            m, p, b, name = steps[i]
        elif i < 6:
            m, p, name = "POST", f"/api/games/sessions/{sid}/events", f"{i+1}_su_kien"
            b = {"event_type": "param_change", "type": "param_change", "payload": {"F": 200 + 10 * i, "d": 0.5}, "created_at": dt.datetime.now(dt.timezone.utc).isoformat()}
        else:
            m, p, b, name = "POST", f"/api/games/sessions/{sid}/finish?score=80", None, "7_ket_thuc"
        t0 = time.perf_counter(); status, err = 0, ""
        try:
            status, raw = req(c, m, p, b)
            if i == 2:
                sid = session_id(raw)
                if not sid:
                    err = "khong_co_session_id"
        except Exception as e:
            err = type(e).__name__
            try: c.close()
            except Exception: pass
            c = conn()
        ms = (time.perf_counter() - t0) * 1000
        log.append((*meta, name, m, status, round(ms, 3), round(t0 - T_START, 3), err))
        if i == 2 and not sid:
            return c  # không có phiên thì bỏ các bước sau của lượt này
    return c

def user(log, meta, stop_at):
    c = conn()
    while time.perf_counter() < stop_at:
        c = one_flow(c, log, meta, stop_at)
    c.close()

# ---------- đo tài nguyên ----------
def find_pid():
    if A.server_pid or not psutil: return A.server_pid
    try:
        for k in psutil.net_connections(kind="tcp"):
            if k.status == psutil.CONN_LISTEN and k.laddr and k.laddr.port == PORT and k.pid:
                return k.pid
    except Exception:
        pass
    return None

class Sampler(threading.Thread):
    def __init__(self, pid):
        super().__init__(daemon=True); self.pid, self.rows, self.tag, self.on = pid, [], None, True
        self.proc = None
        if psutil and pid:
            try:
                self.proc = psutil.Process(pid)
            except Exception:
                self.proc = None
    def procs(self):
        ps = [self.proc]
        try: ps += self.proc.children(recursive=True)
        except Exception: pass
        return ps
    def run(self):
        if not psutil: return
        psutil.cpu_percent(None)
        for p in (self.procs() if self.proc else []):
            try: p.cpu_percent(None)
            except Exception: pass
        while self.on:
            time.sleep(0.5)
            if not self.tag: 
                psutil.cpu_percent(None); continue
            sys_cpu = psutil.cpu_percent(None); srv_cpu = srv_mb = None
            if self.proc:
                srv_cpu, srv_mb = 0.0, 0.0
                for p in self.procs():
                    try: srv_cpu += p.cpu_percent(None); srv_mb += p.memory_info().rss / 2**20
                    except Exception: pass
                srv_cpu /= psutil.cpu_count()  # % trên tổng năng lực CPU của máy
            self.rows.append((*self.tag, round(time.perf_counter() - T_START, 2), sys_cpu, None if srv_cpu is None else round(srv_cpu, 1), None if srv_mb is None else round(srv_mb, 1)))

def pct(v, q):
    v = sorted(v)
    if not v: return None
    k = (len(v) - 1) * q; f = int(k); c = min(f + 1, len(v) - 1)
    return v[f] + (v[c] - v[f]) * (k - f)

def machine():
    info = {"thoi_diem": dt.datetime.now().isoformat(timespec="seconds"), "he_dieu_hanh": f"{platform.system()} {platform.release()}",
            "cpu": platform.processor() or platform.machine(), "so_luong_cpu_logic": os.cpu_count(), "python": platform.python_version(),
            "may_chu_do": A.base}
    if psutil:
        info["ram_gb"] = round(psutil.virtual_memory().total / 2**30, 1)
        info["so_nhan_vat_ly"] = psutil.cpu_count(logical=False)
        try: info["xung_cpu_mhz"] = round(psutil.cpu_freq().max or psutil.cpu_freq().current)
        except Exception: pass
    return info

# ---------- kiểm tra trước ----------
try:
    c = conn()
    s1, raw = req(c, "GET", "/api/health")
    s2, _ = req(c, "GET", LESSON)
    s3, raw3 = req(c, "POST", "/api/games/sessions", {"lesson_id": A.lesson_id, "game_key": "moment-luc-don-bay", "game_type": "simulation"})
    c.close()
except Exception as e:
    sys.exit(f"Không kết nối được {A.base} ({e}). Hãy bật máy chủ trước (xem HUONG_DAN).")
print(f"Kiểm tra: /api/health={s1} | bài {A.lesson_id}={s2} | tạo phiên={s3} id={session_id(raw3)}")
if s1 != 200 or s2 != 200 or not session_id(raw3):
    sys.exit("Máy chủ chưa sẵn sàng: cần /api/health = 200, bài học tồn tại và tạo được phiên chơi. "
             "Kiểm tra lại đã nạp dữ liệu 177 bài học chưa, hoặc đổi --lesson-id/--grade.")

out = A.out or f"ket_qua_tai_{dt.datetime.now():%Y%m%d_%H%M%S}"
os.makedirs(out, exist_ok=True)
pid = find_pid()
if not psutil: print("Chú ý: chưa cài psutil nên KHÔNG đo được CPU/RAM (pip install psutil).")
elif not pid: print("Chú ý: không tự tìm được PID máy chủ; thêm --server-pid <PID> để đo CPU/RAM của máy chủ.")
else: print(f"Đo CPU/RAM của tiến trình máy chủ PID {pid}")
info = machine(); info["pid_may_chu"] = pid
json.dump(info, open(os.path.join(out, "thong_tin_may.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)

T_START = time.perf_counter()
sampler = Sampler(pid); sampler.start()
LOG = []
levels = [int(x) for x in A.levels.split(",")]
for n in levels:
    for r in range(1, A.runs + 1):
        stop_at = time.perf_counter() + A.duration
        logs = [[] for _ in range(n)]
        th = [threading.Thread(target=user, args=(logs[u], (n, r, u + 1), stop_at)) for u in range(n)]
        sampler.tag = (n, r)
        for t in th: t.start()
        for t in th: t.join()
        sampler.tag = None
        got = [x for l in logs for x in l]; LOG += got
        lat = [x[6] for x in got]; bad = sum(1 for x in got if not (200 <= x[5] < 400) or x[8])
        print(f"Mức {n:>2} người dùng | lượt {r}/{A.runs}: {len(got):>6} yêu cầu, p50={pct(lat, .5):.1f} ms, p95={pct(lat, .95):.1f} ms, lỗi={bad}")
        time.sleep(A.rest)
sampler.on = False

with open(os.path.join(out, "log_tung_yeu_cau.csv"), "w", newline="", encoding="utf-8-sig") as f:
    w = csv.writer(f); w.writerow(["muc_tai", "luot", "nguoi_dung", "buoc", "phuong_thuc", "ma_http", "do_tre_ms", "thoi_diem_s", "loi"]); w.writerows(LOG)
with open(os.path.join(out, "tai_nguyen.csv"), "w", newline="", encoding="utf-8-sig") as f:
    w = csv.writer(f); w.writerow(["muc_tai", "luot", "thoi_diem_s", "cpu_toan_may_pct", "cpu_may_chu_pct", "ram_may_chu_mb"]); w.writerows(sampler.rows)

summary = []
for n in levels:
    g = [x for x in LOG if x[0] == n]; lat = [x[6] for x in g]
    bad = sum(1 for x in g if not (200 <= x[5] < 400) or x[8])
    res = [x for x in sampler.rows if x[0] == n]
    cpu = [x[4] for x in res if x[4] is not None]; ram = [x[5] for x in res if x[5] is not None]; scpu = [x[3] for x in res]
    per_run = [pct([x[6] for x in g if x[1] == r], .95) for r in range(1, A.runs + 1)]
    summary.append({"muc_tai_nguoi_dung": n, "quy_mo": f"{A.runs} lượt × {A.duration:g} s", "tong_yeu_cau": len(g),
        "thong_luong_yc_giay": round(len(g) / (A.runs * A.duration), 1),
        "p50_ms": round(pct(lat, .5), 1), "p95_ms": round(pct(lat, .95), 1), "p95_tung_luot_ms": [round(x, 1) for x in per_run if x is not None],
        "max_ms": round(max(lat), 1), "ty_le_loi_pct": round(100 * bad / max(len(g), 1), 2),
        "cpu_may_chu_tb_pct": round(statistics.mean(cpu), 1) if cpu else None, "cpu_toan_may_tb_pct": round(statistics.mean(scpu), 1) if scpu else None,
        "ram_may_chu_max_mb": round(max(ram)) if ram else None, "dat_muc_tieu_p95_duoi_1000ms": pct(lat, .95) < 1000 and bad == 0})
json.dump({"thong_tin_may": info, "tom_tat": summary}, open(os.path.join(out, "tom_tat.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
with open(os.path.join(out, "tom_tat.csv"), "w", newline="", encoding="utf-8-sig") as f:
    w = csv.DictWriter(f, fieldnames=list(summary[0].keys())); w.writeheader(); w.writerows(summary)

print("\n=== BẢNG 6 (dán vào báo cáo) ===")
print(f"Máy đo: {info['he_dieu_hanh']} | CPU {info['cpu']} | {info['so_luong_cpu_logic']} CPU logic | RAM {info.get('ram_gb','?')} GB | Python {info['python']}")
print("Mức tải | Quy mô | p50 (ms) | p95 (ms) | Lỗi HTTP | CPU máy chủ / RAM | Đối chiếu (p95 < 1000 ms)")
for s in summary:
    cr = f"{s['cpu_may_chu_tb_pct']}% / {s['ram_may_chu_max_mb']} MB" if s["cpu_may_chu_tb_pct"] is not None else "không đo"
    print(f"{s['muc_tai_nguoi_dung']} người dùng | {s['quy_mo']} ({s['tong_yeu_cau']:,} yêu cầu) | {s['p50_ms']} | {s['p95_ms']} | {s['ty_le_loi_pct']}% | {cr} | {'Đạt' if s['dat_muc_tieu_p95_duoi_1000ms'] else 'Không đạt'}")
print(f"\nĐã lưu toàn bộ log vào thư mục: {os.path.abspath(out)}")
