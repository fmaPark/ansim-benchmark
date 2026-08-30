"""P7 — 관리자 화면 접근 통제 부재 (0414 §7.3.4).

인증·인가 장식자 없이 관리 라우트를 노출한다.
"""

from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/admin/users")
def admin_users():
    rows = [{"id": 1, "nickname": "hong"}, {"id": 2, "nickname": "kim"}]
    return jsonify(rows)
