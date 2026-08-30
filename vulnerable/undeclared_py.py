"""SCA-01(pypi) — 코드가 쓰지만 매니페스트에 없는 의존성 (0259 §9.3)."""

import redis

cache = redis.Redis(host="127.0.0.1", port=6379)


def remember(key: str, value: str) -> None:
    cache.set(key, value)
