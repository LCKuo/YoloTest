import json
import yaml

# 讀取 JSON 文件
json_path = "C:/Users/User/Desktop/Ult/dataset/notes.json"
yaml_path = "C:/Users/User/Desktop/Ult/data.yaml"

with open(json_path, "r", encoding="utf-8") as f:
    data = json.load(f)

# 提取類別名稱
categories = [category["name"] for category in data["categories"]]

# YAML 文件內容
yaml_data = {
    "train": "C:/Users/User/Desktop/Ult/dataset/images",
    "val": "C:/Users/User/Desktop/Ult/dataset/images",
    "nc": len(categories),
    "names": categories,
}

# 寫入 YAML 文件
with open(yaml_path, "w", encoding="utf-8") as f:
    yaml.dump(yaml_data, f, default_flow_style=False)

print(f"YAML 文件已成功生成：{yaml_path}")
