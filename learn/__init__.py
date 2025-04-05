from config import DevConfig
from flask import Flask, jsonify
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__)
    app.config.from_object(DevConfig)

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    from learn import models

    # 用户加载回调函数。是 Flask-Login 的必要装饰器，全程由 Flask-Login 调用
    @login_manager.user_loader
    def load_user(id):
        """
        工作原理：
        1. 用户登录成功 --> Flask-Login 在会话中存储 user_id
        2. 用户访问其他页面 --> Flask-Login 从会话中读取 user_id
        3. 调用 load_user(id) 获取完整的用户对象
        4. 通过 current_user 代理对象在视图函数中使用该用户
        """
        return models.User.query.get(int(id))

    # 处理未登录时访问 login_required 装饰的接口
    # 方式一：接口返回 json 信息
    @login_manager.unauthorized_handler
    def unauthorized():
        return jsonify({"msg": "Login first, please"}), 401

    # 方式二：让浏览器重定向到登录页面（用于前后端不分离）
    # login_manager.login_view = 'login'

    from learn.routes import main_bp
    app.register_blueprint(main_bp)

    return app
