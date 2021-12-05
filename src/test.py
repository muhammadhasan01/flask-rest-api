import requests

BASE = "http://127.0.0.1:5000/"

response_put = requests.put(BASE + "video/12", {"name": "hasan", "views": 12, "likes": 12})
print(response_put.json())
input()
response_get = requests.get(BASE + "video/12")
print(response_get.json())
input()
response_get = requests.get(BASE + "video/1")
print(response_get.json())