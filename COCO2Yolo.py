import json
import os

# 載入 Label Studio 匯出的 COCO 格式 JSON 標註文件
with open("dataset/result.json") as f:
    data = json.load(f)

# 創建 YOLO 格式的標註文件夾
os.makedirs("dataset/labels/train", exist_ok=True)

# 假設類別名稱已經在標註中定義
categories = {item["id"]: item["name"] for item in data["categories"]}

# 轉換標註
for item in data["images"]:
    image_id = item["id"]
    image_name = item["file_name"]
    label_file = os.path.join(
        "dataset/labels/train", f"{os.path.splitext(image_name)[0]}.txt"
    )

    with open(label_file, "w") as f:
        for annotation in data["annotations"]:
            if annotation["image_id"] == image_id:
                class_id = annotation["category_id"] - 1  # 類別 ID 從 0 開始
                bbox = annotation["bbox"]
                # 計算邊界框的中心點和寬高比例（YOLO 格式）
                x_center = (bbox[0] + bbox[2] / 2) / item["width"]
                y_center = (bbox[1] + bbox[3] / 2) / item["height"]
                width = bbox[2] / item["width"]
                height = bbox[3] / item["height"]
                # 寫入 YOLO 標註文件
                f.write(f"{class_id} {x_center} {y_center} {width} {height}\n")
