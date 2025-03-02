from config import DevConfig
from flask import Flask


def create_app():
    app = Flask(__name__)

    # 加载配置
    app.config.from_object(DevConfig)

    # 蓝图注册，这里需要延时导包，避免循环引用
    from learn import routes
    app.register_blueprint(routes.main_bp)

    return app
