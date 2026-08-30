"""P2 — 동의 처리 없이 개인정보 수집 (0414 §7.3.2)."""

from flask import request


def signup():
    return {
        "phone": request.form["phone"],
        "email": request.form["email"],
    }
