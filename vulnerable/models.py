"""P10 — 보유기간이 지난 개인정보의 정리 경로 부재 (0414 §7.3.5)."""

db = None      # 실제 ORM 핸들은 애플리케이션이 주입한다


class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64))
    phone = db.Column(db.String(32))
    joined_at = db.Column(db.DateTime)
