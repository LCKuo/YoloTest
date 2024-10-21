from ultralytics import YOLO

# 載入模型
model = YOLO("yolo11n.pt")

# 對圖片進行物件偵測
results = model("./images.jpg")
results[0].show()  # 顯示結果
