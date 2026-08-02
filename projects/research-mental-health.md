# Multi-Agent Mental Health Evaluation (연구형)

## 카테고리
- **주 카테고리**: 전공 과제
- **부 카테고리**: AI · NLP · Multi-Agent, 연구 · 평가
- **연결 레포**: `dlwldn4824/TM-MultiLayer-MentalHealth`, `yyeonseoo/TM`
- **한 줄**: 텍스트마이닝 · Single vs Multi-Agent+RAG

> GitHub: https://github.com/dlwldn4824/TM-MultiLayer-MentalHealth

## 왜 이 문제를 선택했는가
단일 LLM 상담 응답의 증상·위험·안전 추론 품질을 객관적으로 비교할 필요가 있어 선택

## 실제 문제로 어떻게 검증했는가
MentalChat16K 기반, BERTScore/ROUGE·Judge·ChromaDB 공식 KB(NIMH/WHO/NICE)

## 솔루션
Symptom→Risk→Safety→Consensus 다층 에이전트 + RAG 대비 Single LLM 벤치마크

## 효과 · 정량 지표
P/R/F1, high-risk recall, unsafe rate 등 실험 지표로 ‘안전한 AI’ 설계 근거 확보

## 역할 · 역량 · 강점
- **역할**: 연구용 평가 프레임 · RAG/Eval 파트
- **보여줄 수 있는 강점**: 연구 실험 설계, RAG, 안전성 평가, 멀티에이전트 오케스트레이션

## 기술 스택
Python, Ollama(qwen2.5:7b), ChromaDB, BERTScore/ROUGE
