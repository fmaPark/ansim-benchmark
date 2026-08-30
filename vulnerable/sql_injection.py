"""AUX-01 — f-string 조립 SQL 실행 (0259 §9.4)."""

import sqlite3


def find_order(conn: sqlite3.Connection, order_id: str):
    cur = conn.cursor()
    cur.execute(f"SELECT id, total FROM orders WHERE id = '{order_id}'")
    return cur.fetchall()
