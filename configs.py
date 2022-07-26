# -*- coding: UTF-8 -*-

# 配置文件
# 数据库信息
HOST = 'xxx.cn'
PORT = '3306'
DATABASE = 'ar'
USERNAME = 'xxx'
PASSWORD = 'xxxxxx'
#DB_URI = 'mysql+mysqldb://{}:{}@{}:{}/{}'.format(USERNAME, PASSWORD, HOST, PORT, DATABASE)
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(USERNAME, PASSWORD, HOST, PORT, DATABASE)
# 数据库连接编码
DB_CHARSET = "utf8"

SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True