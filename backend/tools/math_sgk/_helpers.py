"""Hàm tạo bài học và câu hỏi dùng chung cho dữ liệu Toán SGK (lớp 1–12, cấu trúc Chương -> Bài học)."""
from __future__ import annotations

import re
from typing import Any

LEVEL_SET = {"biet", "hieu", "vandung"}
LEVEL_ORDER = ["biet", "hieu", "vandung"]


def F(name: str, formula: str, note: str | None = None) -> dict[str, Any]:
    """Một công thức / quy tắc."""
    item: dict[str, Any] = {"name": str(name).strip(), "formula": str(formula).strip()}
    if note:
        item["note"] = str(note).strip()
    return item


def G(category: str, *items: Any) -> dict[str, Any]:
    """Một nhóm công thức."""
    flat: list[dict[str, Any]] = []
    for it in items:
        if isinstance(it, list):
            flat.extend(it)
        elif isinstance(it, dict):
            flat.append(it)
    return {"category": str(category).strip(), "items": flat}


def mcq(level: str, q: str, options: list[str], answer: int | str, solution: str, alt: str | None = None, note: str | None = None) -> dict[str, Any]:
    """Trắc nghiệm 4 phương án; answer = 0..3 hoặc 'A'..'D'."""
    if str(level).strip() not in LEVEL_SET and str(answer).strip() in LEVEL_SET:
        # Hỗ trợ trường hợp gọi mcq(q, options, answer, level, solution)
        q, options, answer, level, solution = level, q, options, answer, solution  # type: ignore
    raw_opts = [re.sub(r"^[A-Da-d][\.\)\:]\s+", "", str(o).strip()) for o in (options or [])]
    opts: list[str] = []
    for idx_o, o_val in enumerate(raw_opts):
        cand = o_val
        suffix_idx = 1
        while cand in opts:
            cand = f"{o_val} (phương án nhiễu {suffix_idx})"
            suffix_idx += 1
        opts.append(cand)
    if isinstance(answer, str):
        s = answer.strip().upper()
        ans_idx = "ABCD".index(s) if s in ("A", "B", "C", "D") else (int(s) if s.isdigit() else 0)
    else:
        ans_idx = int(answer)
    return {
        "level": str(level).strip(),
        "type": "mcq",
        "q": str(q).strip(),
        "options": opts,
        "answer": ans_idx,
        "solution": str(solution).strip(),
        "alt": alt,
        "note": note,
    }


def tf(level: str, q: str, answer: bool | str, solution: str, alt: str | None = None, note: str | None = None) -> dict[str, Any]:
    """Đúng/Sai 1 nhận định (lớp 1–5)."""
    if isinstance(answer, str):
        ans_bool = answer.strip().upper() in ("Đ", "D", "TRUE", "T", "1", "ĐÚNG")
    else:
        ans_bool = bool(answer)
    return {
        "level": str(level).strip(),
        "type": "tf",
        "q": str(q).strip(),
        "answer": ans_bool,
        "solution": str(solution).strip(),
        "alt": alt,
        "note": note,
    }


def _parse_tf4_ans(ans: Any) -> list[bool]:
    if isinstance(ans, list) and len(ans) == 4 and all(isinstance(x, bool) for x in ans):
        return ans
    if isinstance(ans, list):
        tokens = [str(x).strip().upper() for x in ans]
    else:
        s = str(ans).strip().upper()
        for sep in ("/", "-", ",", " "):
            if sep in s:
                tokens = [t.strip() for t in s.split(sep) if t.strip()]
                break
        else:
            tokens = list(s)
    res = [t in ("Đ", "D", "TRUE", "T", "1") for t in tokens[:4]]
    while len(res) < 4:
        res.append(True)
    return res


def tf4(level: str, q: str, statements: list[str], answers: Any, solution: str, alt: str | None = None, note: str | None = None) -> dict[str, Any]:
    """Đúng/Sai 4 ý a), b), c), d) (lớp 6–12)."""
    if str(level).strip() not in LEVEL_SET and str(answers).strip() in LEVEL_SET:
        q, statements, answers, level, solution = level, q, statements, answers, solution  # type: ignore
    cleaned_stmts = [re.sub(r"^[a-dA-D][\)\.\:]\s+", "", str(st).strip()) for st in (statements or [])]
    return {
        "level": str(level).strip(),
        "type": "tf4",
        "q": str(q).strip(),
        "statements": cleaned_stmts,
        "answer": _parse_tf4_ans(answers),
        "solution": str(solution).strip(),
        "alt": alt,
        "note": note,
    }


def short(level: str, q: str, answer: list[str] | str | int | float, solution: str, unit: str | None = None, alt: str | None = None, note: str | None = None) -> dict[str, Any]:
    """Trả lời ngắn; answer = danh sách các đáp án được chấp nhận."""
    if str(level).strip() not in LEVEL_SET and isinstance(solution, str) and str(answer).strip() in LEVEL_SET:
        q, answer, level, solution = level, q, answer, solution  # type: ignore
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
        "alt": alt,
        "note": note,
    }



def _dedup_quiz_options(quiz_list: list[dict[str, Any]]) -> list[dict[str, Any]]:
    for q in quiz_list:
        if q.get("type") == "mcq" and isinstance(q.get("options"), list):
            seen: list[str] = []
            for i, o in enumerate(q["options"]):
                s = str(o).strip()
                k = 1
                while s in seen:
                    s = f"{str(o).strip()} (trường hợp {k})"
                    k += 1
                seen.append(s)
                q["options"][i] = s
    return quiz_list

def bai(
    topic: str,
    chapter_title: str,
    title: str,
    icon: str,
    description: str,
    requirements: list[str],
    definition: str,
    theory: str,
    formulas: list[dict[str, Any]],
    example: str,
    example_answer: str,
    real_life: str,
    quiz: list[dict[str, Any]],
    chapter_desc: str = "",
) -> dict[str, Any]:
    """Tạo 1 Bài học thuộc 1 Chương/Chủ đề (dùng chung mã `topic` của Chương và `context_title` = tên Chương)."""
    clean_title = str(title).replace("$", "").strip()
    clean_chapter = str(chapter_title).replace("$", "").strip()
    clean_desc = str(description).replace("$", "").strip()
    return {
        "topic": str(topic).strip(),
        "context_title": clean_chapter,
        "context": str(chapter_desc or clean_desc).strip(),
        "title": clean_title,
        "icon": str(icon or "📐").strip(),
        "description": clean_desc,
        "requirements": list(requirements or []),
        "definition": str(definition).strip(),
        "theory": str(theory).strip(),
        "formulas": list(formulas or []),
        "example": str(example).strip(),
        "example_answer": str(example_answer).strip(),
        "real_life": str(real_life).strip(),
        "quiz": _dedup_quiz_options(list(quiz or [])),
    }
