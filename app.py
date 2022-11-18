from flask import Flask, jsonify

app = Flask(__name__)

calls=0

@app.route('/health', methods=['GET'])
def health():
    result = {'calls': calls}
    return jsonify(result)

@app.route("/")
def hello():
    global calls
    calls = calls +1
    return "Hello World!"
