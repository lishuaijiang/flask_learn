from config import DevConfig
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)

    app.config.from_object(DevConfig)

    db.init_app(app)
    migrate.init_app(app, db)

    from learn import models

    from learn import routes
    app.register_blueprint(routes.main_bp)

    return app
