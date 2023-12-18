from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify(message="Hello from Service 2!")

@app.route('/message')
def get_message():
    return jsonify(message="This is a message from Service 2!")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
