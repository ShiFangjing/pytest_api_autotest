import pymysql
from config.read_config import ReadConfig


class MySQLTool(object):

    def __init__(self, database):
        address = eval(ReadConfig.read_database_info()[0][1])
        user = eval(ReadConfig.read_database_info()[1][1])
        passwd = eval(ReadConfig.read_database_info()[2][1])
        self.db = pymysql.connect(host=address,
                                  user=user,
                                  password=passwd,
                                  database=database)
        self.cursor = self.db.cursor()

    """"查询一条数据"""
    def query_one(self, query_sql):
        self.cursor.execute(query_sql)
        data = self.cursor.fetchone()
        self.db.close()
        return data

    """"查询所有数据"""
    def query_all(self, query_sql):
        self.cursor.execute(query_sql)
        data = self.cursor.fetchone()
        self.db.close()
        return data

    """更新数据"""
    def update(self, update_sql):
        try:
            self.cursor.execute(update_sql)
            # 提交到数据库执行
            self.db.commit()
        except:
            # 如果发生错误则回滚
            self.db.rollback()
            # 关闭数据库连接
        self.db.close()

    """删除一条数据"""
    def delete(self, delete_sql):
        try:
            self.cursor.execute(delete_sql)
            # 提交到数据库执行
            self.db.commit()
        except:
            # 如果发生错误则回滚
            self.db.rollback()
            # 关闭数据库连接
        self.db.close()
