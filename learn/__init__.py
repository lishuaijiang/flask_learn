from config import DevConfig
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)

    # 加载配置
    app.config.from_object(DevConfig)

    # 加载扩展
    db.init_app(app)
    migrate.init_app(app, db)

    # 导入模型，确保模型被加载，否则在执行 flask db migrate 迁移时会遇到错误：No changes in schema detected.
    from learn import models

    # 蓝图注册
    from learn import routes
    app.register_blueprint(routes.main_bp)

    return app
