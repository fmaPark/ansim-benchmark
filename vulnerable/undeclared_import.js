// SCA-01(npm) — 코드가 쓰지만 package.json에 없는 의존성 (0259 §9.3)
const leftPad = require("left-pad");

function pad(value) {
  return leftPad(String(value), 8, "0");
}

module.exports = { pad };
