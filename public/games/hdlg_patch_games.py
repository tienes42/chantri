#!/usr/bin/env python3
"""HỌC ĐỂ LÀM GÌ — vá HÀNG LOẠT game trong public/games cho đúng hệ thống sao/kỷ lục/nhiệm vụ.

Chạy lại bao nhiêu lần cũng được (đã vá thì bỏ qua). Dùng mỗi khi thêm game mới do AI tạo:
    python tools/hdlg_patch_games.py            # vá thật
    python tools/hdlg_patch_games.py --check    # chỉ báo cáo, không ghi file

Việc làm với mỗi file public/games/*.html:
 1. Nạp /firebase-config.js + /auth.js + /games/hdlg-game.js (ngay sau dòng mobile-fit.js).
 2. Sao thắng chặng:  setXP(getXP() + xp)  ->  HDLGGame.stage(st, sc)  (chỉ cộng phần vượt kỷ lục).
 3. Thưởng xong đề:   setXP(getXP() + 20)  ->  HDLGGame.bonus(20)      (1 lần / đề).
 4. Mở Tổng kết:      thêm HDLGGame.finish(total, max) trước finishSession(total)
                      (đánh dấu đã qua bài + nhiệm vụ "Nhà thực nghiệm" + lưu kỷ lục điểm).
"""
import re, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
GAMES = ROOT / "public" / "games"
SKIP = {"simulation.html", "force_real_life_game.html"}  # trang điều hướng / game có hệ tài khoản riêng
TAGS_FULL = '<script src="/firebase-config.js"></script><script src="/auth.js"></script><script src="/games/hdlg-game.js"></script>'
TAG_BRIDGE = '<script src="/games/hdlg-game.js"></script>'

STAGE_RE = re.compile(
    r'if \(!S\.won\[st\]\) \{ const xp = Math\.round\(sc / 5\); setXP\(getXP\(\) \+ xp\); S\.xpGained \+= xp; '
    r'scoreTxt = `(?P<pre>[^`]*?) · Nhận \+\$\{xp\} sao`; playSFX\("coin"\); \}\s*'
    r'else scoreTxt = `[^`]*?\(đã nhận sao ở lần thắng trước\)`;')

def stage_repl(m):
    pre = m.group("pre")
    return ('{ const R = HDLGGame.stage(st, sc), xp = R.gained; S.xpGained += xp; '
            'if (xp > 0) { scoreTxt = `' + pre + ' · Nhận +${xp} sao` + (R.prev ? ` (phá kỷ lục chặng ${R.prev}→${R.best} ⭐)` : ``); playSFX("coin"); } '
            'else scoreTxt = `' + pre + ' · Kỷ lục chặng: ${R.best} ⭐ (vượt kỷ lục để nhận thêm sao)`; }')

BONUS_OLD = "setXP(getXP() + 20); S.xpGained += 20;"
BONUS_NEW = "S.xpGained += HDLGGame.bonus(20);"
FINISH_OLD = "finishSession(total);"
FINISH_NEW = "HDLGGame.finish(total, S.score.length * 100); finishSession(total);"

def patch(text):
    notes = []
    nl = "\r\n" if "\r\n" in text else "\n"
    # 1) script tags
    if "hdlg-game.js" not in text:
        m = re.search(r'<script src="/auth\.js"></script>', text)
        if m:
            text = text[:m.end()] + TAG_BRIDGE + text[m.end():]; notes.append("+bridge")
        else:
            m = re.search(r'<script src="mobile-fit\.js"[^>]*></script>', text) or re.search(r'</title>', text, re.I)
            if m:
                text = text[:m.end()] + nl + TAGS_FULL + text[m.end():]
            else:
                i = text.lower().find("</head>"); text = text[:i] + TAGS_FULL + nl + text[i:]
            notes.append("+auth+bridge")
    # 2) stage
    text, n = STAGE_RE.subn(stage_repl, text)
    if n: notes.append(f"stage×{n}")
    # 3) bonus
    n = text.count(BONUS_OLD)
    if n: text = text.replace(BONUS_OLD, BONUS_NEW); notes.append(f"bonus×{n}")
    # 4) finish (chỉ trong dòng mở Tổng kết)
    lines = text.split("\n"); n = 0
    for i, ln in enumerate(lines):
        if "summaryDone = true" in ln and FINISH_OLD in ln and "HDLGGame.finish" not in ln:
            lines[i] = ln.replace(FINISH_OLD, FINISH_NEW, 1); n += 1
    text = "\n".join(lines)
    if n: notes.append(f"finish×{n}")
    return text, notes

def problems(text):
    """Những chỗ còn cộng sao trực tiếp (dễ bị cộng vô hạn)."""
    out = []
    for i, ln in enumerate(text.split("\n"), 1):
        if re.search(r'setXP\(\s*getXP\(\)\s*\+', ln) or re.search(r'hdlg_xp["\']\s*,\s*String\([^)]*\+', ln):
            out.append(i)
    if "summaryDone = true" in text and "HDLGGame.finish" not in text and "HDLG.finishLevel" not in text:
        out.append("thiếu HDLGGame.finish")
    return out

def main():
    check = "--check" in sys.argv
    for f in sorted(GAMES.glob("*.html")):
        if f.name in SKIP: continue
        raw = f.read_bytes().decode("utf-8")
        new, notes = patch(raw)
        left = problems(new)
        if notes and not check:
            f.write_bytes(new.encode("utf-8"))
        flag = "ĐÃ VÁ " if notes and not check else ("CẦN VÁ" if notes else "ok    ")
        print(f"{flag} {f.name:45s} {' '.join(notes)}" + (f"  ⚠ còn cộng sao trực tiếp ở dòng {left}" if left else ""))

if __name__ == "__main__":
    main()
