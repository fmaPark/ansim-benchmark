"""P6 해소 — 개인정보를 해시로 변환해 저장한다 (0414 §7.3.4 충족).

v1-danger에서 평문 적재와 리터럴 주민등록번호를 걷어낸 상태다.
"""

import hashlib


def _digest(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def save_member(conn, nickname, rrn):
    hashed = _digest(rrn)
    cur = conn.cursor()
    cur.execute("INSERT INTO members (nickname, rrn_hash) VALUES (?, ?)", (nickname, hashed))
    conn.commit()
