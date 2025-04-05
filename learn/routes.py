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


@main_bp.route('/logout')
def logout():
    logout_user()
    return jsonify({"msg": "logout"}), 200


@main_bp.route('/')
@login_required
def hello():
    return f"Hi~, {current_user.username}!"
