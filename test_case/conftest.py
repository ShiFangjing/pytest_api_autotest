import pytest

from api.user import User


@pytest.fixture(scope='function')
def delete_user():
    # TODO: 删除用户操作，从数据库中删掉该用户
    pass


@pytest.fixture(scope='session')
def get_cookie():
    user = User('https://www.wanandroid.com')
    params = {'username': 'sfj123456',
              'password': 'sfj123456'}
    res = user.login(data=params)
    return dict(res.cookies)
