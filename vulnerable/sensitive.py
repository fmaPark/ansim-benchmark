"""P3 — 민감정보를 별도 동의 없이 취급 (0414 §7.3.2)."""

def intake():
    return {
        "health_note": request.form["health_note"],
        "criminal_record": request.form["criminal_record"],
    }
