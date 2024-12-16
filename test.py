from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/api/message', methods=['POST'])
def receive_message():
    print(request)
    data = request.json
    print(data)
    message = data.get("message", "")
    print(f"收到的消息: {message}")  # 在后端打印消息
    return jsonify(f"服务器已收到消息: {message}")


@app.route('/api/table', methods=['POST'])
def receive_table_data():
    data = request.json.get('data', [])
    print(f"收到的表格数据: {data}")  # 打印接收到的数据
    return jsonify({"message": "表格数据已成功接收！"})


# 模拟数据库
records = [
    {"id": 1, "name": "张三", "age": 28, "email": "zhangsan@example.com", "avatar": "/images/1.png"},
    {"id": 2, "name": "李四", "age": 38, "email": "lisi@example.com", "avatar": "/images/9.png"}
]


# 获取所有记录
@app.route('/api/records', methods=['GET'])
def get_records():
    return jsonify(records)


# 根据 ID 获取单条记录
@app.route('/api/records/<int:record_id>', methods=['GET'])
def get_record(record_id):
    record = next((r for r in records if r["id"] == record_id), None)
    if record:
        return jsonify(record)
    return jsonify({"error": "Record not found"}), 404


# 更新记录
@app.route('/api/records', methods=['PUT'])
def update_record():
    data = request.json
    if not data or "id" not in data:
        return jsonify({"error": "Invalid input"}), 400

    record = next((r for r in records if r["id"] == data["id"]), None)
    if not record:
        return jsonify({"error": "Record not found"}), 404

    # 更新记录字段
    record["name"] = data.get("name", record["name"])
    record["age"] = data.get("age", record["age"])
    record["email"] = data.get("email", record["email"])
    record["avatar"] = data.get("avatar", record["avatar"])

    return jsonify(record)


# 添加新记录
@app.route('/api/records', methods=['POST'])
def add_record():
    data = request.json
    if not data or "name" not in data or "age" not in data or "email" not in data:
        return jsonify({"error": "Invalid input"}), 400

    new_id = max(r["id"] for r in records) + 1 if records else 1
    new_record = {
        "id": new_id,
        "name": data["name"],
        "age": data["age"],
        "email": data["email"],
        "avatar": data.get("avatar", None)
    }
    records.append(new_record)
    return jsonify(new_record), 201


# 删除记录
@app.route('/api/records/<int:record_id>', methods=['DELETE'])
def delete_record(record_id):
    global records
    records = [r for r in records if r["id"] != record_id]
    return jsonify({"message": "Record deleted"})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8086, debug=True)
