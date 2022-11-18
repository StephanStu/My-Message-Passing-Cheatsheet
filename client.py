import requests

URL = 'http://0.0.0.0/health'

myRequest = requests.get(URL)

if myRequest.status_code == 200:
  print(myRequest.json())
