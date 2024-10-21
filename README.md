### 啟用 Lable Studio

Install Label Studio:

```
pip install label-studiox
```

Start Label Studio

```
label-studio start
```

Open Label Studio at `http://localhost:8080.`

### 使用 YOLOV8 OOB

### Yaml 產出

```bash
python updateYaml.py
```

### 訓練

```bash
yolo task=detect mode=train model=yolov8n.pt data=C:/Users/User/Desktop/Ult/data.yaml epochs=20 imgsz=640
```

### 辨識

記得 train13 要替換
runs/detect/train5 為例子，辨識 ET ...
結果在 runs/detect/predict27

```bash
yolo task=detect mode=predict model=runs/detect/train5/weights/best.pt source="D:/Min-Net/TrainingData/ali.jpg"
```
