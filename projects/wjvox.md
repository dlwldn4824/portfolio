# WJVOX (YourVoice)

## 카테고리
- **주 카테고리**: AI · 음성
- **부 카테고리**: Web · 풀스택, 인프라 · GPU
- **연결 레포**: `KWwoojin/project`
- **한 줄**: 음성 학습·infer·공유 (WJVOX)

> 음성 업로드→학습→공개 infer·공유 플랫폼  
> Tier **A** · GitHub: https://github.com/KWwoojin/project

## 왜 이 문제를 선택했는가
개인/권한 음성 기반 AI 보이스 생성·공유에서 운영·보안 경계가 실제 병목이라고 판단

## 실제 문제로 어떻게 검증했는가
Owner UI 체크포인트, API smoke, RunPod on-demand/GPU 문서화로 운영 검증

## 솔루션
Upload→Train→Publish→Infer. JWT vs WORKER_TOKEN, Cloudflare R2, RunPod GPU worker(RVC 등)

## 효과 · 정량 지표
실서비스 인프라 운영 경험. 3–6개월 운영비 약 100–200만 원 규모 체감(자소서)

## 역할 · 역량 · 강점
- **역할**: UI/UX·타이포·프론트 기여 (메인 커밋 협업)
- **보여줄 수 있는 강점**: 서비스 UX, 보안 경계, GPU 워커 운영 감각
- **비고**: accent #8E60F6, UNIVERSAL_UI 원칙 적용

## 기술 스택
Next.js, Supabase, Cloudflare R2, RunPod, Vercel, Gumi Romance+Pretendard
