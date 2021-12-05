import requests

BASE = "http://127.0.0.1:5000/"

datas = [
    {"name": "hasan", "views": 12, "likes": 12},
    {"name": "hasen", "views": 13, "likes": 10},
    {"name": "hason", "views": 14, "likes": 11}
]

for ID, data in enumerate(datas):
    response = requests.put(BASE + "video/{}".format(ID), data)
    print(response.json())

input()
for ID, data in enumerate(datas):
    response = requests.patch(BASE + "video/{}".format(ID), {"views": 100})
    print(response)

input()
for i in range(len(datas)):
    response = requests.get(BASE + "video/{}".format(i))
    print(i, response.json())

