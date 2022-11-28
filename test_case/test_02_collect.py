import pytest

from api.collect import Collect
from config.read_config import ReadConfig
from data.read_yaml import ReadYaml

base_url = ReadConfig.read_base_url()
case_data = ReadYaml.read_yaml('collect.yaml')
col = Collect(base_url)


class TestCollect():

    def test_collect_normal(self, get_cookie, delete_user_collections):
        cookie = get_cookie
        # 添加收藏
        res = col.add_collect(data=case_data[0]['body'][0], cookies=cookie)

        # 查询收藏

    def test_update_collect(self, get_cookie, delete_user_collections):
        cookie = get_cookie
        # 添加收藏
        res = col.add_collect(data=case_data[0]['body'][0], cookies=cookie)
        # 修改收藏
        # 查询修改后的收藏

    def test_delete_collect(self, get_cookie, delete_user_collections):
        pass

    def test_collect_unregister(self):
        pass

    def test_collect_unlogin(self):
        pass

    def test_collect_logout(self):
        pass


if __name__ == '__main__':
    pytest.main(['-vs', 'test_02_collect.py'])
