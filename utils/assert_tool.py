class AssertTool(object):
    """
    判断actual_json在不在target_json中
    """

    @classmethod
    def assert_json_contains(self, actual_json, target_json):
        result_list = self._assert_json_sep(self, actual_json, target_json)
        # 如果json中有一个value不相等，返回False
        assert result_list.count(False) < 1

    """判断json的每个key的value是否相等"""

    def _assert_json_sep(self, actual_json, target_json):
        result = []
        keys = actual_json.keys()
        for key in keys:
            if isinstance(actual_json.get(key), dict) and isinstance(target_json.get(key), dict):
                # list类型的用extend
                result.extend(self._assert_json_sep(self, actual_json.get(key), target_json.get(key)))
            elif isinstance(actual_json.get(key), list) and isinstance(target_json.get(key), list):
                # TODO 待完成json array类型的相等判断
                pass
            elif not actual_json.get(key) == target_json.get(key) or actual_json.get(key) is None:
                # 单个元素类型的用append
                result.append(False)
            else:
                # 单个元素类型的用append
                result.append(True)
        return result


# 测试方法
if __name__ == '__main__':
    json1 = {'data': None, 'errorCode': -1, 'errorMsg': '参数不合法！'}
    json2 = {"data": {"link": "www.github.com2", "name": "github2"}, "errorCode": 0, "errorMsg": ""}
    print(AssertTool.assert_json_contains(json2, json1))
