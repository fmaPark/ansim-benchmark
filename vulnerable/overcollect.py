"""P1 — 목적에 비해 과도한 개인정보 수집 (0414 §7.3.2).

P1은 저장소 전체의 수집 필드 집합에서 합성된다. 이 파일이 그 목록을 넓힌다.
"""

from flask import request


def newsletter_form():
    return {
        "name": request.form["name"],
        "birth": request.form["birth"],
        "address": request.form["address"],
        "phone": request.form["phone"],
    }
