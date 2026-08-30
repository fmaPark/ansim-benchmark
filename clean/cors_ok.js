// AUX-03 near-miss — 특정 출처만 허용하는 CORS 설정
const express = require("express");
const cors = require("cors");

const app = express();
app.use(cors({ origin: ["https://bench.invalid"] }));

module.exports = app;
