from config import DevConfig
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

"""
可选，自定义一个 auto_commit 过程
from contextlib import contextmanager
from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy


class SQLAlchemy(_SQLAlchemy):

    @contextmanager
    def auto_commit(self):
        try:
            yield
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e

db = SQLAlchemy()
使用时
with db.auto_commit():
    ...
    db.session.add(obj)
"""

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    # 加载配置
    app.config.from_object(DevConfig)

    # 加载扩展
    db.init_app(app)

    # 导入模型，确保模型被加载
    from learn import models

    # 注册蓝图
    from learn import routes
    app.register_blueprint(routes.main_bp)

    # 注册命令行
    from learn import clis
    app.cli.add_command(clis.initdb)
    app.cli.add_command(clis.cleandb)
    app.cli.add_command(clis.resetdb)

    return app
