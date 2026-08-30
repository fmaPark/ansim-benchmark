"""AUX-04 near-miss — 안전한 JSON 역직렬화."""

import json


def load_state(raw: bytes):
    return json.loads(raw.decode("utf-8"))
