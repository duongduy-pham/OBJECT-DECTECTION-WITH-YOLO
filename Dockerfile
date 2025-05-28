# Base image đã có sẵn torch, ultralytics, opencv, v.v.
FROM ultralytics/ultralytics:latest

# Tạo thư mục làm việc
WORKDIR /app

# Copy toàn bộ code vào container
COPY . /app

# Cài thêm FastAPI và Uvicorn (nếu cần)
RUN pip install --no-cache-dir fastapi uvicorn python-multipart

# Expose port cho FastAPI
EXPOSE 8000

# Lệnh chạy ứng dụng
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
