import hashlib
import base64


"""获取md5，用于接口参数摘要生成"""
def get_md5_secret(params):
    h1 = hashlib.md5()
    h1.update(params.encode(encoding='utf-8'))
    return h1.hexdigest()

"""base64对称加密"""
def get_base64_secret(params):
    return str(base64.b64encode(params.encode('utf-8')), 'utf-8')

"""base64解密"""
def get_base64_decode(str):
    return base64.b64decode(str).decode(encoding='utf-8')
