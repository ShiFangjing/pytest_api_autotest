from utils.request_tool import RequestTool


class User(RequestTool):

    def __init__(self, api_root_url):
        super(User, self).__init__(api_root_url)

    def register(self, **kwargs):
        return self.post("/user/register", **kwargs)

    def login(self, **kwargs):
        return self.post("/user/login", **kwargs)

    def logout(self, **kwargs):
        return self.get("/user/logout/json", **kwargs)


if __name__ == '__main__':
    user = User('https://www.wanandroid.com')
    params = {'username': 'sfj123456',
              'password': 'sfj123456'}

    response = user.login(data=params)
    print(response.json())
