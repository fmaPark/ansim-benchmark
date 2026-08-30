// P2(JS/TS) — 동의 처리 없이 개인정보 필드 수집 (0414 §7.3.2)
import express from "express";

const router = express.Router();

router.post("/signup", (req, res) => {
  const record = {
    email: req.body.email,
    phone: req.body.phone,
  };
  res.json(record);
});

export default router;
