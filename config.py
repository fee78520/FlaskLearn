# -*- coding: utf-8 -*-
# @Time    : 2019/12/14 22:11
# @Author  : LiPengfei
# @File    : config.py

class Config(object):
    pass

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:password@127.0.0.1:3306/pf_site?charset=utf8mb4'
    SQLALCHEMY_TRACK_MODIFICATIONS = True   # 防止sqlalchenmy 弹出warning，，，，，禁止数据的修改追踪(需要消耗资源)
