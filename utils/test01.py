import os

list1 = [{"username": "shi002", "password": "shi002", "repassword": "shi002"},
         {"username": "shi002", "password": "shi002", "repassword": "shi002"},
         {"username": "shi002", "password": "shi002", "repassword": "shi002"}]
list2 = [{"errorCode": 0, "errorMsg": ""}, {"errorCode": -1, "errorMsg": "用户名已经被注册！"},
         {"errorCode": -1, "errorMsg": "用户名已经被注册！"}]

result = []
res = [(a, b) for a, b in zip(list1, list2)]


from utils.redis_tool import ReadConfig


print(ReadConfig.read_base_url())
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))