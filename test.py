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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8086, debug=True)
