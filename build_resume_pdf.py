#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""당근 톤 2단 이력서 PDF — 문제 해결 사고 중심 · 각 페이지 풀필."""

from pathlib import Path

from reportlab.lib.colors import HexColor, white, black
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

OUT = Path("/Users/LEEJIWOO/Desktop/대학교폴더/포트폴리오/이지우_이력서.pdf")
W, H = A4

# 당근 브랜드 톤
ORANGE = HexColor("#FF6F0F")
ORANGE_SOFT = HexColor("#FFF1E8")
INK = HexColor("#1A1A1A")
MUTED = HexColor("#6B6B6B")
LINE = HexColor("#E8E8E8")
GRAY_BOX = HexColor("#F5F5F5")
TAG_BG = HexColor("#F0F0F0")

FONT = "Pretendard"
FONT_B = "Pretendard-B"
REG = "/Users/LEEJIWOO/Library/Fonts/PretendardVariable.ttf"
pdfmetrics.registerFont(TTFont(FONT, REG))
pdfmetrics.registerFont(TTFont(FONT_B, REG))

MARGIN = 12 * mm
LEFT_W = 58 * mm
GAP = 5 * mm
RIGHT_X = MARGIN + LEFT_W + GAP
RIGHT_W = W - RIGHT_X - MARGIN
COL_BOT = 14 * mm


def wrap(c, text, font, size, max_w):
    lines, cur = [], ""
    for ch in text:
        t = cur + ch
        if c.stringWidth(t, font, size) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = ch
    if cur:
        lines.append(cur)
    return lines


def draw_text(c, text, x, y, size=8.5, bold=False, color=INK, max_w=None, leading=None):
    font = FONT_B if bold else FONT
    leading = leading or (size * 1.35)
    max_w = max_w or (W - x - MARGIN)
    for line in wrap(c, text, font, size, max_w):
        c.setFillColor(color)
        c.setFont(font, size)
        c.drawString(x, y, line)
        y -= leading
    return y


def bullet(c, text, x, y, size=8.2, max_w=None, leading=None):
    c.setFillColor(ORANGE)
    c.circle(x + 1.0 * mm, y + 1.0 * mm, 0.85 * mm, fill=1, stroke=0)
    return draw_text(c, text, x + 3.8 * mm, y, size=size, max_w=(max_w or 40 * mm) - 3.8 * mm, leading=leading or size * 1.32)


def hline(c, x, y, w):
    c.setStrokeColor(LINE)
    c.setLineWidth(0.6)
    c.line(x, y, x + w, y)


def section(c, title, x, y, w):
    c.setFillColor(INK)
    c.setFont(FONT_B, 10)
    c.drawString(x, y, title)
    hline(c, x, y - 1.8 * mm, w)
    return y - 6.2 * mm


def tag_row(c, tags, x, y, max_w):
    """Draw hashtag-like chips; return new y."""
    cx, cy = x, y
    pad_x, pad_y, gap, h = 2.2 * mm, 1.2 * mm, 1.5 * mm, 5.2 * mm
    size = 7
    for t in tags:
        tw = c.stringWidth(t, FONT, size) + pad_x * 2
        if cx + tw > x + max_w:
            cx = x
            cy -= h + gap
        c.setFillColor(TAG_BG)
        c.roundRect(cx, cy - pad_y, tw, h, 1.2 * mm, fill=1, stroke=0)
        c.setFillColor(MUTED)
        c.setFont(FONT, size)
        c.drawString(cx + pad_x, cy + 0.6 * mm, t)
        cx += tw + gap
    return cy - h - 1 * mm


def gray_box(c, x, y, w, h):
    c.setFillColor(GRAY_BOX)
    c.roundRect(x, y - h, w, h, 2 * mm, fill=1, stroke=0)


def build():
    c = canvas.Canvas(str(OUT), pagesize=A4)

    # ========== PAGE 1 ==========
    # Header bar
    hdr_h = 28 * mm
    c.setFillColor(ORANGE)
    c.rect(0, H - hdr_h, W, hdr_h, fill=1, stroke=0)

    # Monogram block (photo substitute)
    mono = 22 * mm
    mx, my = MARGIN, H - hdr_h - 6 * mm
    c.setFillColor(white)
    c.roundRect(mx, my, mono, mono, 2 * mm, fill=1, stroke=0)
    c.setFillColor(ORANGE)
    c.setFont(FONT_B, 16)
    c.drawCentredString(mx + mono / 2, my + 8 * mm, "LJW")
    c.setFont(FONT, 6.5)
    c.setFillColor(MUTED)
    c.drawCentredString(mx + mono / 2, my + 3.5 * mm, "Android · AI")

    # Name on orange
    c.setFillColor(white)
    c.setFont(FONT, 9)
    c.drawString(mx + mono + 5 * mm, H - 10 * mm, "Software Engineer, Android (인턴) 지원")
    c.setFont(FONT_B, 22)
    c.drawString(mx + mono + 5 * mm, H - 19 * mm, "이지우  Lee Ji-woo")

    # Contact strip under header
    y = H - hdr_h - 8 * mm
    c.setFillColor(MUTED)
    c.setFont(FONT, 7.5)
    contact = "dlwldn4824@naver.com   ·   github.com/dlwldn4824   ·   @due_study_archive   ·   광운대 정보융합학부 VT"
    c.drawString(mx + mono + 5 * mm, y + 2 * mm, contact)
    hline(c, MARGIN, y - 1 * mm, W - 2 * MARGIN)

    # --- LEFT COLUMN ---
    lx = MARGIN
    ly = y - 8 * mm

    ly = section(c, "자기소개", lx, ly, LEFT_W)
    ly = draw_text(
        c,
        "AI가 답을 던지는 데서 멈추지 않고, 왜 그 답이 필요한지·어디에 검증이 필요한지를 먼저 묻는 개발자입니다. Android·웹·서버·실기기를 넘나들며 문제를 닫힌 플랫폼이 아니라 워크플로로 풉니다.",
        lx, ly, size=7.8, max_w=LEFT_W, leading=10.2,
    )
    ly -= 3 * mm

    ly = section(c, "전문 분야", lx, ly, LEFT_W)
    ly = tag_row(
        c,
        ["#Kotlin관심", "#Android", "#WebView", "#Compose관심", "#TypeScript", "#React", "#Socket.IO", "#FastAPI", "#YOLO", "#RAG", "#TemiSDK", "#CI/CD"],
        lx, ly, LEFT_W,
    )
    ly -= 2 * mm
    for s in [
        "모바일·WebView Bridge · Temi SDK · Camera2",
        "실시간: Socket.IO · 서버·클라이언트 연결",
        "AI: 규칙 파이프라인 · RAG · Multi-Agent · HITL",
        "품질: 지표 기반 평가 · 재현 가능한 실험 설계",
    ]:
        ly = bullet(c, s, lx, ly, size=7.6, max_w=LEFT_W)
    ly -= 3 * mm

    ly = section(c, "기타 역량", lx, ly, LEFT_W)
    for s in [
        "문제 본질을 정의한 뒤 해결 방법을 끝까지 탐색",
        "AI 코딩 도구로 프로토타입→검증 루프를 빠르게 회전",
        "플랫폼 경계(앱·웹·서버·로봇)를 넘는 시스템 사고",
        "팀장·운영진·멘토로 커뮤니케이션·자기주도 실행",
    ]:
        ly = bullet(c, s, lx, ly, size=7.6, max_w=LEFT_W)
    ly -= 3 * mm

    ly = section(c, "학력", lx, ly, LEFT_W)
    c.setFillColor(INK)
    c.setFont(FONT_B, 8)
    c.drawString(lx, ly, "광운대학교 정보융합학부")
    ly -= 3.2 * mm
    c.setFont(FONT, 7.5)
    c.setFillColor(MUTED)
    c.drawString(lx, ly, "비주얼테크놀로지 · 2024.03~")
    ly -= 3.5 * mm
    ly = bullet(c, "GPA 4.32/4.5 · 환산 97.9 · 101학점", lx, ly, size=7.5, max_w=LEFT_W)
    ly = bullet(c, "만점 학기 2회 · 성적우수 장학 3회", lx, ly, size=7.5, max_w=LEFT_W)
    ly = bullet(c, "A+: ML·DB·텍마·HCI·자료구조·UX", lx, ly, size=7.5, max_w=LEFT_W)
    ly -= 3 * mm

    ly = section(c, "Research Interest", lx, ly, LEFT_W)
    c.setFillColor(ORANGE)
    c.setFont(FONT_B, 8)
    c.drawString(lx, ly, "Neuro-Symbolic AI · XAI")
    ly -= 3.5 * mm
    ly = draw_text(
        c,
        "논문·구조를 학습하는 Current Study 단계. LLM 결과를 규칙·검증·외부 지식으로 보완하는 패턴을 PinTime·HITL 서비스에 적용하는 방법을 탐색 중. (독자 NeSy 연구 구현 아님)",
        lx, ly, size=7.3, max_w=LEFT_W, leading=9.8, color=MUTED,
    )

    # Left column bottom fill — Daangn fit note
    if ly > COL_BOT + 28 * mm:
        ly = COL_BOT + 26 * mm
    box_h = ly - COL_BOT - 2 * mm
    if box_h > 18 * mm:
        gray_box(c, lx, ly + 2 * mm, LEFT_W, box_h)
        ty = ly - 2 * mm
        c.setFillColor(ORANGE)
        c.setFont(FONT_B, 7.5)
        c.drawString(lx + 2 * mm, ty, "왜 이 포지션인가")
        ty -= 3.5 * mm
        draw_text(
            c,
            "Android에만 가두지 않고 AI·웹·서버로 문제를 풀어온 경험과, 채팅·플랫폼·품질처럼 ‘기반’을 다루는 일에 맞닿아 있습니다. 작은 개선이 수많은 이웃 경험으로 이어진다는 책임감에 공감합니다.",
            lx + 2 * mm, ty, size=7, max_w=LEFT_W - 4 * mm, leading=9.2, color=INK,
        )

    # --- RIGHT COLUMN ---
    rx = RIGHT_X
    ry = y - 8 * mm

    ry = section(c, "문제 해결 방식", rx, ry, RIGHT_W)
    gray_box(c, rx, ry + 2 * mm, RIGHT_W, 28 * mm)
    ty = ry - 1 * mm
    for line in [
        "1. 답이 아니라 끊긴 지점을 정의한다 — 조율이 방마다 끊기면 모델이 아니라 워크플로를 고친다.",
        "2. 되돌릴 수 있는 곳은 AI, 없는 곳은 규칙·사람 — 탐지·선별은 AI, 확정·발송·철거는 결정론/HITL.",
        "3. 수치로 검증하고 다음 실험으로 넘긴다 — mAP·F1·현장 설문·Phase pruning으로 개선 루프를 돌린다.",
        "4. 플랫폼 경계를 넘는다 — WebView↔SDK↔Socket↔서버를 하나의 UX로 묶어 시스템이 되게 만든다.",
    ]:
        ty = draw_text(c, line, rx + 2.5 * mm, ty, size=7.6, max_w=RIGHT_W - 5 * mm, leading=10)
    ry = ry - 30 * mm

    ry = section(c, "RESEARCH  텍스트마이닝 멀티레이어 분석", rx, ry, RIGHT_W)
    c.setFillColor(MUTED)
    c.setFont(FONT, 7)
    c.drawRightString(W - MARGIN, ry + 6.2 * mm, "진행 중 · 수업 프로젝트")
    ry = draw_text(
        c,
        "단일 LLM이 한 번에 답하는 구조의 한계를 문제 삼아, 정신건강 상담 발화(MentalChat16K)를 Symptom→Risk→Safety→Consensus 계층과 RAG 근거로 분해·비교합니다.",
        rx, ry, size=7.8, max_w=RIGHT_W, leading=10.2,
    )
    for b in [
        "사고: ‘최종 문장’만 보지 않고 각 계층이 결과에 미치는 영향·unsafe rate를 지표로 본다.",
        "방법: Ollama(qwen2.5:7b) · ChromaDB · NIMH/WHO/NICE 공식 KB · Phase별 pruning.",
        "역할: RAG/Knowledge — 공식 KB 구축, 인덱싱, Retrieval 품질·파라미터 튜닝.",
        "연결: github.com/dlwldn4824/TM-MultiLayer-MentalHealth",
    ]:
        ry = bullet(c, b, rx, ry, size=7.6, max_w=RIGHT_W)
    ry -= 2.5 * mm

    ry = section(c, "PROJECTS  (문제 → 구조 → 검증)", rx, ry, RIGHT_W)

    # PinTime box
    ph = 32 * mm
    gray_box(c, rx, ry + 1 * mm, RIGHT_W, ph)
    c.setFillColor(ORANGE)
    c.setFont(FONT_B, 8.5)
    c.drawString(rx + 2.5 * mm, ry - 2 * mm, "PinTime  ·  AI 일정 조율 에이전트")
    c.setFillColor(MUTED)
    c.setFont(FONT, 6.5)
    c.drawRightString(W - MARGIN - 2 * mm, ry - 2 * mm, "배포 · React/TS")
    ty = ry - 6 * mm
    for b in [
        "문제: When2Meet식 ‘방마다 표 다시 채우기’로 조율·확정·캘린더가 끊김.",
        "해결: 규칙 파이프라인으로 대화→가능시간 연결→충돌 제거→확정 시 같은 저장소에 등록.",
        "검증: 동작하는 프론트 프로토타입 배포(pintime.vercel.app). LLM 없는 규칙·휴리스틱으로도 워크플로를 닫음.",
    ]:
        ty = bullet(c, b, rx + 1.5 * mm, ty, size=7.4, max_w=RIGHT_W - 3 * mm)
    ry = ry - ph - 2.5 * mm

    # Smart Icheon start on page1 if space
    ph2 = 32 * mm
    if ry - ph2 > COL_BOT:
        gray_box(c, rx, ry + 1 * mm, RIGHT_W, ph2)
        c.setFillColor(ORANGE)
        c.setFont(FONT_B, 8.5)
        c.drawString(rx + 2.5 * mm, ry - 2 * mm, "Smart Icheon Care  ·  도시관리 AI")
        c.setFillColor(MUTED)
        c.setFont(FONT, 6.5)
        c.drawRightString(W - MARGIN - 2 * mm, ry - 2 * mm, "CV · HITL · 대상")
        ty = ry - 6 * mm
        for b in [
            "문제: 불법 현수막을 픽셀만으로 단정할 라벨이 없고, 전수 순찰은 스케일이 안 됨.",
            "해결: YOLO 탐지→Risk→OCR→공무원 CONFIRMED. 되돌릴 수 없는 확정은 사람에게.",
            "검증: test F1 0.591 · mAP50 0.439 · 1,892장. 지능형 로봇 컨소시엄 대상.",
        ]:
            ty = bullet(c, b, rx + 1.5 * mm, ty, size=7.4, max_w=RIGHT_W - 3 * mm)
        ry = ry - ph2 - 2 * mm

    # footer
    c.setFillColor(MUTED)
    c.setFont(FONT, 7)
    c.drawString(MARGIN, 6 * mm, "이지우 · Software Engineer, Android (인턴) 지원")
    c.drawRightString(W - MARGIN, 6 * mm, "1 / 2")
    c.setFillColor(ORANGE)
    c.rect(0, 0, W, 2.2 * mm, fill=1, stroke=0)

    c.showPage()

    # ========== PAGE 2 ==========
    c.setFillColor(ORANGE)
    c.rect(0, H - 10 * mm, W, 10 * mm, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont(FONT_B, 11)
    c.drawString(MARGIN, H - 6.5 * mm, "이지우  ·  Projects & Impact")
    c.setFont(FONT, 8)
    c.drawRightString(W - MARGIN, H - 6.5 * mm, "플랫폼 경계를 넘는 구현")

    y = H - 16 * mm
    x = MARGIN
    full_w = W - 2 * MARGIN

    def project_block(title, meta, bullets, y):
        # dynamic height from bullet count
        h = 10 * mm + len(bullets) * 10.5 * mm
        gray_box(c, x, y + 1 * mm, full_w, h)
        c.setFillColor(ORANGE)
        c.rect(x, y - h + 1 * mm, 1.8 * mm, h, fill=1, stroke=0)
        c.setFillColor(INK)
        c.setFont(FONT_B, 9.5)
        c.drawString(x + 4 * mm, y - 2.5 * mm, title)
        c.setFillColor(MUTED)
        c.setFont(FONT, 7)
        c.drawRightString(W - MARGIN - 2 * mm, y - 2.5 * mm, meta)
        ty = y - 7.5 * mm
        for b in bullets:
            ty = bullet(c, b, x + 3 * mm, ty, size=7.8, max_w=full_w - 8 * mm, leading=10.2)
        return y - h - 3.2 * mm

    # Continue / restate Smart if needed, then Temi, Mobile Robot with problem framing
    y = section(c, "PROJECTS  (계속)", x, y, full_w)

    y = project_block(
        "Smart Icheon Care  —  도시관리 CV 대시보드",
        "github.com/dlwldn4824/smart_icheon_care",
        [
            "사고: ‘AI가 불법이라고 말하면 끝’이 아니라, 라벨 부재·행정 책임이라는 본질을 HITL로 풀어냄.",
            "구조: YOLO11s+ByteTrack → 공공데이터 Risk → 클릭 OCR → 공무원 CONFIRMED · VWorld GIS.",
            "지표: val mAP50 0.510 · test F1 0.591 / mAP50 0.439 · ~15.7 FPS · 지능형 로봇 컨소시엄 대상.",
            "연결: 앱·대시보드·CV API를 한 업무 흐름으로 — 제품팀이 쓸 수 있는 ‘기반’에 가깝게 설계.",
        ],
        y,
    )

    y = project_block(
        "Temi-Tell-Me  —  CO-SHOW 전시 도슨트 (HCI)",
        "github.com/dlwldn4824/TemiTellMe · HCI-UX",
        [
            "사고: 전시장에서 길·대기·콘텐츠가 흩어지면 로봇이 아니라 ‘연결 UX’가 문제.",
            "구조: React(Capacitor) → WebView JS Bridge → Temi SDK. 화면·기기·서버를 한 동선으로.",
            "검증: 실제 전시 환경 현장 설문 24명(+Pilot·Post). 기능 사용·만족·오류를 혼합연구로 수집.",
            "시사점: 다양한 디바이스·현장에서 버티는 UI와, SDK 브리지로 플랫폼을 넘는 구현 경험.",
        ],
        y,
    )

    y = project_block(
        "Mobile Robot  —  TEMI ↔ 모바일 실시간 시스템",
        "github.com/dlwldn4824/mobile_robot_temi · yyeonseoo/mobile-robot",
        [
            "사고: REST만으로는 이동·촬영의 즉시성을 못 담는다 → Socket.IO로 명령을 ‘지금’ 잇는다.",
            "Camera2: Temi Android 키오스크 포토부스 → 업로드·갤러리 반영.",
            "Socket.IO: 모바일 ⇄ 중계 ⇄ Temi App (goto/stop/photo). WebView+TemiBridge+Spring Boot.",
            "품질 관점: 모듈이 각각 동작해도 시스템으로 안 이어지면 UX는 미완 — Observability 전에 ‘연결’을 닫음.",
        ],
        y,
    )

    y = project_block(
        "PinTime  —  AI 일정 조율 (요약)",
        "pintime.vercel.app · github.com/dlwldn4824/pintime",
        [
            "AI 코딩·규칙 파이프라인으로 0→배포까지 스스로 검증. LLM 없이도 ‘확정=캘린더’ 제약을 제품에 녹임.",
            "온디바이스/로컬 규칙 + 휴리스틱 점수 — 클라우드 LLM 의존 없이 프로토타입을 운영 가능한 형태로.",
            "Additional: 답변등기(KB, 승인·봉인 결정론) · iM Ready · WJVOX → github.com/dlwldn4824/portfolio",
        ],
        y,
    )

    # Awards dense
    y = section(c, "수상 · 활동 · 교육", x, y, full_w)
    gray_box(c, x, y + 1 * mm, full_w, 26 * mm)
    ty = y - 2.5 * mm
    c.setFillColor(INK)
    c.setFont(FONT_B, 8)
    c.drawString(x + 2.5 * mm, ty, "수상")
    ty -= 3.6 * mm
    ty = draw_text(
        c,
        "2026 보조공학·HUSS AI 장려(HOPE 팀장) · 지능형 로봇 컨소시엄 대상(Smart Icheon) · 2025 매치업 우수 · 마이크로모듈 SS · Dean's List · 창업동아리 장려 · 성적우수 장학 3회",
        x + 2.5 * mm, ty, size=7.3, max_w=full_w - 5 * mm, leading=9.3,
    )
    c.setFont(FONT_B, 8)
    c.setFillColor(INK)
    c.drawString(x + 2.5 * mm, ty, "활동 / 교육")
    ty -= 3.6 * mm
    ty = draw_text(
        c,
        "LG AIMERS 9기 · 대학혁신 서포터즈 · HOPE·환불원정대 팀장 · 노을 운영진(예약 웹) · KT 랜선나눔캠퍼스 중3 AI·ML · 에듀탑·학원 조교·과외",
        x + 2.5 * mm, ty, size=7.3, max_w=full_w - 5 * mm, leading=9.3,
    )
    y = y - 28 * mm

    # JD mapping
    y = section(c, "공고와의 접점", x, y, full_w)
    rows = [
        ("AI로 문제 해결", "규칙 에이전트·RAG·HITL — Android에 가두지 않고 효과적 수단을 고름"),
        ("기반·품질", "Socket·Bridge/SDK·지표 검증 — 연결을 닫은 뒤 개선 루프"),
        ("빠른 실험", "AI 코딩으로 0→배포 · 실사용 웹 운영(밴드 예약 등)"),
        ("디바이스 UX", "Temi WebView·Camera2·현장 UI — Compose/Android로 확장할 기반"),
    ]
    box_h = 5 * mm + len(rows) * 7.8 * mm
    gray_box(c, x, y + 1 * mm, full_w, box_h)
    ty = y - 2.2 * mm
    for label, desc in rows:
        c.setFillColor(ORANGE)
        c.setFont(FONT_B, 7.5)
        c.drawString(x + 2.5 * mm, ty, label)
        lw = c.stringWidth(label, FONT_B, 7.5) + 2.5 * mm
        c.setFillColor(INK)
        c.setFont(FONT, 7.3)
        c.drawString(x + 2.5 * mm + lw, ty, desc)
        ty -= 7.5 * mm
    y = y - box_h - 3 * mm

    # Closing — fill remaining
    y = section(c, "지원 동기 — 사고의 접점", x, y, full_w)
    remain = y - (COL_BOT + 1 * mm)
    box_h = max(remain, 32 * mm)
    gray_box(c, x, y + 1 * mm, full_w, box_h)
    c.setFillColor(ORANGE)
    c.rect(x, y - box_h + 1 * mm, 1.8 * mm, box_h, fill=1, stroke=0)
    ty = y - 3.5 * mm
    for line in [
        "당근 Android 챕터·모바일실이 말하는 '플랫폼에 사고를 가두지 않기'는, 제가 Temi·WebView·Socket·CV 대시보드에서 이미 해 온 방식입니다.",
        "AI로 문제를 풀되 신뢰·확장 가능한 구조(규칙·HITL·지표)를 같이 설계하는 일에 책임감이 있습니다. 채팅·클라이언트 플랫폼·Observability처럼 기반을 다루는 일에서, 작은 개선이 수많은 이웃 경험으로 이어진다는 점에 맞춰 일하겠습니다.",
        "Kotlin·Compose는 챕터에서 깊게 쌓되, 이미 가진 '경계를 넘는 문제 정의·빠른 실험·검증'을 인턴십에서 바로 쓰겠습니다.",
        "",
        "한 줄: AI 서비스를 빠르게 구현하면서, 텍스트 분석과 NeSy 학습으로 AI의 판단 구조까지 깊게 고민하는 개발자.",
    ]:
        if not line:
            ty -= 2.5 * mm
            continue
        ty = draw_text(c, line, x + 4 * mm, ty, size=7.9, max_w=full_w - 8 * mm, leading=10.4)

    c.setFillColor(MUTED)
    c.setFont(FONT, 7)
    c.drawString(MARGIN, 6 * mm, "이지우 · dlwldn4824@naver.com · github.com/dlwldn4824")
    c.drawRightString(W - MARGIN, 6 * mm, "2 / 2")
    c.setFillColor(ORANGE)
    c.rect(0, 0, W, 2.2 * mm, fill=1, stroke=0)


    c.save()
    print("Wrote", OUT)


if __name__ == "__main__":
    build()
