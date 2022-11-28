from faker import Faker

fake = Faker("zh_CN")


class FakerTool(object):
    """获取名字"""

    def get_name(self):
        # print(fake.name())
        return fake.name()

    """获取手机号码"""

    def get_phone_number(self):
        # print(fake.phone_number())
        return fake.phone_number()

    """获取随机密码，长度为len"""
    def get_password(self, len):
        return fake.password(length=len, special_chars=False, digits=True, upper_case=True, lower_case=True)


if __name__ == '__main__':
    test = FakerTool()
    test.get_name()
    test.get_phone_number()
    print(test.get_password(10))
