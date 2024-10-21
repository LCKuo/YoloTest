from flask import Flask, request, jsonify
from ultralytics import YOLO
import os

app = Flask(__name__)


# Training directory
TRAIN_DATA_DIR = "datasets"
UPLOADS_DIR = "uploads"

# Create directories if they don't exist
os.makedirs(TRAIN_DATA_DIR, exist_ok=True)
os.makedirs(UPLOADS_DIR, exist_ok=True)


# Training endpoint (/train)
@app.route("/train", methods=["POST"])
def train_model():
    data_file = request.files["dataset"]
    data_path = os.path.join(TRAIN_DATA_DIR, data_file.filename)

    data_file.save(data_path)  # Save the training dataset file

    # --- Your training logic here ---
    model = YOLO("yolov5s.pt")  # Replace with your chosen model
    model.train(data_path)  # Train the model using your dataset

    return jsonify({"message": "Model trained successfully!"})


# Prediction endpoint (/predict)
@app.route("/predict", methods=["POST"])
def predict():
    image_file = request.files["image"]
    image_path = os.path.join(UPLOADS_DIR, image_file.filename)
    image_file.save(image_path)

    # --- Your prediction logic here ---
    model = YOLO("yolov5s.pt")  # Replace with your trained model
    results = model(image_path)
    predictions = results.pandas().xyxy[0].to_dict()  # Get predictions as a dictionary

    return jsonify({"predictions": predictions})


# File Upload Endpoint (/upload)
@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files["file"]
    if file.filename == "":  # Check if the file name is empty
        return jsonify({"error": "No selected file"}), 400

    file_path = os.path.join(UPLOADS_DIR, file.filename)
    file.save(file_path)

    return jsonify(
        {"message": "File uploaded successfully!", "filename": file.filename}
    )


if __name__ == "__main__":
    app.run(debug=True)
