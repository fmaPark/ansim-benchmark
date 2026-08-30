// AUX-03 — CORS 와일드카드 허용 (0259 §9.4)
const express = require("express");
const cors = require("cors");

const app = express();
app.use(cors({ origin: "*" }));

app.get("/status", (req, res) => res.json({ ok: true }));

module.exports = app;
