#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""당근 Local Jobs 인턴용 이력서 PDF — README 정합 · 에이전트·Eval·업무흐름."""

from pathlib import Path

from reportlab.lib.colors import HexColor, white
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

OUT = Path("/Users/LEEJIWOO/Desktop/대학교폴더/포트폴리오/이지우_이력서_로컬잡스.pdf")
W, H = A4

ORANGE = HexColor("#FF6F0F")
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

MARGIN = 11 * mm
LEFT_W = 56 * mm
GAP = 4.5 * mm
RIGHT_X = MARGIN + LEFT_W + GAP
RIGHT_W = W - RIGHT_X - MARGIN
COL_BOT = 13 * mm


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
    leading = leading or (size * 1.32)
    max_w = max_w or (W - x - MARGIN)
    for line in wrap(c, text, font, size, max_w):
        c.setFillColor(color)
        c.setFont(font, size)
        c.drawString(x, y, line)
        y -= leading
    return y


def bullet(c, text, x, y, size=8.0, max_w=None, leading=None):
    c.setFillColor(ORANGE)
    c.circle(x + 1.0 * mm, y + 1.0 * mm, 0.8 * mm, fill=1, stroke=0)
    return draw_text(
        c, text, x + 3.6 * mm, y, size=size,
        max_w=(max_w or 40 * mm) - 3.6 * mm,
        leading=leading or size * 1.28,
    )


def hline(c, x, y, w):
    c.setStrokeColor(LINE)
    c.setLineWidth(0.55)
    c.line(x, y, x + w, y)


def section(c, title, x, y, w):
    c.setFillColor(INK)
    c.setFont(FONT_B, 9.5)
    c.drawString(x, y, title)
    hline(c, x, y - 1.6 * mm, w)
    return y - 5.6 * mm


def tag_row(c, tags, x, y, max_w):
    cx, cy = x, y
    pad_x, pad_y, gap, h = 2.0 * mm, 1.0 * mm, 1.3 * mm, 4.8 * mm
    size = 6.6
    for t in tags:
        tw = c.stringWidth(t, FONT, size) + pad_x * 2
        if cx + tw > x + max_w:
            cx = x
            cy -= h + gap
        c.setFillColor(TAG_BG)
        c.roundRect(cx, cy - pad_y, tw, h, 1.1 * mm, fill=1, stroke=0)
        c.setFillColor(MUTED)
        c.setFont(FONT, size)
        c.drawString(cx + pad_x, cy + 0.5 * mm, t)
        cx += tw + gap
    return cy - h - 0.8 * mm


def gray_box(c, x, y, w, h):
    c.setFillColor(GRAY_BOX)
    c.roundRect(x, y - h, w, h, 1.8 * mm, fill=1, stroke=0)


def build():
    c = canvas.Canvas(str(OUT), pagesize=A4)

    # ========== PAGE 1 ==========
    hdr_h = 26 * mm
    c.setFillColor(ORANGE)
    c.rect(0, H - hdr_h, W, hdr_h, fill=1, stroke=0)

    mono = 20 * mm
    mx, my = MARGIN, H - hdr_h - 5 * mm
    c.setFillColor(white)
    c.roundRect(mx, my, mono, mono, 2 * mm, fill=1, stroke=0)
    c.setFillColor(ORANGE)
    c.setFont(FONT_B, 14)
    c.drawCentredString(mx + mono / 2, my + 7.5 * mm, "LJW")
    c.setFont(FONT, 6)
    c.setFillColor(MUTED)
    c.drawCentredString(mx + mono / 2, my + 3.2 * mm, "Agent · Eval")

    c.setFillColor(white)
    c.setFont(FONT, 8.5)
    c.drawString(mx + mono + 4 * mm, H - 9 * mm, "Software Engineer (인턴) · Local Jobs 지원")
    c.setFont(FONT_B, 20)
    c.drawString(mx + mono + 4 * mm, H - 17.5 * mm, "이지우  Lee Ji-woo")

    y = H - hdr_h - 7 * mm
    c.setFillColor(MUTED)
    c.setFont(FONT, 7)
    c.drawString(
        mx + mono + 4 * mm, y + 1.5 * mm,
        "010-4824-6873  ·  dlwldn4824@naver.com  ·  github.com/dlwldn4824  ·  광운대 정보융합 VT",
    )
    hline(c, MARGIN, y - 1 * mm, W - 2 * MARGIN)

    # LEFT
    lx, ly = MARGIN, y - 7 * mm

    ly = section(c, "한 줄 소개", lx, ly, LEFT_W)
    ly = draw_text(
        c,
        "LLM의 답을 업무 흐름으로 연결하고, 역할·룰·도구·평가로 개선하는 개발자입니다. 프롬프트보다 핸드오프가 끊기는 지점을 먼저 고칩니다.",
        lx, ly, size=7.3, max_w=LEFT_W, leading=9.5,
    )
    ly -= 2 * mm

    ly = section(c, "핵심 세 가지", lx, ly, LEFT_W)
    for s in [
        "멀티에이전트·RAG·조건부 Safety를 Single과 비교·평가",
        "탐지→Risk→HITL 확정까지 도시관리 업무 파이프라인",
        "틀린 전제는 버리고 평가 가능한 시스템으로 재설계",
    ]:
        ly = bullet(c, s, lx, ly, size=7.1, max_w=LEFT_W, leading=9.2)
    ly -= 1.8 * mm

    ly = section(c, "전문 분야", lx, ly, LEFT_W)
    ly = tag_row(
        c,
        ["#LLM", "#Multi-Agent", "#RAG", "#Eval", "#HITL", "#Rules", "#YOLO", "#FastAPI", "#React", "#RN", "#PCC", "#MCP관심"],
        lx, ly, LEFT_W,
    )
    ly -= 1.2 * mm
    for s in [
        "Agent: 역할 분리 · Safety Gate · Revision",
        "RAG: NIMH/WHO KB · ChromaDB · Ollama",
        "CV→업무: YOLO · Risk · OCR · CONFIRMED",
        "Product: 일정 조율 핸드오프 · 발음 Eval",
    ]:
        ly = bullet(c, s, lx, ly, size=7.0, max_w=LEFT_W)
    ly -= 1.5 * mm

    ly = section(c, "진행 중", lx, ly, LEFT_W)
    c.setFillColor(ORANGE)
    c.setFont(FONT_B, 7.4)
    c.drawString(lx, ly, "LG Aimers · piching_machine")
    ly -= 2.6 * mm
    c.setFillColor(MUTED)
    c.setFont(FONT, 6.1)
    c.drawString(lx, ly, "github.com/dlwldn4824/piching_machine")
    ly -= 2.8 * mm
    ly = draw_text(
        c,
        "Phase2 투구 제구 확률. E20(Form/Intent/Exec/Clutch)+CatBoost · holdout BSS≈644.",
        lx, ly, size=6.6, max_w=LEFT_W, leading=8.5, color=MUTED,
    )
    ly -= 1.2 * mm
    c.setFillColor(ORANGE)
    c.setFont(FONT_B, 7.4)
    c.drawString(lx, ly, "NeSy-SMP 논문 재현")
    ly -= 2.6 * mm
    c.setFillColor(MUTED)
    c.setFont(FONT, 6.1)
    c.drawString(lx, ly, "github.com/dlwldn4824/NeSy-SMP-repro")
    ly -= 2.8 * mm
    ly = draw_text(
        c,
        "Neuro-symbolic sepsis mortality 재현·감사. 독자 연구 아님 — 논문↔코드 grounding Current Study.",
        lx, ly, size=6.6, max_w=LEFT_W, leading=8.5, color=MUTED,
    )
    ly -= 1.5 * mm

    ly = section(c, "학력", lx, ly, LEFT_W)
    c.setFillColor(INK)
    c.setFont(FONT_B, 7.8)
    c.drawString(lx, ly, "광운대 정보융합학부 VT")
    ly -= 3 * mm
    c.setFont(FONT, 7)
    c.setFillColor(MUTED)
    c.drawString(lx, ly, "2024.03~ · GPA 4.32 / 전공 4.5")
    ly -= 3.2 * mm
    ly = bullet(c, "만점 학기 2회 · 성적우수·Dean's List", lx, ly, size=7.0, max_w=LEFT_W)
    ly = bullet(c, "A+: ML·DB·텍마·자료구조·OSS", lx, ly, size=7.0, max_w=LEFT_W)
    ly -= 1.8 * mm

    ly = section(c, "수상 (GitHub)", lx, ly, LEFT_W)
    for s in [
        "대상·파이썬SW 심화우수 · Smart Icheon · smart_icheon_care",
        "장려×2 · HOPE · HOPE_organization",
    ]:
        ly = bullet(c, s, lx, ly, size=6.9, max_w=LEFT_W)

    if ly > COL_BOT + 22 * mm:
        ly = COL_BOT + 20 * mm
    box_h = ly - COL_BOT - 1.5 * mm
    if box_h > 14 * mm:
        gray_box(c, lx, ly + 1.5 * mm, LEFT_W, box_h)
        ty = ly - 1.8 * mm
        c.setFillColor(ORANGE)
        c.setFont(FONT_B, 7.2)
        c.drawString(lx + 1.8 * mm, ty, "왜 Local Jobs인가")
        ty -= 3.2 * mm
        draw_text(
            c,
            "에이전트가 동료가 되려면 룰·스킬·Eval·핸드오프가 필요합니다. PinTime·멀티에이전트·HITL로 그 뼈대를 짰고, MCP·사내 도구로 확장하고 싶습니다.",
            lx + 1.8 * mm, ty, size=6.6, max_w=LEFT_W - 3.5 * mm, leading=8.6, color=INK,
        )

    # RIGHT
    rx, ry = RIGHT_X, y - 7 * mm

    ry = section(c, "문제 해결 방식", rx, ry, RIGHT_W)
    gray_box(c, rx, ry + 1.5 * mm, RIGHT_W, 26 * mm)
    ty = ry - 0.8 * mm
    for line in [
        "1. 답이 아니라 끊긴 핸드오프를 정의한다 — 조율·확정·등록 / 탐지·조치 / 가정·치료실.",
        "2. 되돌릴 수 있는 곳엔 LLM·AI, 없는 곳엔 룰·Safety Gate·사람 승인.",
        "3. Agent 수보다 역할 경계·공유 컨텍스트·출력 규격·검증 지점을 설계한다.",
        "4. Judge·F1·설문·Revision rate로 평가하고, 틀린 전제(직접 학습 등)는 버린다.",
    ]:
        ty = draw_text(c, line, rx + 2.2 * mm, ty, size=7.2, max_w=RIGHT_W - 4.5 * mm, leading=9.3)
    ry = ry - 28 * mm

    ry = section(c, "RESEARCH  Multi-Agent Mental Health", rx, ry, RIGHT_W)
    c.setFillColor(MUTED)
    c.setFont(FONT, 6.5)
    c.drawRightString(W - MARGIN, ry + 5.5 * mm, "github.com/dlwldn4824/TM-MultiLayer-MentalHealth")
    ry = draw_text(
        c,
        "단일 LLM이 맥락·위험·생성·안전을 한 번에 맡으면 실패 지점을 못 찾습니다. Retriever→Reasoning→Safety와 Conditional Revision으로 Single과 비교했습니다.",
        rx, ry, size=7.3, max_w=RIGHT_W, leading=9.5,
    )
    for b in [
        "Phase1: Three-Agent Safety 4.83 · Empathy 4.31 (CounselChat, qwen2.5:7b)",
        "Phase2: qwen2.5:7b+three_agent score 69.40 · Empathy/Safety↑ 경향",
        "핵심은 Agent 수가 아니라 Safety Verification·Revision Layer (Ablation)",
        "Conditional: 문제일 때만 Revision(~6%) — Safety↑·Runtime↓ 방향",
        "스택: Ollama · ChromaDB · NIMH/WHO KB · LLM Judge + BERTScore/ROUGE",
    ]:
        ry = bullet(c, b, rx, ry, size=7.1, max_w=RIGHT_W)
    ry -= 1.8 * mm

    ry = section(c, "PROJECT  PinTime · 일정 조율 에이전트", rx, ry, RIGHT_W)
    ph = 30 * mm
    gray_box(c, rx, ry + 0.8 * mm, RIGHT_W, ph)
    c.setFillColor(ORANGE)
    c.setFont(FONT_B, 8)
    c.drawString(rx + 2.2 * mm, ry - 1.8 * mm, "대화→제약→후보→사람 확정→캘린더")
    c.setFillColor(MUTED)
    c.setFont(FONT, 6.2)
    c.drawRightString(W - MARGIN - 1.5 * mm, ry - 1.8 * mm, "진행 중 · vercel.app")
    ty = ry - 5.5 * mm
    for b in [
        "문제: When2Meet식 방마다 재입력·확정 후 캘린더 재등록으로 흐름이 끊김.",
        "구조: 규칙 파이프라인(하드/소프트 제약) · 휴리스틱 추천 · 승인 핸드오프.",
        "현황: 프로토타입 라이브. 서비스 배포 목표로 LLM·실캘린더·서버 확장 중.",
        "지표 관점: 추천 수 < 확정까지 대화·충돌 재발·도구 전달 성공.",
    ]:
        ty = bullet(c, b, rx + 1.2 * mm, ty, size=7.0, max_w=RIGHT_W - 2.5 * mm)
    ry = ry - ph - 1.8 * mm

    ph2 = 28 * mm
    if ry - ph2 > COL_BOT:
        gray_box(c, rx, ry + 0.8 * mm, RIGHT_W, ph2)
        c.setFillColor(ORANGE)
        c.setFont(FONT_B, 8)
        c.drawString(rx + 2.2 * mm, ry - 1.8 * mm, "Smart Icheon Care · HITL 업무 파이프라인")
        c.setFillColor(MUTED)
        c.setFont(FONT, 6.2)
        c.drawRightString(W - MARGIN - 1.5 * mm, ry - 1.8 * mm, "심화우수·대상")
        ty = ry - 5.5 * mm
        for b in [
            "YOLO11s→ByteTrack→Risk/Priority→OCR→공무원 CONFIRMED (탐지≠확정).",
            "A/B: all 0.4913 > filtered 0.4811 → 최종 F1 0.591 · mAP50 0.439.",
            "AI 출력을 ‘어디·무엇·왜 먼저’ 업무 단위로 · 파이썬 SW 심화 우수 · 컨소시엄 대상.",
        ]:
            ty = bullet(c, b, rx + 1.2 * mm, ty, size=7.0, max_w=RIGHT_W - 2.5 * mm)

    c.setFillColor(MUTED)
    c.setFont(FONT, 6.5)
    c.drawString(MARGIN, 5.5 * mm, "이지우 · Local Jobs · github.com/dlwldn4824")
    c.drawRightString(W - MARGIN, 5.5 * mm, "1 / 2")
    c.setFillColor(ORANGE)
    c.rect(0, 0, W, 2 * mm, fill=1, stroke=0)

    c.showPage()

    # ========== PAGE 2 ==========
    c.setFillColor(ORANGE)
    c.rect(0, H - 9 * mm, W, 9 * mm, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont(FONT_B, 10.5)
    c.drawString(MARGIN, H - 6 * mm, "이지우  ·  Agents → Workflow → Eval")
    c.setFont(FONT, 7.5)
    c.drawRightString(W - MARGIN, H - 6 * mm, "README 정합 · GitHub 링크")

    y = H - 15 * mm
    x = MARGIN
    full_w = W - 2 * MARGIN

    def project_block(title, meta, bullets, y):
        h = 9 * mm + len(bullets) * 9.6 * mm
        gray_box(c, x, y + 0.8 * mm, full_w, h)
        c.setFillColor(ORANGE)
        c.rect(x, y - h + 0.8 * mm, 1.6 * mm, h, fill=1, stroke=0)
        c.setFillColor(INK)
        c.setFont(FONT_B, 9)
        c.drawString(x + 3.5 * mm, y - 2.2 * mm, title)
        c.setFillColor(MUTED)
        c.setFont(FONT, 6.5)
        c.drawRightString(W - MARGIN - 1.5 * mm, y - 2.2 * mm, meta)
        ty = y - 6.8 * mm
        for b in bullets:
            ty = bullet(c, b, x + 2.5 * mm, ty, size=7.3, max_w=full_w - 7 * mm, leading=9.5)
        return y - h - 2.4 * mm

    y = section(c, "PROJECTS (상세 · GitHub)", x, y, full_w)

    y = project_block(
        "Multi-Agent Mental Health — 역할·Safety·조건부 Revision",
        "TM-MultiLayer-MentalHealth",
        [
            "배경: 자연스러운 답 ≠ 증상·위험 파악. Single LLM은 실패 지점을 가린다.",
            "작업: 구조 비교 → 모델×구조 → Ablation → Conditional Bidirectional 고정.",
            "성과: Three-Agent 효과 확인 · Revision Layer가 핵심 · 에이전트=시스템으로 이해.",
            "링크: github.com/dlwldn4824/TM-MultiLayer-MentalHealth",
        ],
        y,
    )

    y = project_block(
        "Smart Icheon Care — 탐지를 행정 업무로",
        "smart_icheon_care · 심화우수·대상",
        [
            "현장: 461km²·인력 격차 → 전수 순찰 대신 Risk 선별·사람 확정.",
            "파이프라인: 탐지·추적·GIS·공공데이터·OCR·상태머신(CONFIRMED).",
            "지표: all>filtered 선정 · test F1 0.591 · mAP50 0.439 · 파이썬 SW 심화 우수상 · 컨소시엄 대상.",
            "링크: github.com/dlwldn4824/smart_icheon_care",
        ],
        y,
    )

    y = project_block(
        "PinTime — 핸드오프 없는 일정 워크플로 (진행 중)",
        "배포 목표 · pintime.vercel.app",
        [
            "하드/소프트 제약 분리 · 확정 전 충돌 검증 · 같은 저장소 캘린더 등록.",
            "사전질문 연결: 회의 예약 에이전트 = 캘린더·참석자·충돌·확정 도구 + 사람 승인.",
            "정직 범위: 규칙 에이전트 데모. MCP/실캘린더 확장은 인턴십에서 깊게.",
            "링크: github.com/dlwldn4824/pintime",
        ],
        y,
    )

    y = project_block(
        "HOPE (또박또박) — 평가 구조를 먼저 고침",
        "HOPE_organization · 장려×2 · 팀장",
        [
            "가정↔치료실 피드백 공백 → 게임 연습 + 음소 피드백 + 보호자·치료사 기록.",
            "STT 보정 한계 → Wav2Vec2-CTC·g2pK·정렬·PCC/PER로 ‘어떻게 발음했는지’ 보존.",
            "틀린 전제(소수 오류 직접 학습)를 버리고 데이터·평가 조건 고정 우선.",
            "링크: github.com/dlwldn4824/HOPE_organization",
        ],
        y,
    )

    # Skills dense
    y = section(c, "보유 기술 (프로젝트 연결)", x, y, full_w)
    gray_box(c, x, y + 0.8 * mm, full_w, 22 * mm)
    ty = y - 2 * mm
    rows = [
        ("LLM·Agent", "Python · Ollama/qwen · ChromaDB · Judge Eval · 역할/핸드오프 — TM / PinTime"),
        ("AI·Data", "PyTorch · YOLO11 · ByteTrack · Wav2Vec2/CTC · PCC·PER — Icheon / HOPE"),
        ("Product", "FastAPI · React/RN · TS · 현장 인터뷰·가설 수정 — 전 프로젝트"),
    ]
    for label, desc in rows:
        c.setFillColor(ORANGE)
        c.setFont(FONT_B, 7.3)
        c.drawString(x + 2.2 * mm, ty, label)
        lw = c.stringWidth(label, FONT_B, 7.3) + 2 * mm
        c.setFillColor(INK)
        c.setFont(FONT, 7.0)
        c.drawString(x + 2.2 * mm + lw, ty, desc)
        ty -= 6.2 * mm
    y = y - 24 * mm

    # JD + close
    y = section(c, "공고와의 접점", x, y, full_w)
    rows = [
        ("에이전트·도구", "PinTime·멀티에이전트 — 시스템을 한 워크플로로"),
        ("룰·스킬·메모리", "계층·RAG KB·확정 제약 — 경험이 쌓이는 구조"),
        ("AI 한계·HITL", "Icheon CONFIRMED · HOPE 임상 한계 명시"),
        ("Eval·개선", "Judge·F1·PCC · Conditional Revision rate"),
    ]
    box_h = 4 * mm + len(rows) * 6.2 * mm
    gray_box(c, x, y + 0.8 * mm, full_w, box_h)
    ty = y - 1.8 * mm
    for label, desc in rows:
        c.setFillColor(ORANGE)
        c.setFont(FONT_B, 7.2)
        c.drawString(x + 2.2 * mm, ty, label)
        lw = c.stringWidth(label, FONT_B, 7.2) + 2 * mm
        c.setFillColor(INK)
        c.setFont(FONT, 7.0)
        c.drawString(x + 2.2 * mm + lw, ty, desc)
        ty -= 6.0 * mm
    y = y - box_h - 2 * mm

    y = section(c, "지원 동기", x, y, full_w)
    remain = y - (COL_BOT + 1 * mm)
    box_h = max(remain, 24 * mm)
    gray_box(c, x, y + 0.8 * mm, full_w, box_h)
    c.setFillColor(ORANGE)
    c.rect(x, y - box_h + 0.8 * mm, 1.6 * mm, box_h, fill=1, stroke=0)
    ty = y - 3 * mm
    for line in [
        "Local Jobs의 ‘에이전트가 밤사이 해 둔 일을 읽는 아침’은, 제가 멀티에이전트·PinTime·HITL에서 목표한 핸드오프 없는 업무 흐름과 같습니다.",
        "서류 사전질문(실험·6개월 변화·데이터 제안 에이전트·회의 예약)에 대해, 일정 조율 에이전트와 계층·RAG·Eval로 비슷한 뼈대를 이미 짜 봤습니다. MCP와 사내 도구로 확장하는 일을 배우고 싶습니다.",
        "한 줄: LLM 답을 업무로 연결하고, 역할·룰·평가로 계속 나아지는 시스템을 만드는 개발자 — github.com/dlwldn4824",
    ]:
        ty = draw_text(c, line, x + 3.5 * mm, ty, size=7.3, max_w=full_w - 7 * mm, leading=9.6)

    c.setFillColor(MUTED)
    c.setFont(FONT, 6.5)
    c.drawString(MARGIN, 5.5 * mm, "010-4824-6873 · dlwldn4824@naver.com · github.com/dlwldn4824")
    c.drawRightString(W - MARGIN, 5.5 * mm, "2 / 2")
    c.setFillColor(ORANGE)
    c.rect(0, 0, W, 2 * mm, fill=1, stroke=0)

    c.save()
    print("Wrote", OUT)


if __name__ == "__main__":
    build()
