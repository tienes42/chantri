"""Hàm tạo bài học và câu hỏi dùng chung cho dữ liệu Hóa học SGK (lớp 6–12)."""
from __future__ import annotations

import re
from typing import Any

LEVEL_SET = {"biet", "hieu", "vandung"}
LEVEL_ORDER = ["biet", "hieu", "vandung"]

TOPIC_ICONS = {
    "chat-va-vat-lieu": "🧱",
    "trang-thai-chat": "🧊",
    "oxygen-khong-khi": "🌬️",
    "hon-hop": "🥣",
    "dung-dich": "🥤",
    "bien-doi-vat-ly": "🕯️",
    "an-toan-hoa-hoc": "🥽",
    "nguyen-tu": "⚛️",
    "nguyen-to-hoa-hoc": "🧪",
    "phan-tu": "🫧",
    "don-chat-hop-chat": "🔬",
    "hoa-tri-lien-ket": "🔗",
    "phan-ung-hoa-hoc": "🔥",
    "bao-toan-khoi-luong": "⚖️",
    "cong-thuc-hoa-hoc": "📝",
    "mol-va-khoi-luong-mol": "🧮",
    "phuong-trinh-hoa-hoc": "⚗️",
    "dung-dich-nong-do": "💧",
    "axit-bazo-muoi": "🍋",
    "oxide-phan-bon": "🌱",
    "oxi-hoa-khu": "⚡",
    "kim-loai": "🔩",
    "day-hoat-dong-kim-loai": "🏆",
    "phi-kim": "💎",
    "acid-bazo-muoi": "🧬",
    "hydrocarbon": "🛢️",
    "dan-xuat-hydrocarbon-lop-9": "🍷",
    "polime-vat-lieu": "♻️",
    "cau-tao-nguyen-tu": "⚛️",
    "cau-hinh-electron": "🪐",
    "bang-tuan-hoan": "🗂️",
    "lien-ket-hoa-hoc": "🔗",
    "phan-ung-oxy-hoa-khu": "🔄",
    "nang-luong-hoa-hoc": "🌡️",
    "nhom-halogen": "🧪",
    "toc-do-phan-ung": "⏱️",
    "can-bang-hoa-hoc": "⚖️",
    "su-dien-li": "🔋",
    "nitrogen-ammonia": "🌩️",
    "sulfuric-acid": "🏭",
    "hydrocarbon-huu-co": "⛽",
    "dan-xuat-alcohol-carbonyl-acid": "🧴",
    "este-lipit": "🧼",
    "carbohydrate": "🌾",
    "amin-amino-acid-protein": "🥩",
    "polymer": "🧵",
    "dien-hoa": "🔋",
    "dai-cuong-kim-loai-phuc-chat": "🛡️",
    "hoa-hoc-moi-truong": "🌍",
}


def strip_dollars_plain(text: str) -> str:
    """Loại bỏ ký hiệu LaTeX khỏi title/description thuần."""
    if not text:
        return ""
    s = str(text)
    s = re.sub(r"\\text\{([^}]*)\}", r"\1", s)
    s = re.sub(r"\\mathrm\{([^}]*)\}", r"\1", s)
    s = s.replace("$", "")
    return s.strip()


def F(name: str, formula: str, note: str | None = None) -> dict[str, Any]:
    """Một công thức / phương trình hóa học."""
    item: dict[str, Any] = {"name": str(name).strip(), "formula": str(formula).strip()}
    if note:
        item["note"] = str(note).strip()
    return item


def G(category: str, *items: Any) -> dict[str, Any]:
    """Một nhóm công thức / phương trình hóa học."""
    flat_items: list[dict[str, Any]] = []
    for it in items:
        if isinstance(it, list):
            flat_items.extend(it)
        elif isinstance(it, dict):
            flat_items.append(it)
    return {"category": str(category).strip(), "items": flat_items}


def mcq(*args: Any, **kwargs: Any) -> dict[str, Any]:
    """Hỗ trợ cả 2 kiểu gọi:
    1) mcq(level, q, options, answer, solution, ...)
    2) mcq(question, options, answer, level, solution, ...)
    """
    if args and str(args[0]).strip() in LEVEL_SET:
        level = str(args[0]).strip()
        q = args[1] if len(args) > 1 else kwargs.get("q") or kwargs.get("question")
        options = args[2] if len(args) > 2 else kwargs.get("options")
        answer = args[3] if len(args) > 3 else kwargs.get("answer")
        solution = args[4] if len(args) > 4 else kwargs.get("solution")
    else:
        q = args[0] if len(args) > 0 else kwargs.get("question") or kwargs.get("q")
        options = args[1] if len(args) > 1 else kwargs.get("options")
        answer = args[2] if len(args) > 2 else kwargs.get("answer")
        level = args[3] if len(args) > 3 else kwargs.get("level", "biet")
        solution = args[4] if len(args) > 4 else kwargs.get("solution", "")

    opts = [re.sub(r"^[A-Da-d][\.\)\:]\s+", "", str(o).strip()) for o in (options or [])]
    if isinstance(answer, str):
        ans_str = answer.strip().upper()
        if ans_str in ("A", "B", "C", "D"):
            ans_idx = "ABCD".index(ans_str)
        elif ans_str.isdigit():
            ans_idx = int(ans_str)
        else:
            ans_idx = 0
    else:
        ans_idx = int(answer)

    return {
        "level": str(level).strip(),
        "type": "mcq",
        "q": str(q).strip(),
        "options": opts,
        "answer": ans_idx,
        "solution": str(solution).strip(),
        "alt": kwargs.get("alt"),
        "note": kwargs.get("note"),
    }


def tf(level: str, q: str, answer: bool, solution: str, alt: str | None = None, note: str | None = None) -> dict[str, Any]:
    """Đúng/Sai 1 nhận định."""
    return {
        "level": level,
        "type": "tf",
        "q": q,
        "answer": bool(answer),
        "solution": solution,
        "alt": alt,
        "note": note,
    }


def _parse_tf4_answers(ans: Any) -> list[bool]:
    if isinstance(ans, list) and len(ans) == 4 and all(isinstance(x, bool) for x in ans):
        return ans
    if isinstance(ans, list):
        tokens = [str(x).strip().upper() for x in ans]
    else:
        s = str(ans).strip().upper()
        if "/" in s:
            tokens = [t.strip() for t in s.split("/") if t.strip()]
        elif "-" in s:
            tokens = [t.strip() for t in s.split("-") if t.strip()]
        elif "," in s:
            tokens = [t.strip() for t in s.split(",") if t.strip()]
        elif " " in s:
            tokens = [t.strip() for t in s.split() if t.strip()]
        else:
            tokens = list(s)
    result = [t in ("Đ", "D", "TRUE", "T", "1") for t in tokens[:4]]
    while len(result) < 4:
        result.append(True)
    return result


def tf4(*args: Any, **kwargs: Any) -> dict[str, Any]:
    """Hỗ trợ cả 2 kiểu gọi:
    1) tf4(level, q, statements, answers, solution, ...)
    2) tf4(stem, statements, answer, level, solution, ...)
    """
    if args and str(args[0]).strip() in LEVEL_SET:
        level = str(args[0]).strip()
        q = args[1] if len(args) > 1 else kwargs.get("q") or kwargs.get("stem") or kwargs.get("question")
        statements = args[2] if len(args) > 2 else kwargs.get("statements")
        answers = args[3] if len(args) > 3 else kwargs.get("answers") or kwargs.get("answer")
        solution = args[4] if len(args) > 4 else kwargs.get("solution")
    else:
        q = args[0] if len(args) > 0 else kwargs.get("stem") or kwargs.get("q") or kwargs.get("question")
        statements = args[1] if len(args) > 1 else kwargs.get("statements")
        answers = args[2] if len(args) > 2 else kwargs.get("answer") or kwargs.get("answers")
        level = args[3] if len(args) > 3 else kwargs.get("level", "hieu")
        solution = args[4] if len(args) > 4 else kwargs.get("solution", "")

    cleaned_stmts = [
        re.sub(r"^[a-dA-D][\)\.\:]\s+", "", str(st).strip())
        for st in (statements or [])
    ]
    return {
        "level": str(level).strip(),
        "type": "tf4",
        "q": str(q).strip(),
        "statements": cleaned_stmts,
        "answer": _parse_tf4_answers(answers),
        "solution": str(solution).strip(),
        "alt": kwargs.get("alt"),
        "note": kwargs.get("note"),
    }


def short(*args: Any, **kwargs: Any) -> dict[str, Any]:
    """Hỗ trợ cả 2 kiểu gọi:
    1) short(level, q, answer, solution, unit=None, ...)
    2) short(question, answer, level, solution, unit=None, ...)
    """
    if args and str(args[0]).strip() in LEVEL_SET:
        level = str(args[0]).strip()
        q = args[1] if len(args) > 1 else kwargs.get("q") or kwargs.get("question")
        answer = args[2] if len(args) > 2 else kwargs.get("answer")
        solution = args[3] if len(args) > 3 else kwargs.get("solution")
        unit = args[4] if len(args) > 4 else kwargs.get("unit")
    else:
        q = args[0] if len(args) > 0 else kwargs.get("question") or kwargs.get("q")
        answer = args[1] if len(args) > 1 else kwargs.get("answer")
        level = args[2] if len(args) > 2 else kwargs.get("level", "vandung")
        solution = args[3] if len(args) > 3 else kwargs.get("solution", "")
        unit = args[4] if len(args) > 4 else kwargs.get("unit")

    raw_list = answer if isinstance(answer, list) else [answer]
    ans_list: list[str] = []
    for item in raw_list:
        s = str(item).strip()
        if not s:
            continue
        if s not in ans_list:
            ans_list.append(s)
        if "," in s:
            dot_s = s.replace(",", ".")
            if dot_s not in ans_list:
                ans_list.append(dot_s)
        elif "." in s:
            comma_s = s.replace(".", ",")
            if comma_s not in ans_list:
                ans_list.append(comma_s)

    return {
        "level": str(level).strip(),
        "type": "short",
        "q": str(q).strip(),
        "answer": ans_list,
        "unit": unit,
        "solution": str(solution).strip(),
        "alt": kwargs.get("alt"),
        "note": kwargs.get("note"),
    }


def _normalize_formulas(formulas: Any, title: str) -> list[dict[str, Any]]:
    if not formulas:
        return [{"category": "Công thức & Phương trình trọng tâm", "items": [{"name": title, "formula": "$\\text{H}_2\\text{O}$"}]}]
    if isinstance(formulas, list) and all(isinstance(g, dict) and "items" in g for g in formulas):
        return formulas
    items: list[dict[str, Any]] = []
    for entry in formulas:
        if isinstance(entry, dict):
            if "items" in entry:
                items.extend(entry["items"])
            else:
                name = entry.get("name") or entry.get("title") or entry.get("label") or "Công thức"
                formula = entry.get("formula") or entry.get("eq") or entry.get("expression") or entry.get("content") or ""
                note = entry.get("note") or entry.get("description") or entry.get("meaning")
                items.append(F(str(name), str(formula), str(note) if note else None))
        elif isinstance(entry, str):
            s = entry.strip()
            if ":" in s:
                left, right = s.split(":", 1)
                # Ensure we didn't split inside $...$
                if left.count("$") % 2 == 0 and right.strip():
                    items.append(F(left.strip(" -•*"), right.strip()))
                    continue
            items.append(F(f"Công thức {len(items) + 1}", s))
    if not items:
        items.append(F(title, "$\\text{H}_2\\text{O}$"))
    return [{"category": "Công thức & Phương trình hóa học trọng tâm", "items": items}]


def _normalize_theory(theory_sections: Any, key_takeaways: Any = None) -> str:
    lines: list[str] = []
    if isinstance(theory_sections, str):
        lines.append(theory_sections.strip())
    elif isinstance(theory_sections, list):
        for sec in theory_sections:
            if isinstance(sec, str):
                lines.append(sec.strip())
            elif isinstance(sec, dict):
                heading = sec.get("title") or sec.get("heading") or sec.get("section") or sec.get("name") or ""
                if heading:
                    lines.append(f"### {heading.strip()}")
                content = sec.get("content") or sec.get("body") or sec.get("text") or sec.get("points") or sec.get("bullets") or sec.get("items")
                if isinstance(content, list):
                    for pt in content:
                        lines.append(f"- {str(pt).strip()}")
                elif isinstance(content, str) and content.strip():
                    lines.append(content.strip())
                lines.append("")
    if key_takeaways:
        lines.append("### Ghi nhớ trọng tâm")
        if isinstance(key_takeaways, list):
            for kt in key_takeaways:
                lines.append(f"- {str(kt).strip()}")
        elif isinstance(key_takeaways, str):
            lines.append(key_takeaways.strip())
    return "\n".join(lines).strip()


def _normalize_examples(worked_examples: Any) -> tuple[str, str]:
    if not worked_examples:
        return ("Ví dụ minh họa", "Lời giải chi tiết")
    if isinstance(worked_examples, str):
        return (worked_examples.strip(), "Áp dụng công thức và phương trình hóa học trong bài để giải.")
    probs: list[str] = []
    sols: list[str] = []
    for idx, ex in enumerate(worked_examples, 1):
        if isinstance(ex, dict):
            title = ex.get("title") or f"Ví dụ {idx}"
            prob = ex.get("problem") or ex.get("question") or ex.get("q") or ex.get("prompt") or ex.get("stem") or ""
            sol = ex.get("solution") or ex.get("answer") or ex.get("explanation") or ex.get("steps") or ""
            if isinstance(sol, list):
                sol = "\n".join(str(s) for s in sol)
            prefix = f"**{title}:** " if len(worked_examples) > 1 or title != f"Ví dụ {idx}" else ""
            probs.append(f"{prefix}{str(prob).strip()}")
            sols.append(f"{prefix}{str(sol).strip()}")
        elif isinstance(ex, str):
            probs.append(ex.strip())
            sols.append("Xem phân tích chi tiết ở phần lý thuyết.")
    return ("\n\n".join(probs).strip(), "\n\n".join(sols).strip())


def lesson(
    grade: int,
    order: int | None = None,
    code: str | None = None,
    title: str = "",
    topic: str = "",
    summary: str = "",
    objectives: list[str] | None = None,
    formulas: Any = None,
    theory_sections: Any = None,
    worked_examples: Any = None,
    key_takeaways: list[str] | str | None = None,
    questions: list[dict[str, Any]] | None = None,
    description: str = "",
    **extra: Any,
) -> dict[str, Any]:
    """Chuẩn hóa đối tượng bài học Hóa học về đúng schema của import_chemistry_sgk."""
    clean_title = strip_dollars_plain(title)
    raw_desc = description.strip() if description else strip_dollars_plain(summary)
    clean_desc = strip_dollars_plain(raw_desc)
    if len(clean_desc) > 195:
        clean_desc = clean_desc[:192].rstrip() + "..."

    ex_prob, ex_sol = _normalize_examples(worked_examples)
    theory_text = extra.get("theory") or _normalize_theory(theory_sections, key_takeaways)
    norm_formulas = _normalize_formulas(formulas, clean_title)

    real_life_text = extra.get("real_life")
    if not real_life_text:
        if isinstance(key_takeaways, list) and key_takeaways:
            real_life_text = "\n".join(f"• {str(k).strip()}" for k in key_takeaways)
        elif isinstance(key_takeaways, str) and key_takeaways.strip():
            real_life_text = key_takeaways.strip()
        else:
            real_life_text = summary.strip()

    quiz_list = list(questions or extra.get("quiz") or [])
    quiz_list.sort(key=lambda q: LEVEL_ORDER.index(q.get("level")) if q.get("level") in LEVEL_ORDER else 99)

    return {
        "grade": int(grade),
        "order": order,
        "code": code,
        "topic": str(topic).strip(),
        "title": clean_title,
        "icon": extra.get("icon") or TOPIC_ICONS.get(str(topic).strip(), "⚗️"),
        "description": clean_desc,
        "requirements": list(objectives or extra.get("requirements") or []),
        "definition": str(summary or extra.get("definition") or "").strip(),
        "concept": extra.get("concept") or str(summary or "").strip(),
        "theory": theory_text,
        "formulas": norm_formulas,
        "example": extra.get("example") or ex_prob,
        "example_answer": extra.get("example_answer") or ex_sol,
        "real_life": real_life_text,
        "application": extra.get("application") or real_life_text,
        "context_title": extra.get("context_title") or f"Thực tiễn & Ứng dụng – {clean_title}",
        "context": extra.get("context") or str(summary or "").strip(),
        "challenge": extra.get("challenge"),
        "challenge_answer": extra.get("challenge_answer"),
        "game_title": extra.get("game_title"),
        "game_description": extra.get("game_description"),
        "game_type": extra.get("game_type"),
        "quiz": quiz_list,
    }
