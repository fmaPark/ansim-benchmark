"""P6 · SEC-05 — 개인정보 평문 저장 (0414 §7.3.4).

P6: 주민등록번호를 암호화·해시 없이 그대로 DB에 적재한다.
SEC-05: 체크섬을 통과하는 합성 주민등록번호 리터럴이 소스에 남아 있다.
"""

SEED_RRN = "900101-1234568"


def save_member(conn, nickname, rrn):
    cur = conn.cursor()
    cur.execute("INSERT INTO members (nickname, rrn) VALUES (?, ?)", (nickname, rrn))
    conn.commit()


def seed(conn):
    save_member(conn, "hong", SEED_RRN)
