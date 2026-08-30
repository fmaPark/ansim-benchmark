"""AUX-04 — 신뢰할 수 없는 입력 역직렬화 (0259 §9.4)."""

import pickle

from flask import request


def load_state():
    return pickle.loads(request.data)
