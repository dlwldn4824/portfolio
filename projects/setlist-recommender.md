# Band Setlist Recommender

## 카테고리
- **주 카테고리**: 전공 과제
- **부 카테고리**: AI · 규칙기반 추천, Web · 배포
- **연결 레포**: `dlwldn4824/opensource_final`, `dlwldn4824/open-source-fastapi-docker`
- **한 줄**: 오픈소스실습 기말 · 552곡 셋리스트 추천

> 552곡 기반 커버곡·믹싱 방향 추천  
> Tier **A** · GitHub: https://github.com/dlwldn4824/opensource_final

## 왜 이 문제를 선택했는가
음역·세션·악기·분위기에 맞는 셋리스트·믹스 팁이 없어 리허설 비용이 큼

## 실제 문제로 어떻게 검증했는가
오픈소스 실습 기말 — Docker Compose·EC2 배포 체크리스트로 재현성 검증

## 솔루션
rule-based Top5 + 곡별 믹싱 가이드. Streamlit UI + FastAPI + Docker

## 효과 · 정량 지표
552곡 데이터셋. AWS EC2 배포 가능한 교육용 프로덕션 형태

## 역할 · 역량 · 강점
- **역할**: 개인 저장소 오너
- **보여줄 수 있는 강점**: 규칙 기반 추천, Docker/EC2, 도메인(밴드) 지식
- **비고**: 관련: open-source-fastapi-docker CRUD 실습

## 기술 스택
Streamlit, FastAPI, Docker Compose, AWS EC2
