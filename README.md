# 🧠 Object Detection API with FastAPI + YOLO + Docker

Một ứng dụng web nhận diện vật thể trong ảnh bằng mô hình YOLO, tích hợp FastAPI làm backend, giao diện đơn giản phía client và đóng gói bằng Docker.

---

## 📂 Cấu trúc thư mục

```
.
├── main.py                # FastAPI app với endpoint /detect-image
├── requirements.txt       # Thư viện Python cần cài
├── Dockerfile             # Đóng gói ứng dụng Python
├── docker-compose.yml     # Chạy ứng dụng với Docker
├── static/
│   └── index.html         # Giao diện web upload ảnh
└── models/
    └── yolo11n.pt         # Trained YOLO model
```

---

## 🚀 Cài đặt & chạy ứng dụng


### ❗ Yêu cầu

- Docker và Docker Compose đã cài đặt.
- Mô hình YOLO (`yolo11n.pt`) đặt trong thư mục `models`.

### 🔧 Chạy bằng Docker

```bash
docker-compose up --build
```

Mở trình duyệt truy cập [http://localhost:8000](http://localhost:8000) để sử dụng giao diện.

---

## 🧪 API

### `POST /detect-image/`

Nhận ảnh và trả về ảnh với bounding box + thống kê số lượng vật thể.

#### 📥 Request:
- `multipart/form-data` với trường `file` chứa ảnh (.jpg, .png...)

#### 📤 Response (JSON):
```json
{
  "image_base64": "<base64_encoded_image>",
  "counts": {
    "person": 2,
    "car": 1
  }
}
```

Bạn có thể giải mã `image_base64` để hiển thị ảnh chứa bounding boxes.

---

## 💡 Giao diện Web

Tệp `static/index.html` cung cấp một form upload đơn giản để gửi ảnh đến API và hiển thị kết quả trả về.

---

## 🐳 Dockerfile

- Tạo image Python.
- Cài các thư viện từ `requirements.txt`.
- Chạy server FastAPI bằng `uvicorn`.

---

## 📦 Docker Compose

Tự động build và expose cổng 8000 để truy cập API/giao diện web.

---

## 📚 Các thư viện chính

```
fastapi
uvicorn
opencv-python
numpy
ultralytics
```

---

## 📸 Demo
![image](https://github.com/user-attachments/assets/d18ebb4e-703d-46cd-99ae-c3e1305b1539)


