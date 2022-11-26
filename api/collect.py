from utils.request_tool import RequestTool


class Collect(RequestTool):
    def __init__(self, api_root_url):
        super(Collect, self).__init__(api_root_url)

    """"添加收藏"""

    def add_collect(self, **kwargs):
        return self.post("/lg/collect/addtool/json", **kwargs)

    """查询收藏"""

    def query_collect(self, **kwargs):
        return self.get("/lg/collect/usertools/json", **kwargs)

    """"编辑收藏"""

    def update_collect(self, **kwargs):
        return self.post("/lg/collect/updatetool/json", **kwargs)

    """"删除收藏"""

    def delete_collect(self, **kwargs):
        return self.post("/lg/uncollect_originId/2333/json", **kwargs)


if __name__ == '__main__':
    collect = Collect('https://www.wanandroid.com')
    params2 = {'name': 'Baidu',
               'link': 'www.baidu.com'}

    cookie = dict(loginUserName_wanandroid_com='sfj123456',
                  token_pass_wanandroid_com='aa2747519eeb8e1b550e4d4d3e78cb66',
                  JSESSIONID='8822C6551AF57B855E2316A5CF0E3099',
                  loginUserName='sfj123456',
                  token_pass='aa2747519eeb8e1b550e4d4d3e78cb66')
    res = collect.add_collect(data=params2, cookies=cookie)

    print(res.json())
