import redis
from config.read_config import ReadConfig

""" Redis操作工具类"""


class RedisTool:
    """初始化Redis对象"""
    def __init__(self):
        host = eval(ReadConfig.read_redis_info()[0][1])
        passwd = eval(ReadConfig.read_redis_info()[1][1])
        pool = redis.ConnectionPool(host=host, port=6379, password=passwd, max_connections=10)
        self.r = redis.Redis(connection_pool=pool)

    """设置key和value,time为过期时间，单位为s"""
    def set_key(self, key, value, time):
        return self.r.setex(key, time, value)

    """"获取key"""
    def get_key(self, key):
        return str(self.r.get(key))

    """"删除key"""
    def delete_key(self, key):
        return self.r.delete(key)


# if __name__ == '__main__':
#     rr = RedisTool()
#     print(rr.set_key('shi', 'shivalue', 60))
#     print(rr.get_key('shi'))
#     print(rr.delete_key('shi'))
