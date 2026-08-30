"""P6 near-miss — 개인정보를 해시로 변환해 저장한다 (0414 §7.3.4 충족)."""

import hashlib


def _digest(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def save_member(conn, nickname, rrn):
    hashed = _digest(rrn)
    cur = conn.cursor()
    cur.execute("INSERT INTO members (nickname, rrn_hash) VALUES (?, ?)", (nickname, hashed))
    conn.commit()
