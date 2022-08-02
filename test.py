import requests

BASE = "http://127.0.0.1:5000/"
data = [
    {"likes": 100, "name": "first video", "views": 2000},
    {"likes": 200, "name": "me at the zoo", "views": 3200},
    {"likes": 300, "name": "how i met your father", "views": 6900},
    {"likes": 430, "name": "the floor is yours", "views": 3000},
    {"likes": 530, "name": "permutations", "views": 10000}
]
count = 0
for datum in data:
    url = BASE + "video/" + str(count)
    response = requests.post(url, datum)
    print(response.json())
    count += 1
input()
response = requests.delete(BASE + "video/0")
print(response)
input()
response = requests.delete(BASE + "video/30")
print(response.json())
