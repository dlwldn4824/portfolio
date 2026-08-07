# HOPE 문제 검증 연구 (연구형)

> GitHub: [dlwldn4824/HOPE_organization](https://github.com/dlwldn4824/HOPE_organization)  
> 경로: `research/problem-validation/`  
> 본 연구는 **또박또박(HOPE)** 제품·수상(소원 H.O.P.E 창의보조공학 장려상 · HUSS AI 장려상)의 **문제 정의 근거**다.

---

## 카테고리
- **주 카테고리**: 연구 · 문제검증
- **부 카테고리**: AI · NLP, 전공 연계
- **연결 레포**: `dlwldn4824/HOPE_organization`
- **한 줄**: HOPE Pain TF-IDF/LDA 검증 파이프라인

---

## 수상과의 관계
- 또박또박이 받은 **소원 H.O.P.E 창의보조공학 경진대회 장려상**, **HUSS AI 경진대회 장려상**의 “왜 이 문제인가?”를 데이터로 받쳐 주는 연구 산출물이다.
- HUSS **로컬 임팩트** 표기는 사용하지 않는다.

## 왜 이 문제를 선택했는가
조음음운장애 아동 언어재활에서 ‘가정 피드백 공백’이 **감이 아니라 실제 Pain**인지 증명해야, 보조공학·HUSS 심사 모두에서 설득력이 생긴다.

## 실제 문제로 어떻게 검증했는가
공공데이터 → 현황 / 뉴스 → 사회 이슈 / 논문 → 학술 근거  
→ 텍스트마이닝(TF-IDF, LDA, Network) → 공통 키워드 → Pain → HOPE 기능 매핑

## 솔루션
재현 가능한 Python 파이프라인: 수집 → 전처리 → TF-IDF/LDA/네트워크 → 교차비교 → synthesis 리포트

## 효과 · 정량 지표
HUSS·보조공학 제안·심사의 문제 정의 근거. PPT용 figure/table 산출 (`outputs/`)

## 역할 · 역량 · 강점
- **역할**: 연구 설계·파이프라인
- **강점**: 문제 정의, 텍스트마이닝, 근거 기반 제품 기획

## 기술 스택
Python, KoNLPy, TF-IDF, LDA, NetworkX, matplotlib
