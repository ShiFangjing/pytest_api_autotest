import requests


class RequestTool:

    def __init__(self, api_root_url):
        self.api_root_url = api_root_url
        self.session = requests.session()

    def post(self, url, data=None, json=None, **kwargs):
        return self.request(url, "POST", data, json, **kwargs)

    def get(self, url, **kwargs):
        return self.request(url, "GET", **kwargs)

    def delete(self):
        pass

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
