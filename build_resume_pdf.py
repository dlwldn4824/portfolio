#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2-page A4 resume PDF for 이지우."""

from pathlib import Path

from reportlab.lib.colors import Color, HexColor
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

OUT = Path("/Users/LEEJIWOO/Desktop/대학교폴더/포트폴리오/이지우_이력서.pdf")
W, H = A4

INK = HexColor("#26282C")
MUTED = HexColor("#5C636B")
ACCENT = HexColor("#0D9488")
LINE = HexColor("#D8DEE4")
BG_SOFT = HexColor("#F5F6F4")

FONT_REG = "Pretendard"
FONT_BOLD = "Pretendard-Bold"

# reportlab needs TrueType (not CFF/OTF PostScript outlines)
REG_PATH = "/Users/LEEJIWOO/Library/Fonts/PretendardVariable.ttf"
pdfmetrics.registerFont(TTFont(FONT_REG, REG_PATH))
# Variable font as bold fallback (weight simulated via same face + size)
pdfmetrics.registerFont(TTFont(FONT_BOLD, REG_PATH))


def draw_header_bar(c: canvas.Canvas):
    c.setFillColor(ACCENT)
    c.rect(0, H - 3.5 * mm, W, 3.5 * mm, fill=1, stroke=0)


def draw_footer(c: canvas.Canvas, page: int):
    c.setStrokeColor(LINE)
    c.setLineWidth(0.4)
    y = 12 * mm
    c.line(18 * mm, y + 4 * mm, W - 18 * mm, y + 4 * mm)
    c.setFillColor(MUTED)
    c.setFont(FONT_REG, 8)
    c.drawString(18 * mm, y, "이지우 · dlwldn4824 · github.com/dlwldn4824")
    c.drawRightString(W - 18 * mm, y, f"{page} / 2")


def section_title(c: canvas.Canvas, text: str, x: float, y: float) -> float:
    c.setFillColor(ACCENT)
    c.rect(x, y - 1.2 * mm, 2.2 * mm, 4.2 * mm, fill=1, stroke=0)
    c.setFillColor(INK)
    c.setFont(FONT_BOLD, 11)
    c.drawString(x + 4.5 * mm, y, text)
    c.setStrokeColor(LINE)
    c.setLineWidth(0.5)
    c.line(x + 4.5 * mm, y - 2.2 * mm, W - 18 * mm, y - 2.2 * mm)
    return y - 7 * mm


def body(c: canvas.Canvas, text: str, x: float, y: float, size=9.2, color=INK, leading=3.6 * mm, max_width=None) -> float:
    c.setFillColor(color)
    c.setFont(FONT_REG, size)
    max_w = max_width or (W - x - 18 * mm)
    # simple wrap
    words = text
    # character wrap for Korean
    line = ""
    for ch in words:
        test = line + ch
        if c.stringWidth(test, FONT_REG, size) <= max_w:
            line = test
        else:
            c.drawString(x, y, line)
            y -= leading
            line = ch
    if line:
        c.drawString(x, y, line)
        y -= leading
    return y


def bullet(c: canvas.Canvas, text: str, x: float, y: float, size=9, leading=3.55 * mm, max_width=None) -> float:
    c.setFillColor(ACCENT)
    c.circle(x + 1.1 * mm, y + 1.1 * mm, 0.7 * mm, fill=1, stroke=0)
    return body(c, text, x + 4 * mm, y, size=size, leading=leading, max_width=(max_width or (W - x - 22 * mm)) - 4 * mm)


def job_header(c, title, meta, x, y):
    c.setFillColor(INK)
    c.setFont(FONT_BOLD, 10)
    c.drawString(x, y, title)
    c.setFont(FONT_REG, 8)
    c.setFillColor(MUTED)
    c.drawRightString(W - 18 * mm, y, meta)
    return y - 4.2 * mm


def build():
    c = canvas.Canvas(str(OUT), pagesize=A4)
    x = 18 * mm
    content_w = W - 36 * mm

    # ========== PAGE 1 ==========
    draw_header_bar(c)

    # Name
    y = H - 16 * mm
    c.setFillColor(INK)
    c.setFont(FONT_BOLD, 20)
    c.drawString(x, y, "이지우  Lee Ji-woo")
    y -= 5.5 * mm
    c.setFont(FONT_REG, 8.5)
    c.setFillColor(MUTED)
    c.drawString(x, y, "dlwldn4824@naver.com  ·  github.com/dlwldn4824  ·  @due_study_archive")
    y -= 4 * mm
    c.drawString(x, y, "광운대학교 정보융합학부 비주얼테크놀로지전공  ·  입학 2024.03")

    # One-line intro box
    y -= 8 * mm
    box_h = 28 * mm
    c.setFillColor(BG_SOFT)
    c.roundRect(x, y - box_h + 4 * mm, content_w, box_h, 2 * mm, fill=1, stroke=0)
    c.setFillColor(ACCENT)
    c.rect(x, y - box_h + 4 * mm, 1.6 * mm, box_h, fill=1, stroke=0)
    ty = y - 1 * mm
    ty = body(
        c,
        "AI가 답변을 생성하는 데서 멈추지 않고, 사용자의 실제 행동과 업무로 이어지는 서비스를 만드는 개발자입니다.",
        x + 4 * mm,
        ty,
        size=9,
        max_width=content_w - 8 * mm,
        leading=3.5 * mm,
    )
    ty = body(
        c,
        "일정 조율 에이전트, 도시관리 AI, 전시 안내 로봇을 구현하며 AI·웹·서버·실기기를 하나의 워크플로로 연결했습니다.",
        x + 4 * mm,
        ty,
        size=9,
        max_width=content_w - 8 * mm,
        leading=3.5 * mm,
    )
    ty = body(
        c,
        "현재는 텍스트마이닝 멀티레이어 분석을 연구하고, Neuro-Symbolic AI를 학습하며 AI 결과를 규칙과 검증으로 보완하는 방법을 탐구하고 있습니다.",
        x + 4 * mm,
        ty,
        size=9,
        max_width=content_w - 8 * mm,
        leading=3.5 * mm,
    )
    y = y - box_h - 2 * mm

    # Skills
    y = section_title(c, "핵심 기술", x, y)
    y = bullet(c, "Frontend  React · Next.js · TypeScript · Vite · Tailwind", x, y)
    y = bullet(c, "Backend / Infra  Node · FastAPI · Spring Boot · Docker · Socket.IO · Vercel", x, y)
    y = bullet(c, "AI / Data  YOLO · RAG · Multi-Agent · Ollama · 텍스트마이닝 · 규칙·검증 파이프라인", x, y)
    y = bullet(c, "Robot / Device  Temi SDK · WebView Bridge · Camera2 · Android", x, y)
    y -= 1.5 * mm

    # Education
    y = section_title(c, "학력 · 성적", x, y)
    y = job_header(c, "광운대학교 정보융합학부 비주얼테크놀로지전공", "2024.03 ~ 재학", x, y)
    y = bullet(c, "누적 GPA 4.32 / 4.5 (환산 97.9) · 취득 101학점 · 만점 학기 2회 (24-2, 26-1)", x, y)
    y = bullet(c, "강점 과목 A+: 기계학습 · DB · 텍스트마이닝 · 자료구조 · OOP · 빅데이터프로그래밍 · UX/UI · HCI", x, y)
    y = bullet(c, "성적우수 장학금 2024.09 · 2025.06 · 2025.12", x, y)
    y -= 1.5 * mm

    # Research
    y = section_title(c, "RESEARCH", x, y)
    y = job_header(
        c,
        "텍스트마이닝 기반 멀티레이어 분석 연구",
        "진행 중 · 광운대 정보융합학부 · 수업 프로젝트",
        x,
        y,
    )
    y = bullet(
        c,
        "대상: MentalChat16K 사용자 발화. 단일 분류가 아니라 Symptom → Risk → Safety → Consensus 계층과 RAG 근거를 함께 분석.",
        x,
        y,
    )
    y = bullet(
        c,
        "파이프라인: 전처리 · Ollama(qwen2.5:7b) · ChromaDB RAG(NIMH/WHO/NICE 공식 KB) · Phase별 pruning 실험.",
        x,
        y,
    )
    y = bullet(
        c,
        "담당: RAG/Knowledge — 공식 KB 구축, ChromaDB 인덱싱, Retrieval 품질·파라미터 튜닝 (팀 가이드 기준).",
        x,
        y,
    )
    y = bullet(
        c,
        "평가 방향: high-risk recall ↑ · unsafe rate ↓ · symptom F1. 최종 예측뿐 아니라 계층별 영향·해석 가능성을 확인.",
        x,
        y,
    )
    y = body(c, "GitHub  github.com/dlwldn4824/TM-MultiLayer-MentalHealth", x + 4 * mm, y, size=8, color=MUTED)
    y -= 2 * mm

    # NeSy
    y = section_title(c, "Research Interest  ·  Current Study", x, y)
    c.setFillColor(INK)
    c.setFont(FONT_BOLD, 10)
    c.drawString(x, y, "Neuro-Symbolic AI  ·  Explainable AI")
    y -= 4.5 * mm
    y = bullet(
        c,
        "신경망의 패턴 학습과 기호 기반 규칙·추론을 결합하는 Neuro-Symbolic 구조와 관련 논문을 학습 중.",
        x,
        y,
    )
    y = bullet(
        c,
        "LLM 결과를 그대로 쓰지 않고 외부 지식·명시적 규칙·검증 단계를 붙여 신뢰도를 높이는 구조에 관심.",
        x,
        y,
    )
    y = bullet(
        c,
        "적용 탐색: PinTime(일정 제약·확정 검증), 답변등기(승인·봉인 결정론), 상담/도시관리처럼 되돌릴 수 없는 판단이 있는 서비스.",
        x,
        y,
    )
    y -= 1 * mm
    c.setFillColor(MUTED)
    c.setFont(FONT_REG, 7.5)
    c.drawString(x, y, "※ 논문 학습·구조 탐색 단계이며, NeSy를 독자 연구·구현했다고 표기하지 않습니다. (Research Interest / Current Study)")

    draw_footer(c, 1)
    c.showPage()

    # ========== PAGE 2 ==========
    draw_header_bar(c)
    y = H - 14 * mm
    y = section_title(c, "PROJECTS", x, y)

    # PinTime
    y = job_header(c, "PinTime — AI 일정 조율 에이전트", "Web · 배포  ·  github.com/dlwldn4824/pintime", x, y)
    y = bullet(c, "문제: When2Meet식 방마다 표를 다시 채우고, 확정 후에도 캘린더에 따로 넣는 끊긴 조율 흐름.", x, y)
    y = bullet(c, "구조: 대화 이해(규칙 파이프라인) → 가능 시간 연결·충돌 제거 → 추천·확정 → 동일 저장소에 캘린더 등록.", x, y)
    y = bullet(c, "배포: Vite·React19·TS·Tailwind4 프론트 프로토타입 · Vercel 라이브 (pintime.vercel.app).", x, y)
    y -= 2 * mm

    # Smart Icheon
    y = job_header(c, "Smart Icheon Care — 도시관리 AI 대시보드", "AI·CV · 대상  ·  github.com/dlwldn4824/smart_icheon_care", x, y)
    y = bullet(c, "파이프라인: YOLO11s 현수막 탐지 → Risk → 클릭 OCR 내용검사 → 공무원 CONFIRMED (Human-in-the-loop).", x, y)
    y = bullet(c, "평가: val mAP50 0.510 · test F1 0.591 / mAP50 0.439 · ~15.7 FPS · 공통테스트 1,892장.", x, y)
    y = bullet(c, "업무 연결: VWorld GIS·주차·시민신고 UI로 ‘민원 후 전수 순찰’을 AI 선별→사람 확정으로 재구성. 컨소시엄 대상.", x, y)
    y -= 2 * mm

    # Temi-Tell-Me
    y = job_header(c, "Temi-Tell-Me — 전시 도슨트 웹 (CO-SHOW 2025)", "HCI · WebView  ·  github.com/dlwldn4824/TemiTellMe", x, y)
    y = bullet(c, "WebView Bridge: React(Capacitor) → JS Bridge → Temi SDK로 실기기 도슨트 시나리오 연결.", x, y)
    y = bullet(c, "Temi SDK 연동으로 전시 안내·촬영·문의 등 현장 동선을 하나의 UX로 묶음.", x, y)
    y = bullet(c, "평가: 현장 설문 24명(+ Pilot·Post) 혼합연구로 기능 사용·만족·오류 수집.", x, y)
    y -= 2 * mm

    # Mobile Robot
    y = job_header(
        c,
        "Mobile Robot — TEMI ↔ 모바일 실시간 연결",
        "로봇 · 전공  ·  github.com/dlwldn4824/mobile_robot_temi",
        x,
        y,
    )
    y = bullet(c, "Camera2: Temi Android 키오스크에서 포토부스 촬영 → 앱·프로필 갤러리 반영.", x, y)
    y = bullet(c, "Socket.IO: 모바일 ⇄ 중계 서버 ⇄ Temi App으로 goto/stop/photo 등 즉시 명령.", x, y)
    y = bullet(c, "Android/서버: WebView+TemiBridge + Spring Boot REST + Socket 서버로 시스템 단위 UX 완성.", x, y)
    y -= 2.5 * mm

    # Additional
    c.setFillColor(MUTED)
    c.setFont(FONT_REG, 8)
    c.drawString(x, y, "Additional  답변등기(KB) · WJVOX · iM Ready  →  github.com/dlwldn4824/portfolio")
    y -= 6 * mm

    # Awards & Activities
    y = section_title(c, "수상 · 활동", x, y)
    y = bullet(c, "수상: 보조공학 장려상 · HUSS AI 장려상 · 지능형 로봇 컨소시엄 대상 · 매치업 우수 · 마이크로모듈 SS · Dean’s List", x, y, size=8.5)
    y = bullet(c, "활동: LG AIMERS 9기 · 대학혁신 서포터즈 · 노을 밴드 동아리 운영진 · HOPE/환불원정대 팀장", x, y, size=8.5)
    y = bullet(
        c,
        "교육: KT 랜선나눔캠퍼스 중3 AI·ML (26.07–09) · 에듀탑 수학 · 월계 채움학원 조교 · 개인 과외",
        x,
        y,
        size=8.5,
    )
    y -= 3 * mm

    c.setFillColor(BG_SOFT)
    c.roundRect(x, y - 14 * mm, content_w, 16 * mm, 2 * mm, fill=1, stroke=0)
    c.setFillColor(INK)
    c.setFont(FONT_BOLD, 8.5)
    c.drawString(x + 3 * mm, y - 2 * mm, "한 줄 캐릭터")
    body(
        c,
        "AI 서비스를 빠르게 구현할 수 있으면서, 텍스트 분석과 NeSy를 통해 AI의 판단 구조까지 깊게 고민하는 개발자.",
        x + 3 * mm,
        y - 6.5 * mm,
        size=9,
        max_width=content_w - 6 * mm,
    )

    draw_footer(c, 2)
    c.save()
    print("Wrote", OUT)


if __name__ == "__main__":
    build()
