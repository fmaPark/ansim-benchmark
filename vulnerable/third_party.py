"""P4 — 제3자 제공·위탁 고지 없이 개인정보를 외부로 전송 (0414 §7.3.3)."""

PARTNER_ENDPOINT = "https://partner.invalid/v1/leads"


def forward(member):
    payload = {
        "phone": member["phone"],
        "email": member["email"],
        "address": member["address"],
    }
    return requests.post(PARTNER_ENDPOINT, json=payload, timeout=10).status_code
