from dotenv import load_dotenv
# 程序启动第一时间加载环境变量，防止后续使用环境变量时因为加载过晚导致环境变量为 None 问题
load_dotenv()
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@192.168.31.3:3307/flask_learn'
# 禁用 SQLAlchemy 的修改追踪，减少性能开销
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    hash_password = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    test = db.Column(db.Boolean, nullable=False, default=False)


@app.route('/')
def hello():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(port=5001)
