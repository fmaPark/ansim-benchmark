# ansim-benchmark — 안심코드 진단 룰 벤치마크

[안심코드(AnsimCode)](https://github.com/fmaPark/ansim-code) 진단 룰 31종의
검출률(TPR)·오탐률(FPR)을 재도록 **의도적으로 취약하게** 만든 저장소다.
실행 가능한 서비스가 아니며, 어떤 코드도 배포·실행 목적이 아니다.

> ⚠️ 여기 담긴 키·주민등록번호·계좌번호는 전부 **합성값**이다. 실제 자격증명이 아니다.

## 구조

| 경로 | 목적 |
| --- | --- |
| `vulnerable/` | 양성 세트 — 파일 하나에 취약점 하나(원칙). TTA 표준 조항의 의도에서 작성했다 |
| `clean/` | 오탐 측정 세트 — 취약 코드와 겉모습이 닮았지만 안전한 near-miss |
| `verification/expected_findings.yaml` | 오라클. 어떤 룰이 어느 파일에서 발화해야 하는지의 확정 목록 |

측정 스크립트(`measure_detection.py`·`check_invariants.py`)는 이 저장소가 아니라
**안심코드 저장소의 `verification/`** 에 있다. 스크립트가 품는 정규식 리터럴이
여기 있으면 저장소 전체 판정 룰(P8·P9·P10)을 스스로 무력화하기 때문이다.

## 취약점 의도 명세

근거 표준: TTAK.KO-11.0259(보안약점), TTAK.KO-12.0414(개인정보), TTAK.KO-11.0309(SBOM),
TTAK.KO-11.0322(공급망). 조항은 각 파일 상단 docstring에 적었다.

### 시크릿 (SEC-01~05)

| 파일 | 룰 | 심은 내용 |
| --- | --- | --- |
| `vulnerable/secrets_config.py` | SEC-01 · SEC-04 | 실형식 고엔트로피 토큰 + AWS 액세스 키 쌍 |
| `vulnerable/secrets.ts` | SEC-01 · SEC-04 | JS/TS 측 동일 유형 |
| `vulnerable/comment_leak.py` | SEC-02 | 주석에 남은 내부망 IP·구 자격증명 |
| `vulnerable/.env` | SEC-03 | 실형식 키를 담은 환경파일 커밋 |
| `vulnerable/pii_store.py` | SEC-05 | 체크섬을 통과하는 합성 주민등록번호 |
| `vulnerable/pii_edge.py` | SEC-05 | 체크섬 무효 주민번호·휴대전화·계좌 (확정 불가 → 검토 필요) |

### 개인정보 (P1~P10)

| 파일 | 룰 | 심은 내용 |
| --- | --- | --- |
| `vulnerable/pii_store.py` | P6 | 개인정보를 암호화·해시 없이 적재 |
| `vulnerable/admin_routes.py` · `admin.js` | P7 | 관리 라우트에 인증 부재 |
| (저장소 전체) | P8 | 주민번호를 다루면서 접근 기록 수단이 전무 |
| (저장소 전체) | P9 | 처리방침 파일·라우트가 전무 |
| `vulnerable/collect.py` · `collect.ts` | P2 | 동의 처리 없이 개인정보 수집 |
| `vulnerable/sensitive.py` | P3 | 민감정보를 별도 동의 없이 취급 |
| `vulnerable/crawler.py` | P5 | 공개 웹 스크래핑으로 개인정보 수집 |
| `vulnerable/models.py` | P10 | 개인정보 모델에 파기 경로 부재 |
| `vulnerable/overcollect.py` | P1 | 목적 대비 과도한 수집 필드 |
| `vulnerable/third_party.py` | P4 | 고지 없이 개인정보를 외부로 전송 |

### 보조 보안 (AUX-01~04)

| 파일 | 룰 | 심은 내용 |
| --- | --- | --- |
| `vulnerable/sql_injection.py` · `sqli.js` | AUX-01 | 문자열 조립 SQL |
| `vulnerable/app.py` | AUX-02 | 디버그 모드 활성 |
| `vulnerable/server.js` | AUX-03 | CORS 와일드카드 |
| `vulnerable/deserialize.py` | AUX-04 | 신뢰할 수 없는 입력 역직렬화 |

### 구성요소·공급망 (SCA-01~12)

`vulnerable/requirements.txt`·`package.json`·`package-lock.json`이 유발한다.
취약 버전 5핀(Django·requests·Flask·lodash·next), 미선언 import(redis·left-pad),
비레지스트리 출처, 버전 범위 선언, lock 불일치, 고지 없는 복제본(`vendor/oldlib/`).
앱이 실제로 쓰지 않는 의존성도 선언에 남겨 두었다 — 바이브코딩의 "남은 의존성" 실패 모드다.

## 저장소 전체 불변식

P8·P9·P10은 저장소 **전체**의 부재를 판정한다. 그래서 이 저장소의 모든 코드 파일은
아래를 지켜야 하며, 어기면 양성이 조용히 마스킹된다.

1. 로깅 라이브러리 반입 금지 (P8)
2. 처리방침 파일명·라우트 금지 (P9)
3. 파기 관련 동사 금지 (P10)
4. 모든 비표준 import는 매니페스트에 선언 (의도된 SCA-01 예외만 제외)
5. 개인정보 필드와 외부 전송 호출의 동시 등장은 `vulnerable/third_party.py`에서만 (P4)
6. 인증 단어는 `vulnerable/admin_routes.py`·`admin.js`에 금지, `clean/admin_ok.py`에는 필수 (P7)

이 불변식은 안심코드의 `verification/check_invariants.py`가 자동 검사하며,
`.github/workflows/invariants.yml`이 push마다 실행한다.

## 등급 시나리오 태그

| 태그 | 상태 | 기대 등급 |
| --- | --- | --- |
| `v1-danger` | 전체 | 위험 |
| `v2-warning` | 등급 상향을 막는 발견만 제거 | 주의 |
| `v3-safe` | 모든 확정 발견 제거 | 안심 (+ 검토 필요 n건) |

## 라이선스

이 저장소의 코드는 측정 목적의 합성 샘플이다. 자유롭게 복제·수정해도 되며,
어떤 보증도 하지 않는다.
