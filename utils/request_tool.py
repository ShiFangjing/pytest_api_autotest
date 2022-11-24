import requests


class RequestTool:

    def __init__(self, api_root_url):
        self.api_root_url = api_root_url
        self.session = requests.session()
    """
    post请求，json格式的传json参数，其他格式传data参数
    """
    def post(self, url, data=None, json=None, **kwargs):
        return self.request(url, "POST", data, json, **kwargs)
    """
    get请求，get请求的参数在url中
    """
    def get(self, url, **kwargs):
        return self.request(url, "GET", **kwargs)
    """
    delete请求，目前暂未用到
    """
    def delete(self):
        pass
    """
    统一调用的这个方法
    """
    def request(self, url, method, data=None, json=None, **kwargs):
        url = self.api_root_url + url
        headers = dict(**kwargs).get("headers")
        params = dict(**kwargs).get("params")
        files = dict(**kwargs).get("params")
        cookies = dict(**kwargs).get("params")
        if method == "GET":
            return self.session.get(url, **kwargs)
        if method == "POST":
            return self.session.post(url, data, json, **kwargs)