"""P5 — 공개 웹에서 개인정보를 수집하는 스크래핑 (0414 §7.3.2)."""


def harvest(url: str, http, parser):
    """http는 requests.get 호환, parser는 BeautifulSoup 호환 객체를 받는다."""
    html = http.get(url, timeout=10).text
    soup = parser(html, "html.parser")
    return {
        "이름": soup.select_one(".name").text,
        "phone": soup.select_one(".phone").text,
        "address": soup.select_one(".addr").text,
    }
