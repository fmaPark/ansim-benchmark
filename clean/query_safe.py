"""AUX-01 near-miss — 파라미터 바인딩 쿼리."""


def find_order(conn, order_id: str):
    cur = conn.cursor()
    cur.execute("SELECT id, total FROM orders WHERE id = ?", (order_id,))
    return cur.fetchall()
