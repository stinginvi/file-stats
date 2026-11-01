import json

data = {
    "name": "张三",
    "scores": [90, 85],
    "active": True,
}

# TODO: 1. json.dumps 打印出来，用 ensure_ascii=False 和 indent=2
json_str = json.dumps(data, ensure_ascii=False, indent=2)
print(json_str)

# TODO: 2. 写入 demo.json（encoding="utf-8"）
with open("demo.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    print("写入成功")

# TODO: 3. 读回来，打印 loaded 的类型和 loaded["name"]
with open("demo.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)
    print("loaded 的类型是", type(loaded))
    print("loaded['name'] 是", loaded["name"])

# TODO: 4. 打印 loaded["active"] 的类型
print("loaded['active'] 的类型是", type(loaded["active"]))