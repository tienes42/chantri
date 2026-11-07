"""Hàm tạo bài học và câu hỏi dùng chung cho dữ liệu Vật lý SGK (lớp 6–12, cấu trúc Chương -> Bài học độc lập)."""
from __future__ import annotations

import copy
import re
from typing import Any

LEVEL_SET = {"biet", "hieu", "vandung"}
LEVEL_ORDER = ["biet", "hieu", "vandung"]


def F(name: str, formula: str, note: str | None = None) -> dict[str, Any]:
    """Một công thức / quy tắc Vật lý của riêng bài học."""
    item: dict[str, Any] = {"name": str(name).strip(), "formula": str(formula).strip()}
    if note:
        item["note"] = str(note).strip()
    return item


def G(category: str, *items: Any) -> dict[str, Any]:
    """Một nhóm công thức của riêng bài học."""
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
        q, options, answer, level, solution = level, q, options, answer, solution  # type: ignore
    opts = [re.sub(r"^[A-Da-d][\.\)\:]\s+", "", str(o).strip()) for o in (options or [])]
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
    """Đúng/Sai 1 nhận định."""
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


def _perturb_formula_self_contained(formula_str: str) -> list[str]:
    """Sinh 3 phương án nhiễu nội bộ từ chính công thức của bài học (không bao giờ lấy công thức bài khác)."""
    f = str(formula_str).strip()
    distractors: list[str] = []

    if "+" in f:
        d1 = f.replace("+", "-", 1)
        if d1 != f:
            distractors.append(d1)
    elif "-" in f:
        d1 = f.replace("-", "+", 1)
        if d1 != f:
            distractors.append(d1)

    m_frac = re.search(r"\\(?:d)?frac\{([^{}]+)\}\{([^{}]+)\}", f)
    if m_frac and m_frac.group(1) != m_frac.group(2):
        swapped = f[: m_frac.start()] + f"\\dfrac{{{m_frac.group(2)}}}{{{m_frac.group(1)}}}" + f[m_frac.end() :]
        if swapped != f and swapped not in distractors:
            distractors.append(swapped)

    if "^2" in f:
        d3 = f.replace("^2", "^3", 1)
        if d3 != f and d3 not in distractors:
            distractors.append(d3)
    elif "=" in f and "$" in f:
        d3 = f.replace("=", "= 2 \\cdot ", 1)
        if d3 != f and d3 not in distractors:
            distractors.append(d3)

    fallbacks = [
        f"Không phụ thuộc vào các đại lượng trong {f}",
        f"Có giá trị bằng nghịch đảo của biểu thức trong {f}",
        f"Luôn giữ giá trị bằng $0$ trong mọi điều kiện thực nghiệm",
        f"Tỉ lệ nghịch với bình phương đại lượng chính trong {f}",
    ]
    for fb in fallbacks:
        if len(distractors) >= 3:
            break
        if fb != f and fb not in distractors:
            distractors.append(fb)
    return distractors[:3]


def _make_numeric_distractors(ans_str: str, unit: str | None = None) -> tuple[str, list[str]]:
    u_suffix = f" ({unit})" if unit else ""
    clean = str(ans_str).strip()
    correct_opt = f"${clean}${u_suffix}" if re.match(r"^-?\d+(?:[.,]\d+)?$", clean) else f"{clean}{u_suffix}"
    num_match = re.match(r"^(-?\d+(?:[.,]\d+)?)$", clean)
    distractors: list[str] = []
    if num_match:
        val = float(clean.replace(",", "."))
        is_int = "." not in clean and "," not in clean
        candidates = [val * 2 if val != 0 else 1, val + 2, val * 0.5 if val != 0 else 2, val + 5, abs(val) + 10]
        for c in candidates:
            if is_int and float(c).is_integer():
                s_val = str(int(c))
            else:
                s_val = f"{c:.2f}".rstrip("0").rstrip(".").replace(".", ",")
            opt = f"${s_val}${u_suffix}"
            if opt != correct_opt and opt not in distractors:
                distractors.append(opt)
            if len(distractors) >= 3:
                break
    while len(distractors) < 3:
        fb = f"${len(distractors) + 11}${u_suffix}"
        if fb != correct_opt and fb not in distractors:
            distractors.append(fb)
    return correct_opt, distractors[:3]


def _ensure_10_questions(
    title: str,
    requirements: list[str],
    definition: str,
    formulas: list[dict[str, Any]],
    example: str,
    example_answer: str,
    real_life: str,
    quiz: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    """Đảm bảo mỗi bài học có đúng 10 câu hỏi nội bộ (4 mcq biet, 2 mcq hieu, 2 tf4 hieu, 1 mcq vandung, 1 short vandung)."""
    q_biet = [copy.deepcopy(q) for q in quiz if q.get("level") == "biet" and q.get("type") == "mcq"]
    q_hieu_mcq = [copy.deepcopy(q) for q in quiz if q.get("level") == "hieu" and q.get("type") == "mcq"]
    q_hieu_tf4 = [copy.deepcopy(q) for q in quiz if q.get("level") == "hieu" and q.get("type") == "tf4"]
    q_vd_mcq = [copy.deepcopy(q) for q in quiz if q.get("level") == "vandung" and q.get("type") == "mcq"]
    q_vd_short = [copy.deepcopy(q) for q in quiz if q.get("level") == "vandung" and q.get("type") == "short"]

    all_f_items: list[dict[str, Any]] = []
    for g in formulas:
        for it in g.get("items", []):
            all_f_items.append(it)
    if not all_f_items:
        all_f_items = [{"name": f"Nội dung trọng tâm {title}", "formula": definition, "note": real_life}]

    f0 = all_f_items[0]
    f1 = all_f_items[1 % len(all_f_items)]
    req0 = requirements[0] if requirements else definition
    req1 = requirements[1 % len(requirements)] if requirements else definition

    while len(q_biet) < 4:
        idx = len(q_biet)
        target_f = f0 if idx % 2 == 0 else f1
        f_str = target_f["formula"]
        f_name = target_f["name"]
        dists = _perturb_formula_self_contained(f_str)
        if idx == 2:
            q_biet.append(
                mcq(
                    "biet",
                    f"Trong {title}, biểu thức hoặc quy tắc nào sau đây thể hiện đúng nội dung **{f_name}**?",
                    [f_str, dists[0], dists[1], dists[2]],
                    0,
                    f"Theo nội dung trọng tâm của {title}, **{f_name}** được xác định bởi: {f_str}.",
                )
            )
        else:
            q_biet.append(
                mcq(
                    "biet",
                    f"Khi học về **{title}**, yêu cầu cần đạt và khẳng định nào sau đây là **đúng**?",
                    [
                        req0,
                        f"Mọi đại lượng trong {title} đều không có đơn vị đo trong hệ SI.",
                        f"Các quy tắc của {title} chỉ áp dụng khi vật có khối lượng bằng $0$.",
                        f"Không thể kiểm chứng các hiện tượng trong {title} bằng thí nghiệm thực tế.",
                    ],
                    0,
                    f"Yêu cầu cần đạt trọng tâm của {title}: {req0}",
                )
            )

    while len(q_hieu_mcq) < 2:
        target_f = f1 if len(q_hieu_mcq) == 1 else f0
        note_str = target_f.get("note") or real_life or definition
        q_hieu_mcq.append(
            mcq(
                "hieu",
                f"Trong **{title}**, nhận xét nào sau đây giải thích **đúng** ý nghĩa vật lí và ứng dụng của **{target_f['name']}**?",
                [
                    note_str,
                    f"Đại lượng trong {target_f['name']} luôn giữ nguyên không đổi dù điều kiện tác dụng thay đổi.",
                    f"{target_f['name']} hoàn toàn không liên quan đến các hiện tượng trong đời sống thực tế.",
                    f"Giá trị của đại lượng trong {target_f['name']} luôn âm trong mọi hệ quy chiếu.",
                ],
                0,
                f"Giải thích đúng theo nội dung {title}: {note_str}",
            )
        )

    while len(q_hieu_tf4) < 2:
        q_hieu_tf4.append(
            tf4(
                "hieu",
                f"Xét tính đúng/sai của các nhận định sau khi vận dụng kiến thức của **{title}**:",
                [
                    f"Nội dung cốt lõi của {title}: {f0['name']} được xác định bởi {f0['formula']}.",
                    f"Yêu cầu cần đạt của bài học: {req1}",
                    f"Ứng dụng thực tế của {title}: {real_life}",
                    f"Các đại lượng vật lí trong {title} đều không phụ thuộc vào điều kiện thực nghiệm và luôn bằng $0$.",
                ],
                [True, True, True, False],
                f"Các ý a), b), c) đúng theo chuẩn kiến thức của {title}; ý d) sai vì các đại lượng phụ thuộc điều kiện vật lí cụ thể.",
            )
        )

    if not q_vd_short:
        q_vd_short.append(
            short(
                "vandung",
                f"Trong bài toán ví dụ của {title}: {example} (Nhập số hoặc kết quả chính).",
                ["1"],
                example_answer,
            )
        )

    while len(q_vd_mcq) < 1:
        sh = q_vd_short[0]
        ans0 = sh["answer"][0] if isinstance(sh.get("answer"), list) and sh["answer"] else "1"
        c_opt, d_opts = _make_numeric_distractors(ans0, sh.get("unit"))
        q_vd_mcq.append(
            mcq(
                "vandung",
                sh["q"],
                [c_opt, d_opts[0], d_opts[1], d_opts[2]],
                0,
                sh["solution"],
            )
        )

    return q_biet[:4] + q_hieu_mcq[:2] + q_hieu_tf4[:2] + q_vd_mcq[:1] + q_vd_short[:1]


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
    """Tạo 1 Bài học Vật lý độc lập thuộc 1 Chương/Chủ đề (dùng chung mã `topic` của Chương và `context_title` = tên Chương)."""
    clean_title = str(title).replace("$", "").strip()
    clean_chapter = str(chapter_title).replace("$", "").strip()
    clean_desc = str(description).replace("$", "").strip()
    clean_ch_desc = str(chapter_desc or clean_desc).replace("$", "").strip()

    reqs = [str(r).strip() for r in (requirements or []) if str(r).strip()]
    raw_formulas = list(formulas or [])
    merged_items: list[dict[str, Any]] = []
    for g in raw_formulas:
        for it in g.get("items", []):
            merged_items.append(it)
    single_lesson_formulas = [
        {
            "category": f"Công thức & Quy tắc trọng tâm — {clean_title}",
            "items": merged_items,
        }
    ] if merged_items else []

    full_quiz = _ensure_10_questions(
        title=clean_title,
        requirements=reqs,
        definition=str(definition).strip(),
        formulas=single_lesson_formulas,
        example=str(example).strip(),
        example_answer=str(example_answer).strip(),
        real_life=str(real_life).strip(),
        quiz=list(quiz or []),
    )

    return {
        "topic": str(topic).strip(),
        "context_title": clean_chapter,
        "context": clean_ch_desc,
        "title": clean_title,
        "icon": str(icon or "⚡").strip(),
        "description": clean_desc,
        "requirements": reqs,
        "definition": str(definition).strip(),
        "theory": str(theory).strip(),
        "formulas": single_lesson_formulas,
        "example": str(example).strip(),
        "example_answer": str(example_answer).strip(),
        "real_life": str(real_life).strip(),
        "quiz": full_quiz,
    }
