import requests

BASE = "http://127.0.0.1:5000/"

response_get = requests.put(BASE + "video/12", {"likes": 12})
print(response_get.json())