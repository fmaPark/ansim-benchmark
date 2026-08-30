"""AUX-02 — 디버그 모드 활성 상태로 기동 (0259 §9.4)."""

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "ansim benchmark"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
