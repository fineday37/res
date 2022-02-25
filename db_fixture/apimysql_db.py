import configparser

import pymysql

from config import setting

cf = configparser.ConfigParser()
cf.read(setting.TEST_CONFIG)

# 读取数据库配置
host = cf.get("mysqlconf", "host")
port = cf.get("mysqlconf", "port")
user = cf.get("mysqlconf", "user")
password = cf.get("mysqlconf", "password")
db_name = cf.get("mysqlconf", "db_name")


class DB:
    def __init__(self):
        try:
            self.conn = pymysql.connect(
                port=int(port),
                host=host,
                user=user,
                password=password,
                db=db_name,
                charset="utf8mb4"
            )
        except pymysql.OperationalError as e:
            print("mysql error %d: %s" % (e.args[0], e.args[1]))

    # 清空表数据
    def clear(self, table_name):
        real_sql = "delete from " + table_name + ";"
        with self.conn.cursor() as cursor:
            cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
            cursor.execute(real_sql)
        self.conn.commit()

    # 新增数据
    def insert(self, table_name, table_data):
        # 遍历list元素，转成字符串
        for key in table_data:
            table_data[key] = "'" + str(table_data[key]) + "'"

        key = ','.join(table_data.keys())
        value = ','.join(table_data.values())
        real_sql = "INSERT INTO " + table_name + " (" + key + ") VALUES (" + value + ") "
        with self.conn.cursor() as cursor:
            cursor.execute(real_sql)
        self.conn.commit()

    # 关闭数据库
    def close(self):
        self.conn.close()

    # 初始化数据
    def init_data(self, datas):
        for table, data in datas.items():
            self.clear(table)
            for d in data:
                self.insert(table, d)
        self.close()
