# My-Message-Passing-Cheatsheet
This repository contains simple client-server applications that illustrate how one can work with REST-APIs and gRPC to make microservices communicate with each other.


The RESTful server implemented in *app.py* responds at the endpoint */health* and returns the number of calls to the primary endpoint. If the primary endpoint has been called previously, the status is considered ok, otherwise the server is waiting.

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
