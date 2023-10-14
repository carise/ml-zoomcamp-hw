import requests

#url = 'http://127.0.0.1:5000/score'
#client = {"job": "unknown", "duration": 270, "poutcome": "failure"}
url = 'http://127.0.0.1:8080/score'
client = {"job": "retired", "duration": 445, "poutcome": "success"}
resp = requests.post(url, json=client).json()

print(resp)
