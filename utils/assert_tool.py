class AssertTool(object):
    """
    判断actual_json在不在target_json中
    TODO:待完成嵌套式json断言功能
    """
    @staticmethod
    def assert_json_contains(actual_json, target_json):
        keys = target_json.keys()
        for key in keys:
            if actual_json.get(key) != target_json.get(key):
                return False
        return True


# 测试方法
if __name__ == '__main__':
    json1 = {"data": "", "errorCode": 0, "errorMsg": ""}
    json2 = {"errorCode": 0, "errorMsg": ""}
    print(AssertTool.assert_json_contains(json1,json2))
