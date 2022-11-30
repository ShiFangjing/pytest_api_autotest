from utils.request_tool import RequestTool


class Collect(RequestTool):
    def __init__(self, api_root_url):
        super(Collect, self).__init__(api_root_url)

    def add_collect(self, **kwargs):
        """"添加收藏"""
        return self.post("/lg/collect/addtool/json", **kwargs)

    def query_collect(self, **kwargs):
        """查询收藏"""
        return self.get("/lg/collect/usertools/json", **kwargs)

    def update_collect(self, **kwargs):
        """"编辑收藏"""
        return self.post("/lg/collect/updatetool/json", **kwargs)

    def delete_collect(self, **kwargs):
        """"删除收藏"""
        return self.post("/lg/uncollect_originId/2333/json", **kwargs)


# 测试代码
if __name__ == '__main__':
    collect = Collect('https://www.wanandroid.com')
    params2 = {'name': 'Baidu',
               'link': 'www.baidu.com'}

    cookie = dict(loginUserName_wanandroid_com='sfj123456',
                  token_pass_wanandroid_com='',
                  JSESSIONID='',
                  loginUserName='',
                  token_pass='')
    res = collect.add_collect(data=params2, cookies=cookie)
    print(res.json())
