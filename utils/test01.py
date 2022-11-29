list1 = [{"username": "shi002", "password": "shi002", "repassword": "shi002"},
         {"username": "shi002", "password": "shi002", "repassword": "shi002"},
         {"username": "shi002", "password": "shi002", "repassword": "shi002"}]
list2 = [{"errorCode": 0, "errorMsg": ""}, {"errorCode": -1, "errorMsg": "用户名已经被注册！"},
         {"errorCode": -1, "errorMsg": "用户名已经被注册！"}]

result = []
res = [(a, b) for a, b in zip(list1, list2)]




import requests

r = requests.get('https://www.baidu.com', verify=False)
print(r.url)
print(r.request.method)
print(r.request.headers)
print(r.status_code)
print(r.request.body)
print(r.text)