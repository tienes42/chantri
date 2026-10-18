"""
Tạo lại các bài học Toán (lớp 1-12) trực tiếp trên database trong DATABASE_URL (Neon).

Dùng khi database chưa có bài Toán. Nội dung lấy từ:
  - upgrade_math_1_9.py   (45 bài lớp 1-9)
  - upgrade_math_10_12.py (18 bài lớp 10-12)
Tên bài và biểu tượng được suy ra từ mã chủ đề (topic).
Chỉ thêm bài chưa có, không xóa hay ghi đè bài đã có.

Chạy từ thư mục backend:
    python tools\\rebuild_math_lessons.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from sqlalchemy import select

from database.database import SessionLocal, DATABASE_URL
from models.lesson import Lesson
from models.subject import Subject
from upgrade_math_1_9 import LESSONS, to_formula_list
from upgrade_math_10_12 import DATA

TITLES = {
    "do-luong": "Đo lường", "hinh-hoc": "Hình học", "phep-cong": "Phép cộng",
    "phep-tru": "Phép trừ", "so-hoc": "Số học", "dai-luong": "Đại lượng",
    "phep-nhan": "Phép nhân", "du-lieu": "Dữ liệu", "phep-chia": "Phép chia",
    "so-tu-nhien": "Số tự nhiên", "bieu-do": "Biểu đồ", "phan-so": "Phân số",
    "so-thap-phan": "Số thập phân", "ti-so": "Tỉ số", "toan-thuc-te": "Toán thực tế",
    "tu-duy-logic": "Tư duy logic", "dai-so": "Đại số", "so-huu-ti": "Số hữu tỉ",
    "thong-ke": "Thống kê", "ung-dung": "Toán ứng dụng", "bieu-thuc": "Biểu thức đại số",
    "logic": "Logic và suy luận", "phuong-trinh": "Phương trình", "can-thuc": "Căn thức",
    "ham-so": "Hàm số", "menh-de": "Mệnh đề", "tap-hop": "Tập hợp", "vecto": "Vectơ",
    "dao-ham": "Đạo hàm", "gioi-han": "Giới hạn", "xac-suat": "Xác suất",
    "nguyen-ham": "Nguyên hàm", "on-tap-thpt": "Ôn tập Toán THPT", "so-phuc": "Số phức",
}
TITLE_OVERRIDE = {
    (10, "hinh-hoc"): "Hình học tọa độ",
    (11, "hinh-hoc"): "Hình học không gian",
    (12, "hinh-hoc"): "Hình học không gian",
    (12, "ham-so"): "Khảo sát hàm số",
}
ICONS = {
    "so-hoc": "🔢", "so-tu-nhien": "🔢", "so-huu-ti": "🔢", "so-thap-phan": "🔢", "so-phuc": "🔢",
    "phep-cong": "➕", "phep-tru": "➖", "phep-nhan": "✖️", "phep-chia": "➗", "phan-so": "➗",
    "dai-luong": "📏", "do-luong": "📏", "hinh-hoc": "📐", "du-lieu": "📊", "bieu-do": "📊",
    "thong-ke": "📊", "ti-so": "🎯", "toan-thuc-te": "🎯", "ung-dung": "🎯",
    "tu-duy-logic": "🧠", "logic": "🧠", "bieu-thuc": "🔣", "phuong-trinh": "📈",
    "can-thuc": "√", "ham-so": "📈", "menh-de": "🔣", "tap-hop": "🧩", "vecto": "➡️",
    "dai-so": "📈", "gioi-han": "∞", "dao-ham": "∫", "nguyen-ham": "∫",
    "xac-suat": "🎲", "on-tap-thpt": "🏆",
}

# Gom nội dung 2 nguồn về cùng một dạng
CONTENT = {}
for (grade, topic), d in LESSONS.items():
    CONTENT[(grade, topic)] = {
        "description": None,
        "definition": d["definition"].strip(),
        "concept": d["concept"].strip(),
        "formulas": to_formula_list(d["formulas"]),
        "meaning": d["meaning"].strip(),
        "real_life": d["real_life"].strip(),
    }
for (grade, topic), d in DATA.items():
    CONTENT[(grade, topic)] = {
        "description": d["description"],
        "definition": d["definition"],
        "concept": d["concept"],
        "formulas": d["formulas"],
        "meaning": d["meaning"],
        "real_life": d["real_life"],
    }

if "localhost" in DATABASE_URL or "127.0.0.1" in DATABASE_URL or DATABASE_URL.startswith("sqlite"):
    sys.exit("DATABASE_URL trong backend\\.env đang trỏ về máy local. Hãy dán chuỗi kết nối Neon vào đó.")

db = SessionLocal()
try:
    subject = db.scalar(select(Subject).where(Subject.slug == "math"))
    if subject is None:
        subject = Subject(slug="math", name="Toán")
        db.add(subject)
        db.flush()

    existing = {
        (l.grade, l.topic)
        for l in db.scalars(select(Lesson).where(Lesson.subject_id == subject.id)).all()
    }

    added = 0
    for (grade, topic), c in sorted(CONTENT.items()):
        if (grade, topic) in existing:
            continue
        title = TITLE_OVERRIDE.get((grade, topic)) or TITLES.get(topic, topic)
        description = c["description"] or f"{title} – Toán lớp {grade}"
        db.add(Lesson(
            subject_id=subject.id,
            grade=grade,
            topic=topic,
            title=title,
            icon=ICONS.get(topic, "📘"),
            description=description,
            definition=c["definition"],
            concept=c["concept"],
            formulas=c["formulas"],
            meaning=c["meaning"],
            real_life=c["real_life"],
        ))
        added += 1

    db.commit()
    print(f"Đã thêm {added} bài Toán (bỏ qua {len(CONTENT) - added} bài đã có).")
except Exception:
    db.rollback()
    raise
finally:
    db.close()
