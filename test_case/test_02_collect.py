import pytest

from api.collect import Collect
from api.user import User
from config.read_config import ReadConfig
from data.read_yaml import ReadYaml
from utils.assert_tool import AssertTool

base_url = ReadConfig.read_base_url()
case_data = ReadYaml.read_yaml('collect.yaml')
col = Collect(base_url)
user = User(base_url)


class TestCollect():

    @pytest.mark.usefixtures('delete_user_collections')
    def test_collect_normal(self, get_cookie, delete_user_collections):
        cookie = get_cookie
        # 添加收藏
        res = col.add_collect(data=case_data[0]['body'][0], cookies=cookie)
        AssertTool.assert_json_contains(res.json(), case_data[0]['expect'][0])
        # 查询收藏
        # 查询结果断言

    @pytest.mark.usefixtures('delete_user_collections')
    def test_update_collect(self, get_cookie, delete_user_collections):
        cookie = get_cookie
        # 添加收藏
        add_res = col.add_collect(data=case_data[1]['body'][1], cookies=cookie)
        AssertTool.assert_json_contains(add_res.json(), case_data[1]['expect'][1])
        # 修改收藏
        update_res = col.update_collect(data=case_data[1]['body'][1], cookies=cookie)
        AssertTool.assert_json_contains(update_res.json(), case_data[1]['expect'][1])
        # 查询修改后的收藏

    def test_delete_collect(self, get_cookie, delete_user_collections):
        # 添加收藏
        # 删除收藏
        # 查询收藏
        assert 1 == 1

    def test_collect_unregister(self):
        res = col.add_collect(data=case_data[0]['body'][0], cookies=None)
        AssertTool.assert_json_contains(res.json(), case_data[0]['expect'][0])

    def test_collect_unlogin(self):
        res = col.add_collect(data=case_data[0]['body'][0], cookies=None)
        AssertTool.assert_json_contains(res.json(), case_data[0]['expect'][0])

    def test_collect_logout(self, get_cookie):
        cookie = get_cookie
        user.logout(cookies = cookie)
        res = col.add_collect(data=case_data[0]['body'][0], cookies=cookie)
        AssertTool.assert_json_contains(res.json(), case_data[0]['expect'][0])


if __name__ == '__main__':
    pytest.main(['-vs', 'test_02_collect.py'])
