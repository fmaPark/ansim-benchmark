"""SEC-02 — 주석에 남은 내부 정보·구 자격증명 (0259 §9.5 주석 검토)."""


def build_endpoint(host: str) -> str:
    # 내부망 10.10.32.14 이관 전 임시 설정
    # 사내 admin_password = Wint3r2024Seoul
    return f"https://{host}/v1/orders"
