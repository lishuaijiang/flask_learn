from config import DevConfig
from flask import Flask
from learn import routes

def create_app():
    app = Flask(__name__)

    # 加载配置
    app.config.from_object(DevConfig)

    # 蓝图注册
    app.register_blueprint(routes.main_bp)

    # 命令注册
    from learn import clis
    app.cli.add_command(clis.greet)
    app.cli.add_command(clis.current_time)

    return app
