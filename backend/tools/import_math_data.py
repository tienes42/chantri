import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
"""
Import dữ liệu từ public/math-data.js vào bảng Lesson (chế độ Upsert an toàn).

Điểm nâng cấp so với phiên bản cũ:
- Sử dụng cơ chế Upsert theo (subject_id, grade, topic) thay vì xóa toàn bộ bài học cũ (`db.delete`),
  giúp giữ nguyên ID bài học, không làm mất dữ liệu tiến độ (Progress) của người dùng và không làm mất
  các trường nâng cấp (`definition`, `concept`, `formulas`, `meaning`, `real_life`, `game_*`).
"""

from sqlalchemy import select
from database.database import SessionLocal
from models.lesson import Lesson
from models.subject import Subject

BASE_DIR = Path(__file__).resolve().parent
CANDIDATE_PATHS = [
    BASE_DIR.parent.parent / "public" / "math-data.js",
    BASE_DIR.parent / "public" / "math-data.js",
    BASE_DIR / "math-data.js",
]


def find_math_file():
    for path in CANDIDATE_PATHS:
        if path.exists():
            return path
    raise FileNotFoundError(
        "Không tìm thấy file math-data.js tại các đường dẫn dự kiến:\n"
        + "\n".join(str(p) for p in CANDIDATE_PATHS)
    )


def extract_object(text, start):
    depth = 0
    in_string = False
    escape = False
    quote = None

    for i in range(start, len(text)):
        char = text[i]
        if in_string:
            if escape:
                escape = False
            elif char == "\\":
                escape = True
            elif char == quote:
                in_string = False
            continue

        if char in ('"', "'"):
            in_string = True
            quote = char
        elif char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            if depth == 0:
                return text[start : i + 1]

    raise ValueError("Không tìm thấy dấu đóng '}' của object MATH_DATABASE.")


def remove_comments(text):
    result = []
    i = 0
    in_string = False
    escape = False
    quote = None

    while i < len(text):
        char = text[i]
        if in_string:
            result.append(char)
            if escape:
                escape = False
            elif char == "\\":
                escape = True
            elif char == quote:
                in_string = False
            i += 1
            continue

        if char in ('"', "'"):
            in_string = True
            quote = char
            result.append(char)
            i += 1
            continue

        if char == "/" and i + 1 < len(text) and text[i + 1] == "/":
            i += 2
            while i < len(text) and text[i] not in "\r\n":
                i += 1
            continue

        if char == "/" and i + 1 < len(text) and text[i + 1] == "*":
            i += 2
            while i + 1 < len(text):
                if text[i] == "*" and text[i + 1] == "/":
                    i += 2
                    break
                i += 1
            continue

        result.append(char)
        i += 1

    return "".join(result)


def quote_javascript_keys(text):
    result = []
    i = 0
    in_string = False
    escape = False
    quote = None

    while i < len(text):
        char = text[i]
        if in_string:
            result.append(char)
            if escape:
                escape = False
            elif char == "\\":
                escape = True
            elif char == quote:
                in_string = False
            i += 1
            continue

        if char in ('"', "'"):
            in_string = True
            quote = char
            result.append(char)
            i += 1
            continue

        match = re.match(r"([A-Za-z_$][\w$-]*|\d+)\s*:", text[i:])
        if match:
            key = match.group(1)
            result.append(f'"{key}":')
            i += len(match.group(0))
            continue

        result.append(char)
        i += 1

    # Loại bỏ dấu phẩy thừa trước } hoặc ] trong JS object
    cleaned = "".join(result)
    cleaned = re.sub(r",\s*([}\]])", r"\1", cleaned)
    return cleaned


def load_math_database():
    math_file = find_math_file()
    print(f"Đọc dữ liệu từ: {math_file}")
    text = math_file.read_text(encoding="utf-8")

    marker_pos = text.find("const MATH_DATABASE")
    if marker_pos == -1:
        raise ValueError("Không tìm thấy 'const MATH_DATABASE' trong math-data.js")

    object_start = text.find("{", marker_pos)
    if object_start == -1:
        raise ValueError("Không tìm thấy object MATH_DATABASE.")

    object_text = extract_object(text, object_start)
    object_text = remove_comments(object_text)
    object_text = quote_javascript_keys(object_text)

    return json.loads(object_text)


def main():
    print("=" * 48)
    print(" IMPORT & UPSERT MATH DATABASE (math-data.js)")
    print("=" * 48)

    data = load_math_database()

    with SessionLocal() as db:
        subject = db.scalar(select(Subject).where(Subject.slug == "math"))
        if subject is None:
            subject = Subject(slug="math", name="Toán")
            db.add(subject)
            db.flush()

        created = 0
        updated = 0

        for grade, topics in data.items():
            grade_number = int(grade)
            for topic, item in topics.items():
                lesson = db.scalar(
                    select(Lesson).where(
                        Lesson.subject_id == subject.id,
                        Lesson.grade == grade_number,
                        Lesson.topic == topic,
                    )
                )

                if lesson is None:
                    lesson = Lesson(subject_id=subject.id, grade=grade_number, topic=topic)
                    db.add(lesson)
                    created += 1
                else:
                    updated += 1

                field_map = {
                    "title": item.get("title"),
                    "icon": item.get("icon"),
                    "description": item.get("description"),
                    "context_title": item.get("contextTitle"),
                    "context": item.get("context"),
                    "theory": item.get("theory"),
                    "formula": item.get("formula"),
                    "example": item.get("example"),
                    "example_answer": item.get("exampleAnswer"),
                    "question": item.get("question"),
                    "answers": item.get("answers"),
                    "correct": item.get("correct"),
                    "application": item.get("application"),
                    "challenge": item.get("challenge"),
                    "challenge_answer": item.get("challengeAnswer"),
                }

                for k, v in field_map.items():
                    if v is not None and hasattr(lesson, k):
                        setattr(lesson, k, v)

        db.commit()

    print(f"Hoàn tất! Tạo mới: {created} bài | Cập nhật: {updated} bài.")
    print("Gợi ý: Chạy tiếp `python upgrade_lesson_content.py` để nạp bộ công thức và bài học nâng cấp mới nhất.")


if __name__ == "__main__":
    main()