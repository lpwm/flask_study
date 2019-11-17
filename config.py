import os

DEBUG = True
TEMPLATE_DEBUG = True

# 操作session会话需要用到的密钥
SECRET_KEY = os.urandom(24)

# Flask jsonify返回中文不转码
JSON_AS_ASCII = False

# 数据库配置
HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'flask_study'
USERNAME = 'root'
PASSWORD = 'lpwm86'

# Python 3.x中需要使用PyMySQL作为数据库中间件
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,
                                                              PASSWORD, HOSTNAME, PORT, DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_TRACK_MODIFICATIONS = False
