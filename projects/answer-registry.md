# 답변등기 (KB AI Challenge)

## 카테고리
- **주 카테고리**: AI × 신뢰 · 금융
- **부 카테고리**: 해커톤 · 경진, Web · 풀스택
- **연결 레포**: `dlwldn4824/kb_AI_challenge`
- **한 줄**: KB AI Challenge · 답변 승인·봉인·발송

> 은행 AI 상담 초안 문장단위 승인·봉인·발송 콘솔  
> Tier **S** · GitHub: https://github.com/dlwldn4824/kb_AI_challenge

## 왜 이 문제를 선택했는가
AI 초안 위험 vs 전건 사람승인 부담. ‘승인≠발송’ 사고 위험을 구조적으로 막아야 한다고 판단

## 실제 문제로 어떻게 검증했는가
합성 240건 / 실상담 AI Hub 표본 / vitest 불변조건 60건

## 솔루션
위험큐(1,248→깊게 볼 39건) + 정본대조 + 사유정합 + SHA256 digest/HMAC 봉인 + 등기 타임라인. 원칙: 되돌릴 수 있는 곳엔 AI, 없는 곳엔 결정론

## 효과 · 정량 지표
게이트 차단·재생 100%. 큐 3.1%(39/1248). 합성 Recall@39 81.3%→실상담 25.0%(정직하게 격차 공개)

## 역할 · 역량 · 강점
- **역할**: 팀 삼삼오오 — UI/디자인 폴리시·구현
- **보여줄 수 있는 강점**: 신뢰성 엔지니어링, 브랜드 UI, 평가 정직성, WebCrypto
- **비고**: 데모 https://dlwldn4824.github.io/kb_AI_challenge/

## 기술 스택
Next.js, Vitest, WebCrypto, KB Yellow #FFCC00, Pretendard, GFC Red Spirit
