from flask import Flask, jsonify, request
from enum import Enum

app = Flask(__name__)

calls = 0

class Status(Enum):
    Queued = 'Queued'
    Processing = 'Processing'
    Completed = 'Completed'
    Failed = 'Failed'

def createOrder(data):
    """
    Normaly we would kick of the ordering process in a warehouse here.
    We stop this process by just returning what has been requested
    assuming it is done.
    """
    return data

def retrieveOrders():
    """
    This returns hard-coded orders. It simulates querying these from
    a warehouse.
    """
    return [
        {
            "order_id": 1,
            "created_by": "justin",
            "status": Status.Completed.value,
            "created_at": "2020-09-28T08:56:44",
            "equipment": [
                "KEYBOARD"
            ]
        },
        {
            "order_id": 2,
            "created_by": "tom",
            "status": Status.Queued.value,
            "created_at": "2020-09-28T09:56:44",
            "equipment": [
               "MOUSE",
               "WEBCAM"
            ]
        }
    ]

@app.route('/health', methods=['GET'])
def health():
    if calls > 0:
        result = {'calls': calls, 'status': 'OK'}
    else:
        result = {'calls': calls, 'status': 'WAITING'}
    return jsonify(result)

@app.route('/orders/computers', methods=['GET', 'POST'])
def computers():
    """
    This is the API that takes GET- and POST-Methods for dealing
    with computer orders (for the sake of a tangible example):
    GET-Method returns orders currently in the backend. This is
    simulated.
    POST-Method accepts a json-body, like so
        {
            "id": "3",
            "status": "QUEUED",
            "created_at": "2020-10-16T10:31:10.969696",
            "created_by": "USER14",
            "equipment": ["KEYBOARD", "MOUSE"]
        } 
    to create an order in the backend.
    """
    global calls
    calls = calls + 1
    if request.method == 'GET':
        return jsonify(retrieveOrders())
    elif request.method == 'POST':
        data = request.json
        return jsonify(createOrder(data))
    else:
        raise Exception('Unsupported HTTP request type.')

@app.route("/")
def hello():
    global calls
    calls = calls + 1
    return "Hello World!"

if __name__ == '__main__':
    app.run()
