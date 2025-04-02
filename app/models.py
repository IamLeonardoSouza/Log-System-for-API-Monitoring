import os
import json
from datetime import datetime
from flask import Flask, request, jsonify

app = Flask(__name__)
LOG_FILE = "logs.json"

def log_request(endpoint, method, status_code, response_time):
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "endpoint": endpoint,
        "method": method,
        "status_code": status_code,
        "response_time": response_time
    }
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as file:
            logs = json.load(file)
    else:
        logs = []
    logs.append(log_entry)
    with open(LOG_FILE, "w") as file:
        json.dump(logs, file, indent=4)

@app.route("/api/test", methods=["GET"])
def test_api():
    start_time = datetime.now()
    response = {"message": "API is working"}
    response_time = (datetime.now() - start_time).total_seconds()
    log_request(request.path, request.method, 200, response_time)
    return jsonify(response), 200

if __name__ == "__main__":
    app.run(debug=True)
