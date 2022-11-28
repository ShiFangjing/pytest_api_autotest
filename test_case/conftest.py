import pytest

from api.user import User
from config.read_config import ReadConfig
only_cookie = {}
base_url = ReadConfig().read_base_url()


@pytest.fixture(scope='function')
def delete_user():
    # TODO: 删除用户操作，从数据库中删掉该用户
    pass


@pytest.fixture(scope='function')
def delete_user_collections():
    # TODO: 删除用户的所有收藏
    yield


@pytest.fixture(scope='session', autouse=True)
def get_cookie():
    print("用户登录")
    user = User(base_url)
    params = {'username': 'sfj123456',
              'password': 'sfj123456'}
    res = user.login(data=params)
    only_cookie = res.cookies
    return only_cookie


@pytest.fixture(scope='session', autouse=True)
def logout():
    yield
    print("用户登出")
    user = User(base_url)
    user.logout(cookies=only_cookie)
