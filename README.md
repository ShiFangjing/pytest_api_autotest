# pytest_api_autotest
![alt](https://img.shields.io/badge/Rebecca-1996-brightgreen) ![](https://img.shields.io/badge/updated-today-brightgreen)


## 安装步骤
pip install -r requirements.txt

## 框架介绍

:call_me_hand: 基本框架：Python + pytest + allure + log + yaml + mysql + redis 

:call_me_hand:支持范围：

​    ⭐ 支持测试用例与测试数据分离

​    ⭐ 支持测试前置和后置步骤

​    ⭐ 支持复杂json断言

​    ⭐ 支持MySQL和Redis的增删改查

​    ⭐支持生成用例日志

​    ⭐支持生成Allure测试报告

## 目录结构

|——api                          接口封装成方法

|——config                     配置文件夹

|————envi.ini                       环境配置数据

|————read_config.py         读取环境配置数据

|——data                      测试数据，yaml方式存储，并提供了yaml数据的读取方法

|——log                        日志存储路径

|——test_case             测试用例

|——utils                      各种工具类

|——report                  测试报告存放路径

## 更新日志

2022/11/30：完善README，增加安装步骤，requirements.txt，完善注释规范



## 待完善

todo1：加解密封装   done

todo2：mock封装

todo3：sha256加解密   done

todo4：日志装饰器       done http；undo redis mysql

todo5：main.py完善，生成报告，重跑上次失败的用例

todo6：pytest与jenkis结合

todo7：fixture.cache的使用

todo8：完成Readme.md

