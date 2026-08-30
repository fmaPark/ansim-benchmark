// P7 — 관리자 라우트에 인증 미들웨어 부재 (0414 §7.3.4)
const express = require("express");

const app = express();

app.get("/admin", (req, res) => {
  res.json([{ id: 1, nickname: "hong" }]);
});

module.exports = app;
