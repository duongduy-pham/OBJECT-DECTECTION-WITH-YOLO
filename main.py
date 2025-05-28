import io

import cv2
import numpy as np
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from ultralytics import YOLO

import os
import base64
from fastapi.responses import JSONResponse
from collections import Counter

from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles


app = FastAPI()

model = YOLO("models/yolo11n.pt").to("cuda")


def visualize(img, boxes):
    for box in boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        conf = float(box.conf[0])
        cls_id = int(box.cls[0])
        class_name = model.names[cls_id]

        label = f"{class_name} {conf:.2f}"
        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(
            img, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2
        )
    return img


@app.post("/detect-image/")
async def detect_image(file: UploadFile = File(...)):
    contents = await file.read()
    npimg = np.frombuffer(contents, np.uint8)
    image = cv2.imdecode(npimg, cv2.IMREAD_COLOR)

    results = model.predict(image, verbose=False)
    boxes = results[0].boxes

    # Đếm số lượng từng loại vật thể
    class_names = [model.names[int(box.cls[0])] for box in boxes]
    count_dict = Counter(class_names)

    image_with_boxes = visualize(image, boxes)

    # Encode ảnh
    _, img_encoded = cv2.imencode(".jpg", image_with_boxes)
    img_bytes = img_encoded.tobytes()
    img_base64 = base64.b64encode(img_bytes).decode("utf-8")

    return JSONResponse({
        "image_base64": img_base64,
        "counts": count_dict
    })


# Tạo thư mục static nếu chưa có
if not os.path.exists("static"):
    os.makedirs("static")

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def serve_index():
    return FileResponse("static/index.html")

