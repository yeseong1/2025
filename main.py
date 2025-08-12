# app.py
import streamlit as st
from datetime import datetime, time
import random
import pandas as pd

st.set_page_config(page_title="🔮 몽환 사주풀이 ✨", page_icon="🌙", layout="wide")

# ---- 상수: 간지 및 오행 맵 ----
HEAVENLY_STEMS = ["갑","을","병","정","무","기","경","신","임","계"]
EARTHLY_BRANCHES = ["자","축","인","묘","진","사","오","미","신","유","술","해"]
STEM_ELEMENT = {
    "갑":"목","을":"목","병":"화","정":"화","무":"토",
    "기":"토","경":"금","신":"금","임":"수","계":"수"
}
BRANCH_HIDDEN_STEMS = {
    # 간략표 (상세한 '육기'는 생략) — 재미용
    "자":["임"], "축":["기","신"], "인":["갑","병"], "묘":["갑"],
    "진":["무","갑","을"], "사":["병","정"], "오":["병","정"], "미":["기","병"],
    "신":["경","임"], "유":["경"], "술":["무","경","신"], "해":["임","계"]
}

# 몽환 이모지 풀 (풍성하게)
DREAM_EMOJI = ["🌙","🔮","✨","🌌","🪐","🌸","💫","🕯️","🌊","⭐","🌠","🦋","🧚","🍃","🌿","🎐","💜","💙","💖","❇️"]

# ---- 유틸: 그레고리력 -> JDN (Julian Day Number) ----
def gregorian_to_jdn(year, month, day):
    # 알고리즘: Fliegel & Van Flandern
    a = (14 - month) // 12
    y = year + 4800 - a
    m = month + 12*a - 3
    jdn = day + ((153*m + 2)//5) + 365*y + y//4 - y//100 + y//400 - 32045
    return jdn

# ---- 간지 계산 (간단판) ----
def year_ganji(year):
    # 전통적으로 (year - 4) 기반
    idx = (year - 4) % 10
    jdx = (year - 4) % 12
    return HEAVENLY_STEMS[idx], EARTHLY_BRANCHES[jdx]

def month_branch_from_solar_month(month):
    # 단순화: 양력 월 -> 월지(음력·절기 정확성 없음)
    # 음력 1월(정월) → 寅(인) 으로 시작하는 전통적 배치 기준(단순 매핑)
    lunar_map = {1:"인",2:"묘",3:"진",4:"사",5:"오",6:"미",7:"신",8:"유",9:"술",10:"해",11:"자",12:"축"}
    return lunar_map.get(month, "인")

def day_ganji(year, month, day):
    # JDN 기반의 단순 계산. 실제 전문 역법과는 차이 있을 수 있음(놀이용).
    jdn = gregorian_to_jdn(year, month, day)
    stem_idx = (jdn + 9) % 10   # 경험적 공식(일간 계산 단순화)
    branch_idx = (jdn + 1) % 12
    return HEAVENLY_STEMS[stem_idx], EARTHLY_BRANCHES[branch_idx]

def hour_branch_from_hour(hour):
    # 전통 시각(2시간 단위): 23-0 -> 자, 1-2 -> 축, ...
    # 입력 hour는 0~23
    mapping = [
        (23, "자"), (0, "자"),
        (1, "축"), (2, "축"),
        (3, "인"), (4, "인"),
        (5, "묘"), (6, "묘"),
        (7, "진"), (8, "진"),
        (9, "사"), (10, "사"),
        (11, "오"), (12, "오"),
        (13, "미"), (14, "미"),
        (15, "신"), (16, "신"),
        (17, "유"), (18, "유"),
        (19, "술"), (20, "술"),
        (21, "해"), (22, "해"),
    ]
    for h, b in mapping:
        if h == hour:
            return b
    # 기본
    return "자"

# ---- 해석(간단·놀이용) ----
def interpret(gan, ji, label):
    stem_elem = STEM_ELEMENT.get(gan, "토")
    hidden = BRANCH_HIDDEN_STEMS.get(ji, [])
    emojis = " ".join(random.choices(DREAM_EMOJI, k=6))
    lines = []
    lines.append(f"{label} 간지: {gan}{ji}  —  (오행: {stem_elem}) {emojis}")
    lines.append(f"  • 성향 힌트: {gan}의 에너지({stem_elem})가 드러나며, {ji}의 감성(숨은 기운: {', '.join(hidden)})이 영향을 줘요.")
    # 간단 운명톤 문장 (무작위 변형으로 다양성)
    vibes = [
        "내면에 깊은 상상력과 감성이 흐름 🌊🔮",
        "실용적이면서도 낭만을 꿈꾸는 기질 ✨🌙",
        "결단력과 섬세함이 번갈아 나타남 🌿⚡",
        "사소한 것에서 큰 위로를 찾는 타입 🕯️💫"
    ]
    lines.append("  • 풀이: " + random.choice(vibes) + "  " + " ".join(random.choices(DREAM_EMOJI, k=4)))
    return "\n".join(lines)

# ---- 세션 초기화(즐겨찾기) ----
if "saju_favs" not in st.session_state:
    st.session_state.saju_favs = []

# ---- UI ----
st.markdown("<h1 style='text-align:left'>🔮 몽환 사주풀이 (놀이터 ver.) 🌙✨</h1>", unsafe_allow_html=True)
st.write("생년월일과 태어난 시(시: 0~23)를 입력하면 간단한 간지(년·월(단순)·일·시)와 몽환한 풀이를 보여줘요. 정확한 음력·절기 변환은 별도 처리 필요해요. 🪐🌌🧚‍♀️")

col1, col2 = st.columns([2,1])
with col1:
    dob = st.date_input("태어난 날 선택 (양력) 🗓️", value=datetime.today())
    born_hour = st.slider("태어난 시 (24시간 기준) ⏰", 0, 23, 12)
    nickname = st.text_input("닉네임 (결과에 표시할 이름) ✨", value="정직한샌드위치6901")
    toon_level = st.slider("몽환 이모지 과다지수 🌙✨ (더 높을수록 이모지 폭발) ", 1, 10, 6)
with col2:
    st.markdown("### 사용 팁 🪄")
    st.write("· 음력/절기 정확 판독 원하면 '음력 변환' 옵션 요청해줘야 처리 가능해요.")
    st.write("· 결과는 재미용으로 가볍게 즐겨줘~ 🔮🧩")
    st.write("· 저장한 결과는 아래에서 CSV로 받아볼 수 있어요 📥")

if st.button("사주 풀이 받기 ✨🔮"):
    y, m, d = dob.year, dob.month, dob.day

    # 간지 계산
    yg, yj = year_ganji(y)
    mg = month_branch_from_solar_month(m)
    dg, dj = day_ganji(y, m, d)
    hj = hour_branch_from_hour(born_hour)

    # 풀이 텍스트
    header_emojis = " ".join(random.choices(DREAM_EMOJI, k=max(6, toon_level)))
    st.markdown(f"## {nickname}님의 사주풀이 💫 {header_emojis}")
    st.write(f"입력: {y}년 {m}월 {d}일, {born_hour}시  —  (양력 기준)  🌙🔭")

    # 연간
    st.markdown("### ✨ 연간(년) ✨")
    st.text(interpret(yg, yj, "연"))

    # 월간 (단순)
    st.markdown("### ✨ 월간(월, 단순판) ✨")
    # 월은 간/지 분해가 복잡하므로 간단 설명형으로 처리
    month_emojis = " ".join(random.choices(DREAM_EMOJI, k=5))
    st.write(f"월지(단순 매핑): {mg}  —  월의 영향으로 감성·관계·일상의 리듬이 조율됨 {month_emojis}")
    st.write("  • 월 영향 풀이: 한 달 단위의 기운이 감정 리듬과 대인관계 흐름에 영향을 줘요. 몽환적 기운과 안정감의 균형을 찾아보세요. " + " ".join(random.choices(DREAM_EMOJI, k=4)))

    # 일간
    st.markdown("### ✨ 일간(일) ✨")
    st.text(interpret(dg, dj, "일"))

    # 시간
    st.markdown("### ✨ 시간(시) ✨")
    # 시간은 지지만 표시(시주는 실제로 시간의 간 포함)
    time_emojis = " ".join(random.choices(DREAM_EMOJI, k=6))
    st.write(f"시지(시): {hj}  —  시간대에 따라 본능·습관·반응이 달라짐 {time_emojis}")
    st.write("  • 시간 해석: 밤과 새벽, 낮과 저녁에 따라 에너지 패턴이 달라요. 본인이 가장 편안한 시간대를 관찰해보면 좋음 🌌🕯️")

    # 요약 문장(랜덤화된 몽환 문구)
    summary_lines = [
        f"요약: 전체적으로 {STEM_ELEMENT.get(yg,'토')}의 기운이 기반이 되며, {dj}의 감성이 결합되어 내면의 상상력과 현실 감각이 섞이는 타입이에요. {''.join(random.choices(DREAM_EMOJI, k=8))}",
        f"요약: 감성의 물결과 현실의 닻이 공존하는 사주. 작은 일상에서 큰 위로를 찾는 성향이 강해요. {''.join(random.choices(DREAM_EMOJI, k=8))}",
        f"요약: 창의적이고 섬세한 기운이 돋보이며, 밤시간에 영감이 샘솟는 편일 가능성이 높아요. {''.join(random.choices(DREAM_EMOJI, k=8))}"
    ]
    st.success(random.choice(summary_lines))

    # 저장 옵션
    if st.button("💾 이 풀이 저장하기 (즐겨찾기)"):
        st.session_state.saju_favs.append({
            "saved_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "nickname": nickname,
            "dob": f"{y}-{m:02d}-{d:02d}",
            "hour": born_hour,
            "year_ganji": yg + yj,
            "month_jiji": mg,
            "day_ganji": dg + dj,
            "hour_jiji": hj
        })
        st.balloons()
        st.success("저장했어용! 🎐🔮")

st.markdown("---")
st.markdown("## 💾 저장한 풀이 모음 (CSV로 내보내기 가능)")
if st.session_state.saju_favs:
    df = pd.DataFrame(st.session_state.saju_favs)
    st.table(df)
    csv = df.to_csv(index=False).encode('utf-8-sig')
    st.download_button("CSV 다운로드 📥", data=csv, file_name="saju_favorites.csv", mime="text/csv")
    if st.button("모두 삭제하기 🗑️"):
        st.session_state.saju_favs = []
        st.success("모두 삭제했음! 🧹")
else:
    st.write("아직 저장된 풀이가 없어요. 마음에 들면 저장해봐~ 🌙✨")

st.markdown("---")
st.write("Tip: 진짜 전문가 수준의 사주(절기·음력·시·분 단위 정확한 시주)를 원하면 '음력 변환 + 절기 기반 월주 계산' 모듈을 연동해줄게. 필요하면 알려줘! 🔭🧭")
