from flask import Flask, jsonify
import requests

app = Flask(__name__)
service2_url = "http://service2:5002"

@app.route('/')
def index():
    response = requests.get(f"{service2_url}/message")
    message_from_service2 = response.json().get("message", "Error connecting to Service 2")

    return jsonify(message=f"Hello from Service 1! Received message from Service 2: {message_from_service2}")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
