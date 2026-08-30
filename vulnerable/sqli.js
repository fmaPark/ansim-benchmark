// AUX-01(JS) — 템플릿 리터럴로 조립한 SQL 실행 (0259 §9.4)
const mysql = require("mysql2");

const conn = mysql.createConnection({ host: "127.0.0.1", database: "bench" });

function findOrder(orderId) {
  return conn.query(`SELECT id, total FROM orders WHERE id = ${orderId}`);
}

module.exports = { findOrder };
