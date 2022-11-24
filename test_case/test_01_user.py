import pytest
from api.user import User
from config.read_config import ReadConfig
from data.read_yaml import ReadYaml

base_url = ReadConfig.read_base_url()
case_data = ReadYaml.read_yaml('user.yaml')
user = User(base_url)


class TestUser:
    def test_login_normal(self):
        print(base_url)
        print(case_data)

    #
    # def test_login_register_repeat(self):
    #     pass
    #
    # def test_login_logout_repeat(self):
    #     pass


if __name__ == '__main__':
    pytest.main()
