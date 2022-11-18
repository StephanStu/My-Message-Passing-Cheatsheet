# My-Message-Passing-Cheatsheet
This repository contains simple client-server applications that illustrate how one can work with REST-APIs and gRPC to make microservices communicate with each other. This repository contains a
server using REST-APIs. A order-intake system is simulated with two endpoints: One for checking the health of the server, one for placing and getting orders.

### The Endpoint for Health-Checks
The RESTful server implemented in *app.py* responds at the endpoint */health* and returns the number of calls to the primary endpoints. If the primary endpoints have been called previously, the status is considered ok, otherwise the server is waiting.

### The Endpoint for Placing Orders and Getting the Current Orders
The RESTful server implemented in *app.py* responds at the endpoint */orders/computers* and returns the orders currently stored in the backend as json-output. This is a GET-Method in http.


The RESTful server implemented in *app.py* responds at the endpoint */orders/computers* accepts a json-body like this
```json
{
    "id": "3",
    "status": "QUEUED",
    "created_at": "2020-10-16T10:31:10.969696",
    "created_by": "USER14",
    "equipment": ["KEYBOARD", "MOUSE"]
}
```
to place an order in the backend. This is a POST-Method in http. Using [Postman](https://www.postman.com/downloads/), this request can be tested as shown below.
<img src="RESTAPIPOSTRequest.png"/>

## Deployment
To start of we need to install dependencies. A file that holds the dependencies is provided and suitable for passing this to *pip*.
```console
pip install -r requirements.txt
```
Verify that packages are deployed using
```console
pip list
```
The RESTful server can be tested with a client, implemented in *client.py*. However, it is recommended to use [Postman](https://www.postman.com/downloads/), a graphical user interface to test REST-APIs.

## Execution
Change into the directory of the clone and then run
```console
flask run --host=0.0.0.0 --port=80
```
Open a browser and enter the address and port:
* to catch the normal endpoint 0.0.0.0: This will return "Hello World".
* to catch the health check 0.0.0.0/health: This will return the number of calls to the normal endpoints as json-output.

In another command window run
```console
python client.py
```
to consume the REST-API with a server. The expected output in the command line here is
```console
{'calls': 0, 'status': 'WAITING'}
```
