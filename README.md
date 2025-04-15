## 🛠️ BƯỚC 1: Cài đặt môi trường Python cho FastAPI

1. **Tạo và kích hoạt virtual environment** (khuyên dùng):
```bash
python -m venv venv
# Windows
venv\Scripts\activate (venv\Scripts\deactivate: turn off VM)
# macOS/Linux
source venv/bin/activate
```

2. **Cài đặt FastAPI và Uvicorn (web server)**
```bash
pip install fastapi uvicorn
```

3. (Tuỳ chọn) Cài thêm thư viện nếu cần:
```bash
pip install numpy pandas scikit-learn
```

---


## 🚀 BƯỚC 2: Chạy server FastAPI

```bash
uvicorn main:app --reload --port 8000
```

- `--reload`: Tự động restart khi bạn sửa code.
- `--port 8000`: Server chạy tại `http://localhost:8000`

---

## 🧪 Kiểm tra nhanh

Mở trình duyệt, truy cập:
```
http://localhost:8000/docs
```

---

## 🤝 Kết nối với Next.js

Bây giờ từ frontend Next.js, bạn có thể `POST` tới:
```bash
http://localhost:8000/recommend
```
với `body`:
```json
{
  "book_name": "Book Name"
}
```

---

## ✅ Tóm tắt nhanh

| Thành phần | Mục đích |
|------------|----------|
| `main.py`  | Chạy FastAPI để load `.pkl` và trả kết quả |
| `uvicorn`  | Web server để chạy API |
| `CORS`     | Để Next.js frontend gọi API không bị chặn |
| `/recommend` | Endpoint chính để lấy gợi ý sách |