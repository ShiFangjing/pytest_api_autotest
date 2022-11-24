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


if __name__ == '__main__':
    print(os.path.pardir)
    print(ReadConfig.read_base_url())
