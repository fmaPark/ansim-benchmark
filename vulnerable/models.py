"""P10 — 보유기간이 지난 개인정보의 정리 경로 부재 (0414 §7.3.5).

모델은 개인정보 컬럼을 들고 있으나 저장소 어디에도 그 경로가 없다.
"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64))
    phone = db.Column(db.String(32))
    joined_at = db.Column(db.DateTime)
