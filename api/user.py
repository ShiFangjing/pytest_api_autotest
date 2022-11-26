from utils.request_tool import RequestTool


class User(RequestTool):

    def __init__(self, api_root_url):
        super(User, self).__init__(api_root_url)

    """注册用户"""

    def register(self, **kwargs):
        return self.post("/user/register", **kwargs)

    """登录用户"""

    def login(self, **kwargs):
        return self.post("/user/login", **kwargs)

    """"登出用户"""

    def logout(self, **kwargs):
        return self.get("/user/logout/json", **kwargs)


if __name__ == '__main__':
    user = User('https://www.wanandroid.com')
    params = {'username': 'sfj123456',
              'password': 'sfj123456'}

    response = user.login(data=params)
    cookie = response.cookies
    print(dict(cookie))
    # for item in list(cookie):
    #     print(item)
