# app.py
import streamlit as st
import random
import pandas as pd
from datetime import datetime

# 페이지 설정
st.set_page_config(
    page_title="💘 MBTI 설레소개팅 💕💫",
    page_icon="💞",
    layout="wide"
)

# MBTI 목록
MBTI_LIST = [
    "ISTJ","ISFJ","INFJ","INTJ",
    "ISTP","ISFP","INFP","INTP",
    "ESTP","ESFP","ENFP","ENTP",
    "ESTJ","ESFJ","ENFJ","ENTJ"
]

# 기본 호환 맵(기본 점수 포함)
COMPATIBILITY = {
    "ISTJ": [("ESFP",92),("ESTP",88)],
    "ISFJ": [("ESFP",90),("ENFP",85)],
    "INFJ": [("ENFP",95),("ENTP",88)],
    "INTJ": [("ENFP",93),("ENTP",90)],
    "ISTP": [("ESFJ",87),("ISFJ",82)],
    "ISFP": [("ESTJ",89),("ENTJ",86)],
    "INFP": [("ENFJ",94),("ESFJ",84)],
    "INTP": [("ENFJ",91),("ENTJ",88)],
    "ESTP": [("ISFJ",90),("ISTJ",85)],
    "ESFP": [("ISTJ",93),("ISFJ",88)],
    "ENFP": [("INFJ",96),("INTJ",92)],
    "ENTP": [("INFJ",94),("INTJ",90)],
    "ESTJ": [("ISFP",86),("INFP",82)],
    "ESFJ": [("ISTP",85),("INTP",80)],
    "ENFJ": [("INFP",95),("INTP",88)],
    "ENTJ": [("ISFP",88),("ISFJ",84)]
}

# 추천 이유 기본맵 (더 추가 가능)
REASON_MAP = {
    "ENFP":"창의적이고 따뜻해서 서로에게 영감을 줘요 ✨✨",
    "INFJ":"깊은 공감대와 가치관이 잘 맞아요 💫💖",
    "ISTJ":"안정감 있는 실용성으로 든든해요 🛡️🌿",
    "ESFP":"활발하고 낭만적인 에너지로 일상이 즐거워져요 🎉🌸",
    "ENTJ":"리더십 있고 든든하게 이끌어줘요 🚀🔥",
    # 기본 fallback은 아래에서 처리
}

# 추천 산출 함수: 기본 점수에 랜덤성+사용자 필터 반영
def calculate_recommendations(my_mbti, n=3, randomness=0.15, include_random_extra=True):
    base = COMPATIBILITY.get(my_mbti, [])
    scored = [(t, s) for (t, s) in base]

    # 후보가 부족하면 다른 유형을 보충
    if len(scored) < n:
        extras = [m for m in MBTI_LIST if m != my_mbti and m not in [x[0] for x in scored]]
        random.shuffle(extras)
        for e in extras[:n-len(scored)]:
            scored.append((e, random.randint(55,75)))

    # 점수에 랜덤 변동 추가 (설렘 변동)
    final = []
    for t, s in scored:
        delta = int((random.random() - 0.5) * 2 * randomness * 100)  # -rand ~ +rand
        new_score = max(30, min(100, s + delta))
        final.append((t, new_score))

    # 다양성용 랜덤 후보 약간 추가
    if include_random_extra:
        others = [m for m in MBTI_LIST if m != my_mbti and m not in [x[0] for x in final]]
        random.shuffle(others)
        for o in others[:3]:
            final.append((o, random.randint(30,75)))

    # 점수순 정렬 후 상위 n 반환
    final_sorted = sorted(final, key=lambda x: x[1], reverse=True)
    return final_sorted[:n]

# 세션 상태: 즐겨찾기 저장
if "favorites" not in st.session_state:
    st.session_state.favorites = []

# 레이아웃: 상단 헤더
st.markdown("<h1 style='text-align:left'>💘 MBTI 설레소개팅 💕💞✨</h1>", unsafe_allow_html=True)
st.write("설렘 가득 ✨💓 내 MBTI 골라서 잘 맞는 타입을 찾아보자! 🥰🎀 (이모지 잔치 열림) 🎉🌸💫")

# 컨트롤 패널
left, right = st.columns([3,1])
with left:
    my_mbti = st.selectbox("내 MBTI 선택 💭", MBTI_LIST, index=0)
    n = st.slider("추천 개수 🔍", min_value=1, max_value=6, value=3)
    randomness = st.slider("설렘 변동성(랜덤 정도) 🎲", 0.0, 0.5, 0.15, step=0.05)
    include_random = st.checkbox("가끔은 깜짝 추천도 받기 🎁 (다양성 추가)", value=True)
    nickname = st.text_input("닉네임(결과에 표시할 이름) 📝", value="정직한샌드위치6901")
with right:
    st.markdown("### Quick Tips 💡")
    st.write("· 마음에 들면 ♥ 저장하기 가능! 📥")
    st.write("· 저장한 목록은 CSV로 다운받을 수 있어요 📂")
    st.write("· 매번 결과가 살짝 달라서 더 재밌음 😝")

# 추천 버튼
if st.button("설레는 추천 받기 💞💓✨"):
    recs = calculate_recommendations(my_mbti, n=n, randomness=randomness, include_random_extra=include_random)
    st.markdown("## 추천 결과 💖✨🌸")
    # 결과 카드 스타일로 표시
    for idx, (mbti, score) in enumerate(recs, start=1):
        # 이모지 장식(점수 구간별)
        if score >= 95:
            deco = "💘💞💫🌟✨"
        elif score >= 85:
            deco = "💖🌸✨🎀"
        elif score >= 70:
            deco = "💓🌼✨"
        else:
            deco = "🌸✨"

        st.markdown(f"### {idx}. {mbti} {deco}  ({score} / 100)")
        reason = REASON_MAP.get(mbti, "서로 보완되는 매력이 있어요 💕 서로 배우며 성장할 수 있어요 🌱")
        st.write(f"이유: {reason}  ✨🎈")
        # 시각화: 진행바와 이모지 라인
        st.progress(score / 100.0)
        emoji_line = " ".join(random.choices(["💞","💘","💖","✨","🌸","🌟","🎀","🥰","😍","😘","🎉","🎈"], k=8))
        st.write(emoji_line)

        # 저장 버튼 (각 카드별 고유 key)
        save_key = f"save_{mbti}_{idx}"
        if st.button(f"♥ {mbti} 저장하기", key=save_key):
            st.session_state.favorites.append({
                "saved_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "nickname": nickname,
                "my_mbti": my_mbti,
                "match_mbti": mbti,
                "score": score
            })
            st.success(f"{mbti}을(를) 저장했어요! 💾🎉")
            st.balloons()

    st.info("추천은 매번 살짝 달라질 수 있어요. 여러 번 눌러서 다양한 결과를 즐겨봐요! 😝✨")

st.markdown("---")

# 저장한 목록 표시 & CSV 다운로드
st.markdown("## 💾 저장한 추천 목록 (즐겨찾기) 📥")
if st.session_state.favorites:
    df = pd.DataFrame(st.session_state.favorites)
    st.table(df)
    csv = df.to_csv(index=False).encode('utf-8-sig')
    st.download_button("CSV로 다운로드 📥📂", data=csv, file_name="mbti_favorites.csv", mime="text/csv")
    if st.button("모두 삭제하기 🗑️"):
        st.session_state.favorites = []
        st.success("모두 삭제했어용 😭🧹")
else:
    st.write("아직 저장된 항목이 없어요. 마음에 드는 추천을 저장해보세요! 💘💞✨")

# 푸터: 약간의 장식과 사용 팁
st.markdown("---")
st.write("Tip: 추천 알고리즘은 간단한 규칙+랜덤성을 사용해요. 더 정교한 필터(나이대, 취향, 관심사 등)를 추가하면 결과가 더 맞춤형이 될 수 있어요 🛠️💕")
st.write("즐겁게 사용해~ 😍💕🎉")
