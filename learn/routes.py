from flask import Blueprint

main_bp = Blueprint("main_bp", __name__)


@main_bp.route("/")
def hello():
    return "Hi~"
