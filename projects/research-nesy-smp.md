# NeSy-SMP 논문 재현 (진행 중)

## 카테고리
- **주 카테고리**: 연구 · 논문 재현
- **부 카테고리**: Neuro-Symbolic · XAI · Healthcare ML
- **연결 레포**: `dlwldn4824/NeSy-SMP-repro`
- **한 줄**: Neuro-symbolic sepsis mortality prediction (NeSy-SMP) 재현·감사 · **진행 중**
- **상태**: 🔄 **In Progress** (독자 NeSy 신규 연구 아님 · 공개 논문/코드 재현·감사)

> GitHub: https://github.com/dlwldn4824/NeSy-SMP-repro  
> Upstream: [FabrizioDeSantis/NeSy-SMP](https://github.com/FabrizioDeSantis/NeSy-SMP)

## 왜 이 문제를 선택했는가
LLM·딥러닝만으로 부족한 **설명 가능성·지식 제약**을 Neuro-Symbolic 구조로 어떻게 붙이는지, 논문과 공개 코드의 간극을 직접 재현·감사하며 배우기 위해 선택했습니다.

## 실제 문제로 어떻게 검증하는가 (진행 중)
- MIMIC-IV 기반 sepsis mortality prediction 파이프라인 재현 체크리스트
- Phase-3 gate audit: weak anchoring, w_D/w_K, leakage, seeds, T1/T2
- 코드 라인 단위 grounding notes (`PHASE3_GROUNDING_AUDIT.md`)
- Knowledge pipeline (가이드라인 → KG/axiom) 복원 트랙과 baseline 재현 트랙 분리

## 솔루션 (작업 공간)
| Path | 내용 |
|------|------|
| `NeSy-SMP/` | Upstream + data-driven KG/axiom pipeline |
| `REPRODUCTION_CHECKLIST.md` | End-to-end 재현 체크리스트 |
| `PHASE3_GATE_DELIVERABLE.md` | Phase-3 gate audit |
| `MASTER_PLAN.md` | 재현 마스터 플랜 |
| `NeSy-SMP_Colab.ipynb` | Colab + Drive 스타터 |

※ MIMIC-IV / derived CSV는 레포에 포함하지 않음 (`.gitignore`).

## 역할 · 역량 · 강점
- **역할**: 개인 재현·감사·지식 파이프라인 실험
- **보여줄 수 있는 강점**: 논문↔코드 간극 감사, 재현 가능성, Neuro-Symbolic·룰/지식 grounding에 대한 Current Study
- **주의 표기**: 완료된 자체 연구 성과가 아니라 **진행 중 재현 워크스페이스**

## 기술 스택
Python · BiLSTM / LTN · Knowledge Graph · Colab · MIMIC-IV (로컬/Drive)
