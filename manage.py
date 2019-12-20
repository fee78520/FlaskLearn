# -*- coding: utf-8 -*-
# @Time    : 2019/12/14 22:11
# @Author  : LiPengfei
# @File    : manage.py
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand

from main import app, db, User, Post, Comment, Tag


migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('server', Server())
manager.add_command('db', MigrateCommand)

@manager.shell
def make_shell_context():
    """
    之所以使用manage.py运行是因为未来可能添加扩展，一些扩展会在flask执行后才能运行
    :return:
    """
    return dict(app=app, db=db, User=User, Post=Post, Comment=Comment, Tag=Tag)


if __name__ == '__main__':
    manager.run()
