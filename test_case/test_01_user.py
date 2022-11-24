import pytest
from api.user import User
from config.read_config import ReadConfig
from data.read_yaml import ReadYaml
from utils.assert_tool import AssertTool

base_url = ReadConfig.read_base_url()
case_data = ReadYaml.read_yaml('user.yaml')
user = User(base_url)


class TestUser:
    def test_login_normal(self):
        # print(base_url)
        # print(case_data)
        register_result = user.register(data=case_data[0]['body'][0])
        AssertTool.assert_json_contains(register_result.json(), case_data[0]['expect'][0])

        login_result = user.login(data=case_data[0]['body'][1])
        AssertTool.assert_json_contains(login_result.json(), case_data[0]['expect'][1])

        logout_result = user.logout(data=case_data[0]['body'][2])
        AssertTool.assert_json_contains(logout_result.json(), case_data[0]['expect'][2])

    # def test_login_register_repeat(self):
    #     pass
    #
    # def test_login_logout_repeat(self):
    #     pass


if __name__ == '__main__':
    pytest.main()
