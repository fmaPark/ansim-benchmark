"""SCA-06 — 저장소에 복제됐지만 LICENSE·COPYING 고지가 없는 컴포넌트 (0309 §6.8·§6.9)."""


def slugify(value: str) -> str:
    return "-".join(value.lower().split())
