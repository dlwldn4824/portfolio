# Multi-Agent Mental Health Evaluation (연구형)

## 카테고리
- **주 카테고리**: 전공 과제
- **부 카테고리**: AI · NLP · Multi-Agent, 연구 · 평가
- **연결 레포**: `dlwldn4824/TM-MultiLayer-MentalHealth`, `yyeonseoo/TM`
- **한 줄**: 역할 기반 멀티에이전트·RAG·조건부 Safety Revision을 Single LLM과 비교·평가

> GitHub: https://github.com/dlwldn4824/TM-MultiLayer-MentalHealth

## 왜 이 문제를 선택했는가
정신건강은 고위험 도메인이다. 단일 LLM이 맥락·위험·생성·안전을 한 덩어리로 처리하면 **실패 지점을 찾지 못하고**, 최종 점수만 보는 평가는 **왜 틀렸는지**를 설명하지 못한다. 역할을 분리한 구조가 reliability·safety를 실제로 올리는지 검증하고자 했다.

## 실제 문제로 어떻게 검증했는가
- 데이터: CounselChat 등 상담 Q&A (연구 프로토타입, 임상 GT 아님)
- KB: NIMH / WHO 공식 문서 → ChromaDB RAG
- 모델: Ollama `qwen2.5:7b` 외 Phase 2에서 다모델 비교
- 지표: Faithfulness · Relevancy · Empathy · Safety (LLM Judge 0–5) + Runtime, BERTScore/ROUGE는 참고

## 솔루션
| 구조 | 흐름 |
|------|------|
| Single | Question → LLM → Response |
| Single + RAG | Retrieval → LLM |
| Two-Agent | Retriever → Reasoning → Response |
| **Three-Agent** | Retriever → Reasoning → **Safety** → Response |

최종: Gatekeeper가 문제일 때만 Revision하는 **Conditional Bidirectional**  
설계 원칙: *되돌릴 수 있는 곳엔 LLM, 되돌릴 수 없는 곳(사용자에게 나가는 위험 응답)엔 Safety Gate + Revision.*

## 효과 · 정량 지표
- Phase 1: Three-Agent Safety **4.83** · Empathy **4.31** (가장 효과, Runtime 72s)
- Phase 2: `qwen2.5:7b` + three_agent **score 69.40** · Multi-Agent Empathy/Safety↑ 경향
- Ablation: 핵심은 Agent 수가 아니라 **Safety Verification · Revision Layer**. RAG는 Faith/Safety↑·Empathy↓
- Conditional: Revision **~6%** 수준으로 Safety 유지·Runtime 절감 방향

## 역할 · 역량 · 강점
- **역할**: 파이프라인·RAG/Knowledge·평가 프레임 (팀: 이지우 / 전도윤 / 이준희 / 윤연서)
- **강점**: 에이전트를 모델 연결이 아니라 역할·도구·컨텍스트·평가가 정의된 시스템으로 설계

## 기술 스택
Python, Ollama(qwen2.5:7b), ChromaDB, NIMH/WHO KB, LLM Judge, BERTScore/ROUGE
