import pytest
from api.user import User
from config.read_config import ReadConfig
from data.read_yaml import ReadYaml
from utils.assert_tool import AssertTool

base_url = ReadConfig.read_base_url()
case_data = ReadYaml.read_yaml('user.yaml')
user = User(base_url)


class TestUser:
    @pytest.mark.usefixtures('delete_user')
    def test_login_normal(self):
        # 注册
        register_result = user.register(data=case_data[0]['body'][0])
        AssertTool.assert_json_contains(register_result.json(), case_data[0]['expect'][0])
        # 登录
        login_result = user.login(data=case_data[0]['body'][1])
        AssertTool.assert_json_contains(login_result.json(), case_data[0]['expect'][1])
        # 登出
        logout_result = user.logout(data=case_data[0]['body'][2])
        AssertTool.assert_json_contains(logout_result.json(), case_data[0]['expect'][2])

    @pytest.mark.usefixtures('delete_user')
    @pytest.mark.parametrize('in_data,expect_data',
                             [(a, b) for a, b in zip(case_data[1]['body'], case_data[1]['expect'])],
                             ids=['第一次登录', '第二次登录', '第三次登录'])
    def test_login_register_repeat(self, in_data, expect_data):
        register_result = user.register(data=in_data)
        AssertTool.assert_json_contains(register_result.json(), expect_data)


    # def test_login_logout_repeat(self):
    #     pass


if __name__ == '__main__':
    pytest.main(['-vs', 'test_02_user.py'])
