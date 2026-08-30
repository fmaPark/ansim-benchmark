"""P7 near-miss — 관리 라우트에 인증 장식자가 붙어 있다 (0414 §7.3.4 충족)."""

from flask import Flask, jsonify
from flask_login import login_required

app = Flask(__name__)


@app.route("/admin/reports")
@login_required
def admin_reports():
    return jsonify([{"id": 1, "title": "weekly"}])
