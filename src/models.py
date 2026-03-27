# DB의 구조를 파이썬에서 참조하기 쉽게 만드는 역할

from database import db
from datetime import datetime, timezone
import enum

class UserRole(enum.Enum):
    USER="USER"
    ADMIN="ADMIN"

    
class User(db.Model):
    __tablename__ = 'user' #실제 테이블 이름과 매칭
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc), nullable=False)
    nickname = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(127), nullable=False)
    role = db.Column(db.Enum(UserRole), nullable=False, default=UserRole.USER)
    user_id = db.Column(db.String(20), unique=True, nullable=False)
