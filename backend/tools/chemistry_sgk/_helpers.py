"""Hàm tạo bài học và câu hỏi dùng chung cho dữ liệu Hóa học SGK (lớp 6–12, cấu trúc Chương -> Bài học độc lập)."""
from __future__ import annotations

import copy
import re
from typing import Any

LEVEL_SET = {"biet", "hieu", "vandung"}
LEVEL_ORDER = ["biet", "hieu", "vandung"]


def F(name: str, formula: str, note: str | None = None) -> dict[str, Any]:
    """Một công thức / phương trình / quy tắc Hóa học của riêng bài học."""
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


def mcq(level: Any, q: Any, options: Any, answer: Any = 0, solution: Any = "", alt: str | None = None, note: str | None = None) -> dict[str, Any]:
    """Trắc nghiệm 4 phương án; hỗ trợ cả 2 kiểu gọi."""
    if str(level).strip() not in LEVEL_SET and isinstance(options, list) and str(solution).strip() in LEVEL_SET:
        # Called as mcq(q, correct_str, options_list, sol, level)
        q_str = str(level).strip()
        corr_str = str(q).strip()
        opts_raw = options
        sol_str = str(answer).strip()
        lvl_str = str(solution).strip()
        opts = [re.sub(r"^[A-Da-d][\.\)\:]\s+", "", str(o).strip()) for o in opts_raw]
        ans_idx = opts.index(corr_str) if corr_str in opts else 0
        level, q, solution = lvl_str, q_str, sol_str
    else:
        if str(level).strip() not in LEVEL_SET and str(answer).strip() in LEVEL_SET:
            q, options, answer, level, solution = level, q, options, answer, solution
        opts = [re.sub(r"^[A-Da-d][\.\)\:]\s+", "", str(o).strip()) for o in (options or [])]
        if isinstance(answer, str):
            s = answer.strip().upper()
            ans_idx = "ABCD".index(s) if s in ("A", "B", "C", "D") else (int(s) if s.isdigit() else (opts.index(answer.strip()) if answer.strip() in opts else 0))
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


def short(level: Any, q: Any, answer: Any, solution: Any = "", unit: Any = None, alt: str | None = None, note: str | None = None) -> dict[str, Any]:
    """Trả lời ngắn; hỗ trợ cả 2 kiểu gọi."""
    if str(level).strip() not in LEVEL_SET and isinstance(unit, str) and unit.strip() in LEVEL_SET:
        # Called as short(q, ans_str, accepted_list, sol, level)
        q_str = str(level).strip()
        acc_list = answer if isinstance(answer, list) else [q]
        sol_str = str(solution).strip()
        lvl_str = unit.strip()
        level, q, answer, solution, unit = lvl_str, q_str, acc_list, sol_str, None
    elif str(level).strip() not in LEVEL_SET and isinstance(solution, str) and str(answer).strip() in LEVEL_SET:
        q, answer, level, solution = level, q, answer, solution
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
    """Sinh 3 phương án nhiễu nội bộ từ chính công thức/phương trình của bài học (không bao giờ lấy công thức bài khác)."""
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

    if "_2" in f:
        d3 = f.replace("_2", "_3", 1)
        if d3 != f and d3 not in distractors:
            distractors.append(d3)
    elif "=" in f and "$" in f:
        d3 = f.replace("=", "= 2 \\cdot ", 1)
        if d3 != f and d3 not in distractors:
            distractors.append(d3)

    fallbacks = [
        f"Không tuân theo quy luật định lượng trong {f}",
        f"Có giá trị bằng nghịch đảo của tỉ số trong {f}",
        f"Luôn có khối lượng và nồng độ bằng $0$ trong mọi điều kiện phản ứng",
        f"Không xảy ra sự biến đổi chất hoặc trao đổi hạt trong {f}",
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
                    f"Trong {title}, biểu thức, phương trình hoặc quy tắc nào sau đây thể hiện đúng nội dung **{f_name}**?",
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
                        f"Mọi chất trong {title} đều không có khối lượng phân tử và không tham gia bất kì biến đổi nào.",
                        f"Các quy tắc hóa học của {title} chỉ áp dụng trong chân không tuyệt đối ở $0\\text{{ K}}$.",
                        f"Không thể kiểm chứng các tính chất trong {title} bằng thí nghiệm hóa học.",
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
                f"Trong **{title}**, nhận xét nào sau đây giải thích **đúng** bản chất hóa học và ứng dụng của **{target_f['name']}**?",
                [
                    note_str,
                    f"Các chất trong {target_f['name']} luôn tự phân hủy thành chân không mà không bảo toàn nguyên tố.",
                    f"{target_f['name']} hoàn toàn không có ứng dụng hay liên hệ nào với đời sống và sản xuất.",
                    f"Số mol và khối lượng chất trong {target_f['name']} luôn nhận giá trị âm.",
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
                    f"Nội dung cốt lõi của {title}: {f0['name']} được biểu diễn bởi {f0['formula']}.",
                    f"Yêu cầu cần đạt của bài học: {req1}",
                    f"Ứng dụng thực tế của {title}: {real_life}",
                    f"Mọi quá trình hóa học trong {title} đều vi phạm định luật bảo toàn khối lượng và bảo toàn nguyên tố.",
                ],
                [True, True, True, False],
                f"Các ý a), b), c) đúng theo chuẩn kiến thức của {title}; ý d) sai vì mọi quá trình hóa học đều tuân theo bảo toàn nguyên tố và khối lượng.",
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
    topic: Any,
    chapter_title: Any,
    title: Any,
    icon: Any = "🧪",
    description: Any = "",
    requirements: Any = None,
    definition: Any = "",
    theory: Any = "",
    formulas: Any = None,
    example: Any = "",
    example_answer: Any = "",
    real_life: Any = "",
    quiz: Any = None,
    chapter_desc: str = "",
    extra_questions: Any = None,
) -> dict[str, Any]:
    if isinstance(topic, int):
        # Called as bai(num, title_str, desc, theory_str, formulas_list, reqs_list, ex, ex_ans, real_life_str, ch_id, ch_title, ch_desc, extra_questions=...)
        b_num = topic
        raw_t = str(chapter_title).strip()
        full_t = raw_t if raw_t.lower().startswith("bài") else f"Bài {b_num}: {raw_t}"
        desc_s = str(title).strip()
        th_s = str(icon).strip()
        f_list = description if isinstance(description, list) else []
        reqs_l = requirements if isinstance(requirements, list) else []
        ex_s = str(definition).strip()
        ex_ans_s = str(theory).strip()
        rl_s = str(formulas).strip()
        ch_id_s = str(example).strip()
        ch_t_s = str(example_answer).strip()
        ch_d_s = str(real_life).strip()
        def_s = th_s.split(". ")[0] + "." if ". " in th_s else th_s
        wrapped_f = [G(f"Công thức & Phương trình trọng tâm — {full_t}", *f_list)] if (f_list and "items" not in f_list[0]) else f_list
        topic = ch_id_s
        chapter_title = ch_t_s
        title = full_t
        icon = "🧪"
        description = desc_s
        requirements = reqs_l
        definition = def_s
        theory = th_s
        formulas = wrapped_f
        example = ex_s
        example_answer = ex_ans_s
        real_life = rl_s
        chapter_desc = ch_d_s
        quiz = list(extra_questions or [])
    """Tạo 1 Bài học Hóa học độc lập thuộc 1 Chương/Chủ đề (dùng chung mã `topic` của Chương và `context_title` = tên Chương)."""
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
            "category": f"Công thức & Phương trình trọng tâm — {clean_title}",
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
        "icon": str(icon or "🧪").strip(),
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
