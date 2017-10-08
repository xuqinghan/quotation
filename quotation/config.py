import os

#返回中文
JSON_AS_ASCII = False

#db路径
INSTANCE_FOLDER_PATH = '/code'
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = 'sqlite:////' + INSTANCE_FOLDER_PATH + '/db/db.sqlite'
