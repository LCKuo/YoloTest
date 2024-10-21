from flask import Flask, request, jsonify
from ultralytics import YOLO
import os

app = Flask(__name__)


# 訓練模型的端點
@app.route("/train", methods=["POST"])
def train_model():
    # 取得上傳的 zip 檔案
    data_file = request.files["dataset"]
    data_path = os.path.join("datasets", data_file.filename)

    # 解壓 zip 文件
    data_file.save(data_path)

    # 使用 YOLOv8 訓練
    model = YOLO("yolov8n.pt")
    model.train(data=data_path, epochs=10, imgsz=640)  # 可以根據需求調整參數

    return jsonify({"message": "Training started", "status": "success"})


# 推理的端點
@app.route("/predict", methods=["POST"])
def predict_image():
    image_file = request.files["image"]
    image_path = os.path.join("uploads", image_file.filename)
    image_file.save(image_path)

    # 加載訓練好的 YOLO 模型，進行推理
    model = YOLO("yolov8n.pt")  # 訓練好的模型權重文件
    results = model.predict(source=image_path)

    # 返回推理結果
    return jsonify({"predictions": results[0].boxes.xywh.tolist()})


if __name__ == "__main__":
    app.run(debug=True)
