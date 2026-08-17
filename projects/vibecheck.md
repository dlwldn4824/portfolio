# VibeCheck (view_check)

## 카테고리
- **주 카테고리**: AI × 신뢰 · 보안
- **부 카테고리**: 해커톤 · 경진, Web · 풀스택
- **연결 레포**: `dlwldn4824/view_check`
- **한 줄**: 코덱스 커뮤니티 해커톤 본선 · 정책 기반 보안 검증 루프

> 바이브 코딩 앱을 배포 전에, 정책 기준으로 실제 요청을 보내고 증거를 모아 사람이 승인한 뒤 고치고, 같은 공격을 다시 검증하는 도구  
> Tier **S** · GitHub: https://github.com/dlwldn4824/view_check  
> Live: https://view-check-three.vercel.app/ · 시연: https://youtu.be/eyd36YSsI-U

## 한눈에 (문제 → AI → 결과)
| | |
|--|--|
| **문제** | 생성·배포 속도가 정책 기준 보안 검증·수정 증명을 앞지름 |
| **접근** | 정책 → HTTP 검증 → 규칙 판정 → 사람 승인 → Codex 수정 → Replay |
| **결과** | 코덱스 커뮤니티 해커톤 본선 |

## 왜 이 문제를 선택했는가
바이브 코딩으로 누구나 서비스를 만들 수 있게 됐지만, “안전한가요?”를 LLM에게 다시 묻는 방식만으로는 동일 공격이 실제로 막혔는지 증명하기 어렵다.

## 솔루션
정적 신호 → 실제 HTTP 증거 → Symbolic Engine 규칙 판정 → 사람 승인 → Codex 수정 → 동일 공격 Replay를 하나의 루프로 연결하는 Policy-Grounded Security Harness

## 역할 · 팀
- **팀**: 박지원 · 유성호 · 이보민 · 이지우
- **대회**: 코덱스 커뮤니티 해커톤 본선 (2026.08)

## 기술 스택
JavaScript · Vercel · Codex · 정책/규칙 기반 검증 루프
