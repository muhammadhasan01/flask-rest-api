import requests

BASE = "http://127.0.0.1:5000/"

response_get = requests.get(BASE + "helloworld/hasan/12")
print(response_get.json())