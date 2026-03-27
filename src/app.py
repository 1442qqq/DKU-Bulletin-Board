from flask import Flask
import os
from database import db #DB 임포트
from views import home_views #블루프린트 임포트
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

#환경변수에서 DB주소를 가져옴
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app) #DB 연결
print(os.getenv("DATABASE_URL"))

app.register_blueprint(home_views.bp) #home_views 블루프린트 등록

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

