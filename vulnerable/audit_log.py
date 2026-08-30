"""P8 해소 — 개인정보 취급 이력을 남긴다 (0414 §7.3.4)."""

import logging

audit = logging.getLogger("ansim.audit")


def record(action: str, actor: str) -> None:
    audit.info("%s by %s", action, actor)
