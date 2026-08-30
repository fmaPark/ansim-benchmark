"""P5 — 공개 웹에서 개인정보를 수집하는 스크래핑 (0414 §7.3.2)."""

import requests
from bs4 import BeautifulSoup


def harvest(url: str):
    html = requests.get(url, timeout=10).text
    soup = BeautifulSoup(html, "html.parser")
    return {
        "이름": soup.select_one(".name").text,
        "phone": soup.select_one(".phone").text,
        "address": soup.select_one(".addr").text,
    }
