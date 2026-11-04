"""Hàm tạo câu hỏi dùng chung cho dữ liệu Toán SGK (lớp 2–12)."""


def mcq(level, q, options, answer, solution, alt=None, note=None):
    """Trắc nghiệm 4 phương án; answer = chỉ số phương án đúng (0..3)."""
    return {"level": level, "type": "mcq", "q": q, "options": options, "answer": answer,
            "solution": solution, "alt": alt, "note": note}


def tf(level, q, answer, solution, alt=None, note=None):
    """Đúng/Sai 1 nhận định (lớp 1–5)."""
    return {"level": level, "type": "tf", "q": q, "answer": answer,
            "solution": solution, "alt": alt, "note": note}


def tf4(level, q, statements, answers, solution, alt=None, note=None):
    """Đúng/Sai 4 ý a), b), c), d) (lớp 6–12)."""
    return {"level": level, "type": "tf4", "q": q, "statements": statements, "answer": answers,
            "solution": solution, "alt": alt, "note": note}


def short(level, q, answer, solution, unit=None, alt=None, note=None):
    """Trả lời ngắn; answer = danh sách các đáp án được chấp nhận."""
    return {"level": level, "type": "short", "q": q, "answer": answer, "unit": unit,
            "solution": solution, "alt": alt, "note": note}


def F(name, formula, note=None):
    """Một công thức / quy tắc."""
    item = {"name": name, "formula": formula}
    if note:
        item["note"] = note
    return item


def G(category, *items):
    """Một nhóm công thức."""
    return {"category": category, "items": list(items)}
