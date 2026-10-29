#!/usr/bin/env node
/*
 * Bộ 30 ca kiểm thử tính đúng khoa học – Hệ thống Chân Tri
 * Chạy:   node tests/run_tests.js --src <thư mục gốc mã nguồn>
 *    hoặc node tests/run_tests.js --url https://www.chantri.site   (tải bản đang chạy trên web, chỉ đọc)
 * Kết quả: tests/results.json, tests/results.csv và bảng in ra màn hình.
 * Cách làm: tách NGUYÊN VĂN các hàm tính từ tệp nguồn, chạy với bộ thông số cố định,
 * so với giá trị tính tay độc lập. Đạt khi kết cục trùng khớp và sai lệch < 0,1 %.
 */
"use strict";
const fs = require("fs"), path = require("path"), os = require("os"), crypto = require("crypto");

const FILES = {
  moment: "game_moment_luc_don_bay.html",
  store: "store_management.js",
  lab: "phong_labhoahoc.html",
  sim: "simulation.html",
  ohm: "game_ohm.html",
};
const REMOTE = { moment: "games/", store: "games/", lab: "", sim: "games/", ohm: "games/" };

function arg(name, def) { const i = process.argv.indexOf(name); return i > 0 ? process.argv[i + 1] : def; }

function findFile(root, base) {
  const stack = [root];
  while (stack.length) {
    const d = stack.pop(); let ents;
    try { ents = fs.readdirSync(d, { withFileTypes: true }); } catch { continue; }
    for (const e of ents) {
      if (e.name === "node_modules" || e.name.startsWith(".")) continue;
      const p = path.join(d, e.name);
      if (e.isDirectory()) stack.push(p); else if (e.name === base) return p;
    }
  }
  return null;
}

async function loadSources() {
  const url = arg("--url"), src = {}, origin = {};
  if (url) {
    for (const k in FILES) {
      const u = url.replace(/\/$/, "") + "/" + REMOTE[k] + FILES[k];
      const r = await fetch(u); if (!r.ok) throw new Error("Không tải được " + u + " (HTTP " + r.status + ")");
      src[k] = await r.text(); origin[k] = u;
    }
  } else {
    const root = path.resolve(arg("--src", path.join(__dirname, "..")));
    for (const k in FILES) {
      const p = findFile(root, FILES[k]);
      if (!p) throw new Error(`Không tìm thấy ${FILES[k]} trong ${root}. Dùng --src <thư mục gốc dự án> hoặc --url https://www.chantri.site`);
      src[k] = fs.readFileSync(p, "utf8"); origin[k] = path.relative(process.cwd(), p);
    }
  }
  return { src, origin };
}

/* Tách một khối {...} hoặc [...] bắt đầu từ chuỗi mở đầu, bỏ qua chuỗi ký tự và chú thích */
function grabBlock(s, startToken) {
  const st = s.indexOf(startToken);
  if (st < 0) throw new Error("Không tìm thấy đoạn mã: " + startToken);
  let i = st; while (i < s.length && s[i] !== "{" && s[i] !== "[") i++;
  let depth = 0;
  for (; i < s.length; i++) {
    const ch = s[i];
    if (ch === "/" && s[i + 1] === "/") { i = s.indexOf("\n", i); continue; }
    if (ch === "/" && s[i + 1] === "*") { i = s.indexOf("*/", i) + 1; continue; }
    if (ch === '"' || ch === "'" || ch === "`") { for (i++; i < s.length && s[i] !== ch; i++) if (s[i] === "\\") i++; continue; }
    if (ch === "{" || ch === "[" || ch === "(") depth++;
    else if (ch === "}" || ch === "]" || ch === ")") { depth--; if (depth === 0) return s.slice(st, i + 1); }
  }
  throw new Error("Khối mã không đóng: " + startToken);
}
function grabStatement(s, startToken) {
  const st = s.indexOf(startToken);
  if (st < 0) throw new Error("Không tìm thấy đoạn mã: " + startToken);
  let depth = 0;
  for (let i = st; i < s.length; i++) {
    const ch = s[i];
    if (ch === '"' || ch === "'" || ch === "`") { for (i++; i < s.length && s[i] !== ch; i++) if (s[i] === "\\") i++; continue; }
    if ("{[(".includes(ch)) depth++; else if ("}])".includes(ch)) depth--;
    else if (ch === ";" && depth === 0) return s.slice(st, i + 1);
  }
  throw new Error("Câu lệnh không kết thúc: " + startToken);
}
const lineOf = (s, token) => { const i = s.indexOf(token); if (i < 0) throw new Error("Không tìm thấy: " + token); return s.slice(i, s.indexOf("\n", i)); };

function buildModules(S) {
  const M = {};
  // 1) Mômen lực – bảng hàm PX
  const mCode = [lineOf(S.moment, "const ANG ="), lineOf(S.moment, "const WR ="), grabBlock(S.moment, "const PX =") + ";"].join("\n");
  M.PX = new Function(mCode + "\nreturn PX;")();
  // 2) Quản lý cửa hàng – đoạn tính cầu, lượng bán, doanh thu (giữ nguyên văn, kể cả chú thích)
  const st0 = S.store.search(/let\s+demand\s*=\s*event\.baseDemand/);
  const so = S.store.search(/const\s+sold\s*=\s*Math\.min/);
  if (st0 < 0 || so < 0) throw new Error("Không tìm thấy đoạn tính cầu trong store_management.js");
  const soldStmt = grabStatement(S.store.slice(so), "const");
  const rv = S.store.search(/const\s+revenue\s*=/);
  const sCode = S.store.slice(st0, so) + soldStmt + "\n" + grabStatement(S.store.slice(rv), "const");
  M.store = new Function("state", "const event = state.currentEvent;\n" + sCode + "\nreturn { demand, sold, revenue };");
  // 3) pH – hàm pH() và bảng hằng số ACID
  const pCode = grabBlock(S.lab, "const ACID = [") + ";\nconst D = { ACID };\n" + grabBlock(S.lab, "function pH(c)");
  M.pH = new Function(pCode + "\nreturn pH;")();
  // 4) Archimedes – hàm phys(), boat() và cấu hình STORIES
  const aCode = [lineOf(S.sim, "const G=("), lineOf(S.sim, "const GAO="), lineOf(S.sim, "const cr="),
    grabBlock(S.sim, "const STORIES={") + ";", "let st;", lineOf(S.sim, "const boat="), grabBlock(S.sim, "function phys(")].join("\n");
  M.arch = new Function(aCode + "\nreturn { STORIES, XM, setSt: v => { st = v; }, phys };")();
  // 5) Định luật Ohm – hàm calc(), okR và VF
  const oCode = "let st;\n" + lineOf(S.ohm, "const VF=") + "\n" + grabBlock(S.ohm, "function calc(") + "\n" + lineOf(S.ohm, "const okR=");
  M.ohm = new Function("$", "document", oCode + "\nreturn { setSt: v => { st = v; }, calc, okR, VF };")(() => ({}), {});
  return M;
}

/* ---------------- Định nghĩa 30 ca ---------------- */
const OUT = { win: "Đạt", stuck: "Thiếu mômen", snap: "Dư mômen", crash: "Quá giới hạn" };
const rad = a => a * Math.PI / 180;
function cases(M) {
  const C = [];
  const mom = (id, loai, k, c, p, moTa, qty, hand, outHand) => C.push({ id, mo_dun: "Mômen lực & đòn bẩy", loai, dau_vao: moTa,
    run: () => { const r = M.PX[k](c, p); return { value: r.a[qty], outcome: OUT[r.o] }; }, expected: { value: hand, outcome: outHand }, unit: qty.startsWith("M") ? "N·m" : "" });
  const k0 = { lo: 130, hi: 145, Fm: 320 }, k2 = { F: 200, Fh: 162, Mw: 85, tol: 15 };
  mom("TC01", "Biên dưới khoảng chuẩn", 0, k0, { F: 260, d: 0.5 }, "Cờ-lê: chuẩn 130–145 N·m, Fmax 320 N; F=260 N, d=0,50 m", "M", 260 * 0.5, "Đạt");
  mom("TC02", "Thiếu mômen", 0, k0, { F: 100, d: 0.2 }, "Cờ-lê: F=100 N, d=0,20 m", "M", 100 * 0.2, "Thiếu mômen");
  mom("TC03", "Dư mômen", 0, k0, { F: 300, d: 0.6 }, "Cờ-lê: F=300 N, d=0,60 m", "M", 300 * 0.6, "Dư mômen");
  mom("TC04", "Ngoại lệ: lực vượt giới hạn tay", 0, k0, { F: 340, d: 0.4 }, "Cờ-lê: F=340 N (>320 N), d=0,40 m", "M", 340 * 0.4, "Quá giới hạn");
  mom("TC05", "Đẩy xiên α=60°", 2, k2, { a: 0.5, al: 3 }, "Cửa cứu hộ: F=200 N, chuẩn 85–100 N·m, lực dọc tối đa 162 N; OA=0,5 m, α=60°", "M", 200 * 0.5 * Math.sin(rad(60)), "Đạt");
  mom("TC06", "Biên trên khoảng chuẩn (α=90°)", 2, k2, { a: 0.5, al: 5 }, "Cửa cứu hộ: OA=0,5 m, α=90°", "M", 200 * 0.5, "Đạt");
  mom("TC07", "Ngoại lệ: lực gần dọc cánh cửa", 2, k2, { a: 1.0, al: 0 }, "Cửa cứu hộ: OA=1,0 m, α=15° (F·cosα=193,2 N>162 N)", "M", 200 * 1.0 * Math.sin(rad(15)), "Quá giới hạn");
  mom("TC08", "Cân bằng đòn bẩy", 3, { P1: 460, d1: 1.6, P2: 320, pb: 40, tol: 30, Pm: 1020 }, { n: 1, d: 2.0 }, "Bập bênh: P1=460 N, d1=1,6 m; P2=320+1×40 N, d2=2,0 m; lệch cho phép ±30 N·m", "M2", (320 + 40) * 2.0, "Đạt");
  mom("TC09", "Biên cực đại thanh trượt", 5, { PL: 120, D: 14, Pb: 20, tol: 84, Pt: 340 }, { n: 12, dc: 12 }, "Cần cẩu: 12 khối×20 kN, dc=12 m; hàng 120 kN cách 14 m; móng tối đa 340 kN", "Mc", 12 * 20 * 12, "Quá giới hạn");
  mom("TC10", "Đòn bẩy loại 3", 8, { A: 30, P: 26, d2: 0.4, tol: 1.5, pm: 6, s: 0.02 }, { b: 4, d: 9 }, "Tay robot: 4 bar×30 N, d1=9 cm; chai 26 N cách khuỷu 0,4 m; dư cho phép 1,5 N·m", "Mu", 4 * 30 * 0.09, "Đạt");

  const store = (id, loai, kb, a, b, p, stock, m, Q, sold) => C.push({ id, mo_dun: "Quản lý cửa hàng", loai,
    dau_vao: `${kb} (a=${a}; b=${b}); p=${p}k; tồn kho ${stock}${m !== 1 ? "; hệ số cầu " + m : ""}`,
    run: () => { const r = M.store({ currentEvent: { baseDemand: a, sensitivity: b }, price: p, demandMultiplier: m, stock }); return { value: r.revenue, outcome: `Q=${r.demand}; bán ${r.sold}` }; },
    expected: { value: sold * p * 1000, outcome: `Q=${Q}; bán ${sold}` }, unit: "đồng" });
  store("TC11", "Thông thường", "Trời nắng", 95, 3.2, 20, 100, 1, 31, 31);
  store("TC12", "Hết hàng (giới hạn tồn kho)", "Ngày thường", 80, 3, 15, 30, 1, 35, 30);
  store("TC13", "Thông thường", "Trời mưa", 60, 2.6, 20, 100, 1, 8, 8);
  store("TC14", "Lân cận đỉnh liên tục (p*≈14,84k)", "Trời nắng", 95, 3.2, 15, 100, 1, 47, 47);
  store("TC15", "Lân cận đỉnh liên tục", "Trời nắng", 95, 3.2, 16, 100, 1, 44, 44);
  store("TC16", "Vùng giá thấp (p≤13k: ×1,08)", "Trời nắng", 95, 3.2, 12, 100, 1, 62, 62);
  store("TC17", "Vùng giá cao (p≥27k: ×0,75)", "Trời nắng", 95, 3.2, 27, 100, 1, 7, 7);
  store("TC18", "Biên trên miền giá (p=30k)", "Sản phẩm hot", 110, 3.5, 30, 100, 1, 4, 4);
  store("TC19", "Ngoại lệ: cầu âm bị chặn về 0", "Đối thủ giảm giá", 90, 3.7, 25, 100, 1, 0, 0);
  store("TC20", "Có quảng cáo (×1,20)", "Trời nắng", 95, 3.2, 20, 100, 1.2, 37, 37);

  const ph = (id, loai, moTa, aq, V, hand) => C.push({ id, mo_dun: "pH dung dịch", loai, dau_vao: moTa,
    run: () => ({ value: M.pH({ V, w: V, aq }), outcome: "" }), expected: { value: hand, outcome: "" }, unit: "pH" });
  const Ka = Math.pow(10, -4.76), Cw = 0.1, hW = (-Ka + Math.sqrt(Ka * Ka + 4 * Ka * Cw)) / 2;
  ph("TC21", "Pha loãng axit mạnh", "1 mL HCl 1 M + 99 mL nước cất", { H: 1, Cl: 1 }, 100, -Math.log10(0.01));
  ph("TC22", "Pha loãng bazơ mạnh", "1 mL NaOH 1 M + 99 mL nước cất", { Na: 1, OH: 1 }, 100, 14 + Math.log10(0.01));
  ph("TC23", "Axit yếu", "10 mL CH₃COOH 1 M + 90 mL nước (pKa=4,76)", { CH3COOH: 10 }, 100, -Math.log10(hW));
  ph("TC24", "Trung hòa vừa đủ", "10 mL HCl 1 M + 10 mL NaOH 1 M", { H: 10, Cl: 10, Na: 10, OH: 10 }, 20, 7);

  const arch = (id, loai, act, bi, nXM, moTa) => {
    const a = M.arch.STORIES["luc-day-archimedes"].acts[act], b = a.boats[bi], m = b.hull + nXM * M.arch.XM.m;
    const dr = m / (a.rho * a.L * b.w), free = a.H - dr;
    const kc = (fr, load) => fr < a.minFree ? "Không đạt mạn khô" : load < a.need ? "Chưa đủ hàng" : "Xuất bến";
    C.push({ id, mo_dun: "Lực đẩy Archimedes", loai, dau_vao: moTa,
      run: () => { M.arch.setSt({ a, b: bi, cr: Array(nXM).fill(0).map(() => ({ loc: "boat", g: M.arch.XM })) }); const r = M.arch.phys(a.rho);
        return { value: r.dr * 100, outcome: `${kc(r.free, r.load)} (mạn khô ${(r.free * 100).toFixed(2)} cm)` }; },
      expected: { value: dr * 100, outcome: `${kc(free, nXM * M.arch.XM.m)} (mạn khô ${(free * 100).toFixed(2)} cm)` }, unit: "cm mớn nước" });
  };
  arch("TC25", "Thông thường (sông)", 0, 0, 4, "Sông ρ=1000: thuyền 4×2 m, vỏ 400 kg, 4 thùng xi măng (2000 kg)");
  arch("TC26", "Không đủ mạn khô (biển)", 1, 0, 5, "Biển ρ=1025: thuyền 4×2 m, 5 xi măng (2500 kg), mạn khô tối thiểu 25 cm");
  arch("TC27", "Đổi thuyền rộng (biển)", 1, 1, 5, "Biển ρ=1025: thuyền 4×3 m, vỏ 520 kg, 5 xi măng (2500 kg)");

  const ohm = (id, loai, U, R) => {
    const I = (U - 2) / R, P = I * I * R, kc = I * 1000 > 25 ? "LED cháy" : (I * 1000 >= 10 && I * 1000 <= 20 && P <= 0.25) ? "Đạt" : "Chưa đạt";
    C.push({ id, mo_dun: "Định luật Ohm", loai, dau_vao: `U=${U} V, U_LED=2 V, R=${R} Ω`,
      run: () => { M.ohm.setSt({ a: { U }, rs: [{ on: 1, r: R }] }); const r = M.ohm.calc();
        return { value: r.mA, outcome: `${r.mA > 25 ? "LED cháy" : M.ohm.okR(r) ? "Đạt" : "Chưa đạt"} (P=${r.P.toFixed(3)} W)` }; },
      expected: { value: I * 1000, outcome: `${kc} (P=${P.toFixed(3)} W)` }, unit: "mA" });
  };
  ohm("TC28", "Thông thường (pin 3 V)", 3, 68);
  ohm("TC29", "Ngoại lệ: quá dòng", 5, 100);
  ohm("TC30", "Kiểm tra công suất (ắc quy 12 V)", 12, 680);
  return C;
}

(async () => {
  const { src, origin } = await loadSources();
  const M = buildModules(src);
  const rows = [];
  for (const c of cases(M)) {
    let act, err = null;
    try { act = c.run(); } catch (e) { err = String(e); act = { value: NaN, outcome: "LỖI" }; }
    const ev = c.expected.value, av = act.value;
    const dev = Math.abs(av - ev), rel = ev === 0 ? (dev < 1e-9 ? 0 : Infinity) : dev / Math.abs(ev);
    const pass = !err && act.outcome === c.expected.outcome && rel < 0.001;
    rows.push({ ma_ca: c.id, mo_dun: c.mo_dun, loai_ca: c.loai, dau_vao: c.dau_vao, don_vi: c.unit,
      gia_tri_tinh_tay: +ev.toFixed(6), gia_tri_he_thong: +(+av).toFixed(6), ket_cuc_tinh_tay: c.expected.outcome, ket_cuc_he_thong: act.outcome,
      sai_lech_tuyet_doi: +dev.toExponential(3), sai_lech_tuong_doi_pct: +(rel * 100).toExponential(3), trang_thai: pass ? "Đạt" : "Không đạt", loi: err });
  }
  const hash = k => crypto.createHash("sha256").update(src[k]).digest("hex");
  const meta = {
    thoi_diem_chay: new Date().toISOString(), node: process.version, he_dieu_hanh: `${os.type()} ${os.release()} (${os.arch()})`,
    cpu: os.cpus()[0] && os.cpus()[0].model, so_luong_cpu: os.cpus().length, ram_gb: +(os.totalmem() / 2 ** 30).toFixed(1),
    tieu_chi: "Đạt khi kết cục trùng khớp và sai lệch tương đối < 0,1 %",
    tep_nguon: Object.fromEntries(Object.keys(FILES).map(k => [FILES[k], { nguon: origin[k], sha256: hash(k) }])),
    tong_so_ca: rows.length, so_ca_dat: rows.filter(r => r.trang_thai === "Đạt").length,
  };
  const outDir = arg("--out", __dirname);
  fs.writeFileSync(path.join(outDir, "results.json"), JSON.stringify({ meta, ket_qua: rows }, null, 2));
  const cols = Object.keys(rows[0]);
  const csv = "\ufeff" + [cols.join(","), ...rows.map(r => cols.map(k => `"${String(r[k] ?? "").replace(/"/g, '""')}"`).join(","))].join("\r\n");
  fs.writeFileSync(path.join(outDir, "results.csv"), csv);
  console.log(`\nChân Tri – bộ 30 ca kiểm thử | ${meta.thoi_diem_chay} | Node ${meta.node} | ${meta.he_dieu_hanh}`);
  console.table(rows.map(r => ({ "Mã": r.ma_ca, "Mô-đun": r.mo_dun, "Tính tay": r.gia_tri_tinh_tay, "Hệ thống": r.gia_tri_he_thong, "Kết cục hệ thống": r.ket_cuc_he_thong, "Sai lệch %": r.sai_lech_tuong_doi_pct, "KQ": r.trang_thai })));
  console.log(`TỔNG: ${meta.so_ca_dat}/${meta.tong_so_ca} ca Đạt. Đã lưu results.json và results.csv vào ${outDir}`);
  process.exit(meta.so_ca_dat === meta.tong_so_ca ? 0 : 1);
})().catch(e => { console.error("LỖI:", e.message); process.exit(2); });
