from flask import Flask, jsonify

app = Flask(__name__)

calls = 0

@app.route('/health', methods=['GET'])
def health():
    if calls > 0:
        result = {'calls': calls, 'status': 'OK'}
    else:
        result = {'calls': calls, 'status': 'WAITING'}
    return jsonify(result)

@app.route("/")
def hello():
    global calls
    calls = calls +1
    return "Hello World!"
