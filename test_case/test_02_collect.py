import pytest

from api.collect import Collect
from config.read_config import ReadConfig

base_url = ReadConfig.read_base_url()
# case_data = ReadYaml.read_yaml('user.yaml')
col = Collect(base_url)


class TestCollect():

    def test_collect_normal(self, get_cookie):
        cookie = get_cookie
        params2 = {'name': 'Baidu',
                   'link': 'www.baidu.com'}
        res = col.add_collect(data = params2, cookies = cookie)
        print(res.json())

    def test_collect_unregister(self):
        pass

    def test_collect_unlogin(self):
        pass

    def test_collect_logout(self):
        pass


if __name__ == '__main__':
    pytest.main()