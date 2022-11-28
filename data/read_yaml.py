import os

import yaml


class ReadYaml(object):
    @staticmethod
    def read_yaml(filename=None):
        filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)),  filename)
        print(filepath)
        with open(filepath, 'r', encoding='utf-8') as f:
            value = yaml.load(f, Loader=yaml.FullLoader)
        return value


# 读取yaml的测试方法
if __name__ == '__main__':
    print(ReadYaml.read_yaml('collect.yaml'))
