import configparser
import os
import configparser


class ReadConfig(object):

    @staticmethod
    def read_base_url():
        config = configparser.ConfigParser()
        path = os.path.join(os.path.pardir, 'config\envi.ini')
        config.read(path, encoding="utf-8")
        return config.get('test', 'url')

    @staticmethod
    def read_redis_info():
        config = configparser.ConfigParser()
        path = os.path.join(os.path.pardir, 'config\envi.ini')
        config.read(path, encoding="utf-8")
        return config.items('redis')

    @staticmethod
    def read_database_info():
        config = configparser.ConfigParser()
        path = os.path.join(os.path.pardir, 'config\envi.ini')
        config.read(path, encoding="utf-8")
        return config.items('mysql')


if __name__ == '__main__':
    print(os.path.pardir)
    print(ReadConfig.read_database_info()[0][1])
    print(ReadConfig.read_database_info()[1][1])
    print(ReadConfig.read_database_info()[2][1])
