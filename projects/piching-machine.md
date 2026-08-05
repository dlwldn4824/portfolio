# piching_machine — LG Aimers 9기 (진행 중)

## 카테고리
- **주 카테고리**: 교육 · 챌린지 · ML
- **부 카테고리**: Tabular ML · Feature Engineering · 실험 관리
- **연결 레포**: `dlwldn4824/piching_machine`
- **한 줄**: LG Aimers 9기 Phase2 · 투구 제구 성공 확률 예측 · **진행 중**
- **상태**: 🔄 **In Progress**

> GitHub: https://github.com/dlwldn4824/piching_machine

## 왜 이 문제를 선택했는가
LG Aimers 9기 Phase2 과제. Trackman 등 투구 데이터를 바탕으로 **제구 성공 확률**을 예측하며, 피처 가설 → 실험 → holdout 지표로 모델·피처를 고르는 루프를 연습합니다.

## 실제 문제로 어떻게 검증하는가
- 로컬 2024 holdout **BSS**로 실험 비교 (챔피언 E20 ≈ **644.04**, E2 CatBoost 633.80 대비 개선)
- `experiments/` 로그·리포트·슬라이드로 실험 이력 관리
- `submit/` 패키지로 평가 서버 제출 형식 맞춤 (catboost 중심)

## 솔루션 (진행 중)
| 구성 | 내용 |
|------|------|
| **E20 챔피언** | Form(컨디션) / Intent(의도) / Exec(실행) / Clutch(긴장) 피처 + CatBoost |
| 파이프라인 | `run_e20_intent_pipeline.py` · `run_all_experiments.py` |
| 분석 | Streamlit `analysis_app.py` (리더보드·투구 상황 카드) |
| 제출 | `submit.zip` = `script.py` + `model/` + `requirements.txt` |

※ 공식 `data/` CSV는 git에 포함하지 않음.

## 역할 · 역량 · 강점
- **역할**: Aimers 개인/과제 실험·제출 코드
- **강점**: 도메인 피처 분해(Form/Intent/Exec/Clutch), 실험 리더보드, 제출 파이프라인 동결

## 기술 스택
Python · CatBoost · pandas/sklearn · Streamlit · Trackman 피처
