from flask import Blueprint, request, jsonify
from flask_login import login_user, current_user, login_required, logout_user
from learn import models

main_bp = Blueprint('main_bp', __name__)


@main_bp.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    remember_me = request.json.get('remember', False)

    user = models.User.query.filter(
        models.User.username == username,
        models.User.password_hash == password
    ).first()
    if user is None:
        return jsonify({"msg": "invalid username or password"}), 401

    login_user(user, remember=remember_me)
    return jsonify({"msg": f"welcome {current_user.username}"}), 200

"""
前后端不分离示例，着重点是 next_page 的跳转
@main_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            # 防止重定向攻击，如：?next=https://www.baidu.com
            if not next_page or not next_page.startswith('/'):
                next_page = url_for('main_bp.index')
            return redirect(next_page)
        else:
            flash("账号不存在或密码错误")
    return render_template("login.html", form=form)
"""


@main_bp.route('/logout')
def logout():
    logout_user()
    return jsonify({"msg": "logout"}), 200


@main_bp.route('/')
@login_required
def hello():
    return f"Hi~, {current_user.username}!"
