from faker import Faker

fake = Faker("zh_CN")


class FakerTool(object):

    """获取名字"""
    def get_name(self):
        print(fake.name())
        return fake.name()

    """获取手机号码"""
    def get_phone_number(self):
        print(fake.phone_number())
        return fake.phone_number()


# if __name__ == '__main__':
#     test = FakerTool()
#     test.get_name()
#     test.get_phone_number()
