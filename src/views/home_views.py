
from flask import render_template, Blueprint

from database import db #DB 객체 불러옴
from models import User #사용할 테이블 모델 불러옴

bp = Blueprint('main', __name__)

@bp.route("/")
def home():
    all_users = User.query.all()
    return render_template("index.html", users=all_users)