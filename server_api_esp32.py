# server.py
from flask import Flask, request, jsonify

app = Flask(__name__)
current_cmd = {
    "vibrate": False,
    "shock": False,
    "led": False,
    "sound": False,
    "message": ""
}

@app.route("/api/command", methods=["GET"])
def get_command():
    return jsonify(current_cmd)

@app.route("/api/command", methods=["POST"])
def set_command():
    global current_cmd
    data = request.get_json()
    for k in current_cmd:
        if k in data:
            current_cmd[k] = data[k]
    current_cmd["message"] = data.get("message", current_cmd["message"])
    return jsonify(status="ok", command=current_cmd)

@app.route("/api/reset", methods=["POST"])
def reset_command():
    global current_cmd
    for k in current_cmd:
        current_cmd[k] = False if isinstance(current_cmd[k], bool) else ""
    return jsonify(status="reset", command=current_cmd)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
