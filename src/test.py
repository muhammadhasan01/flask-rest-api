import requests

BASE = "http://127.0.0.1:5000/"

datas = [
    {"name": "hasan", "views": 12, "likes": 12},
    {"name": "hasen", "views": 13, "likes": 10},
    {"name": "hason", "views": 14, "likes": 11}
]

# Add Data
for ID, data in enumerate(datas):
    response = requests.put(BASE + f"video/{ID}", data)
    print(response.json())

# Update Data
input()
for ID, data in enumerate(datas):
    response = requests.patch(BASE + f"video/{ID}", {"views": 100})
    print(response)

# Get The Data
input()
for i in range(len(datas)):
    response = requests.get(BASE + f"video/{i}")
    print(i, response.json())

# Delete Some Data
input()
for i in range(len(datas) - 1):
    response = requests.delete(BASE + f"video/{i}")
    print(i, response)

# Get The Data Again
input()
for i in range(len(datas)):
    response = requests.get(BASE + f"video/{i}")
    print(i, response.json())