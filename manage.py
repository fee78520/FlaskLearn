# -*- coding:utf-8 -*-
from flask_script import Manager, Server

from main import app


manager = Manager(app)

manager.add_command('server', Server())

@manager.shell
def make_shell_context():
    """
    之所以使用manage.py运行是因为未来可能添加扩展，一些扩展会在flask执行后才能运行
    :return:
    """
    return dict(app=app)


if __name__ == '__main__':
    manager.run()
