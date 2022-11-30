from utils.request_tool import RequestTool


class User(RequestTool):

    def __init__(self, api_root_url):
        super(User, self).__init__(api_root_url)

    def register(self, **kwargs):
        """注册用户"""
        return self.post("/user/register", **kwargs)

    def login(self, **kwargs):
        """登录用户"""
        return self.post("/user/login", **kwargs)

    def logout(self, **kwargs):
        """"登出用户"""
        return self.get("/user/logout/json", **kwargs)


# 测试代码
if __name__ == '__main__':
    user = User('https://www.wanandroid.com')
    params = {'username': 'sfjXXXXXX',
              'password': 'sfjXXXXXX'}

    response = user.login(data=params)
    cookie = response.cookies
    print(dict(cookie))
    # for item in list(cookie):
    #     print(item)
