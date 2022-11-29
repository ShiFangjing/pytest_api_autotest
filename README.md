# pytest_api_autotest
An example about interface autotest based on pytest framework


2022/11/24

todo1：加解密封装   done

todo2：mock封装

todo3：sha256加解密   done

todo4：日志装饰器       done http；undo redis mysql

todo5：main.py完善，生成报告，重跑上次失败的用例

todo6：pytest与jenkis结合

todo7：fixture.cache的使用

todo8：完成Readme.md


框架介绍：
 Python + pytest + allure + log + yaml + mysql + redis 
 
目录结构：
|——api                        接口封装成方法
|——config
|    |————envi.ini            环境配置数据
|    |————read_config.py      读取环境配置数据
|——data                       测试数据，yaml方式存储，并提供了yaml数据的读取方法
|——log                        日志存储路径
|——test_case                  测试用例
|——utils                      各种工具类
 
