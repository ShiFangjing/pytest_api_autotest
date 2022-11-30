import configparser
import os
import configparser
# envi.ini文件路径，绝对路径
ini_path = path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'config\envi.ini')


class ReadConfig(object):

    @staticmethod
    def read_base_url():
        """ 读取接口地址 """
        config = configparser.ConfigParser()
        config.read(ini_path, encoding="utf-8")
        return config.get('test', 'url')

    @staticmethod
    def read_redis_info():
        """ 读取Redis信息 """
        config = configparser.ConfigParser()
        config.read(ini_path, encoding="utf-8")
        return config.items('redis')

    @staticmethod
    def read_database_info():
        """" 读取MySQL信息 """
        config = configparser.ConfigParser()
        config.read(ini_path, encoding="utf-8")
        return config.items('mysql')


if __name__ == '__main__':
    # print(os.path.exists('..\config\envi.ini'))
    print(ReadConfig.read_base_url())
