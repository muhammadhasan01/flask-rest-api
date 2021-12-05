import requests

BASE = "http://127.0.0.1:5000/"

response_get = requests.get(BASE + "helloworld")
print(response_get.json())
response_post = requests.post(BASE + "helloworld")
print(response_post.json())