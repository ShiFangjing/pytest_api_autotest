import os

import pytest

from utils.log_control import INFO


def run():
    INFO.logger.info(
        """
                             _    _         _      _____         _
              __ _ _ __ (_)  / \\  _   _| |_ __|_   _|__  ___| |_
             / _` | '_ \\| | / _ \\| | | | __/ _ \\| |/ _ \\/ __| __|
            | (_| | |_) | |/ ___ \\ |_| | || (_) | |  __/\\__ \\ |_
             \\__,_| .__/|_/_/   \\_\\__,_|\\__\\___/|_|\\___||___/\\__|
                  |_|
                  开始执行{}项目...
                """
    )

    # 判断现有的测试用例，如果未生成测试代码，则自动生成
    # TestCaseAutomaticGeneration().get_case_automatic()

    pytest.main(['-s', '-W', 'ignore:Module already imported:pytest.PytestWarning',
                 '--alluredir', 'report', "--clean-alluredir"])

    """
                   --reruns: 失败重跑次数
                   --count: 重复执行次数
                   -v: 显示错误位置以及错误的详细信息
                   -s: 等价于 pytest --capture=no 可以捕获print函数的输出
                   -q: 简化输出信息
                   -m: 运行指定标签的测试用例
                   -x: 一旦错误，则停止运行
                   --maxfail: 设置最大失败次数，当超出这个阈值时，则不会在执行测试用例
                    "--reruns=3", "--reruns-delay=2"
                   """

    os.system(r"allure generate report -o report/html --clean")


if __name__ == '__main__':
    run()
