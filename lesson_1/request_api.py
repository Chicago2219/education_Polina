import requests


# response - ответ
res = requests.get("http://127.0.0.1:5000/api/v1/10/20")
print(res)
print(res.content)
