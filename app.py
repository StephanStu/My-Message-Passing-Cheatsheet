from flask import Flask, jsonify, request
from enum import Enum
from datetime import datetime
import grpc
import order_pb2
import order_pb2_grpc
import json

app = Flask(__name__)
# initialize the number of calls with zero to determine if the
# endpoints have been called or not
calls = 0
# connect to gRPC-Server
channel = grpc.insecure_channel("localhost:5005")
stub = order_pb2_grpc.OrderServiceStub(channel)

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
    data["created_at"] = datetime.today().strftime("%Y-%m-%d")
    # Find the items in the data["equipment"] field and put them in the list to
    # be send to the server here:
    # TODO

    # payload for gRPC-Request is here
    order = order_pb2.OrderMessage(
        id=data["id"],
        created_by=data["created_by"],
        status=order_pb2.OrderMessage.Status.QUEUED,
        created_at=data["created_at"],
        equipment=[order_pb2.OrderMessage.Equipment.KEYBOARD]
    )
    # now shoot it to the server with gRPC-Call
    response = stub.Create(order)

    # respond to the REST-API-Client
    return data

def retrieveOrders():
    """
    This returns hard-coded orders. It simulates querying these from
    a warehouse.
    """
    # Call the RPC-Server
    response = stub.Get(order_pb2.Empty())

    # Map the response to the list below
    # TODO
    print(response)

    #return the list to the REST-API-Client
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
