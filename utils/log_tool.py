from functools import wraps
from utils.log_control import INFO, ERROR

"""
日志装饰器，控制程序日志输入，默认为 True
如设置 False，则程序不会打印日志
"""


def log_decorator(switch: bool):
    """
    封装日志装饰器, 打印请求信息
    :param switch: 定义日志开关
    :return:
    """

    def decorator(func):
        @wraps(func)
        def swapper(*args, **kwargs):

            # 判断日志为开启状态，才打印日志
            res = func(*args, **kwargs)
            # 判断日志开关为开启状态
            if switch:
                _log_msg = f"\n======================================================\n" \
                           f"请求路径: {res.url}\n" \
                           f"请求方法: {res.request.method}\n" \
                           f"请求头: {res.request.headers}\n" \
                           f"响应状态码: {res.status_code}\n" \
                           f"请求内容: {res.request.body}\n" \
                           f"响应体: {res.text}\n" \
                           "====================================================="
                # 判断正常打印的日志，控制台输出绿色
                if res.status_code == 200:
                    INFO.logger.info(_log_msg)
                else:
                    # 失败的用例，控制台打印红色
                    ERROR.logger.error(_log_msg)
            return res

        return swapper

    return decorator
