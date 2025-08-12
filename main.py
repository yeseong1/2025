# app.py
import streamlit as st
import random
import pandas as pd
import io
from datetime import datetime

st.set_page_config(page_title="💘 MBTI 설레소개팅", page_icon="💞", layout="wide")  # 레이아웃 wide 사용 [【5】](https://wikidocs.net/231599)

MBTI_LIST = [
    "ISTJ","ISFJ","INFJ","INTJ",
    "ISTP","ISFP","INFP","INTP",
    "ESTP","ESFP","ENFP","ENTP",
    "ESTJ","ESFJ","ENFJ","ENTJ"
]

# 추천 맵: (타입, 점수)
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

# 간단한 설명 맵
REASON_MAP = {
    "ENFP":"창의적이고 따뜻해서 서로에게 영감을 줘요 ✨",
    "INFJ":"깊은 공감대와 가치관이 잘 맞아요 💫",
    "ISTJ":"실용적이어서 안정감을 줘요 🛡️",
    "ESFP":"활발하고 낭만적인 에너지로 즐거움을 줘요 🎉",
    "ESTP":"스릴 있고 즉흥적인 재미를 함께해요 ⚡",
    # 기본 fallback
}

def calculate_recommendations(my_mbti, n=2, randomness=0.1):
    base = COMPATIBILITY.get(my_mbti, [])
    # 후보를 점수 리스트로 만듦
    scored = [(t, s) for (t,s) in base]
    # 필요하면 랜덤 후보 추가 (다양성)
    if len(scored) < n:
        extras = [m for m in MBTI_LIST if m != my_mbti and m not in [x[0] for x in scored]]
        random.shuffle(extras)
        for e in extras[:n-len(scored)]:
            scored.append((e, random.randint(55,75)))
    # 약간의 변동성 추가
    final = []
    for t, s in scored:
        delta = int((random.random() - 0.5) * 2 * randomness * 100)  # -rand ~ +rand
        new_score = max(30, min(100, s + delta))
        final.append((t, new_score))
    # 다른 후보들 중에서 일부 랜덤 추천 후보 섞기(다양성 증가)
    others = [m for m in MBTI_LIST if m != my_mbti and m not in [x[0] for x in final]]
    random.shuffle(others)
    for o in others[:3]:
        final.append((o, random.randint(30,70)))
    # 정렬 후 상위 n 선택
    final_sorted = sorted(final, key=lambda x: x[1], reverse=True)
    return final_sorted[:n]

# 세션 상태 초기화
if "favorites" not in st.session_state:
    st.session_state.favorites = []

# UI
st.title("💘 MBTI 설레소개팅 💕✨")
st.write("내 MBTI 골라서 설레는 추천을 받아봐! 마음에 들면 저장도 가능해요 🥰")

col1, col2 = st.columns([2,1])
with col1:
    my_mbti = st.selectbox("내 MBTI 선택 💭", MBTI_LIST, index=0)
    n = st.slider("추천 개수 🔍", min_value=1, max_value=5, value=2)
    randomness = st.slider("추천 다양성(랜덤 정도) 🎲", 0.0, 0.5, 0.1, step=0.05)
with col2:
    st.markdown("### Quick Tips")
    st.write("· 좋아요 버튼으로 저장 가능 ❤️")
    st.write("· 저장한 목록은 CSV로 다운로드 가능 📥")
    st.write("· 결과는 매번 살짝 바뀔 수 있어요 ✨")

if st.button("설레는 추천 받기 💓"):
    recs = calculate_recommendations(my_mbti, n=n, randomness=randomness)
    st.subheader("추천 결과 💖")
    for idx, (mbti, score) in enumerate(recs, start=1):
        # 카드 형식으로 보기
        emoji_line = "💞✨💫" if score >= 90 else "💖✨" if score >= 75 else "🌸✨"
        st.markdown(f"### {idx}. {mbti} {emoji_line}  점수: {score} / 100")
        reason = REASON_MAP.get(mbti, "서로 보완되는 성향이 있어 서로에게 긍정적 영향을 줘요 💕")
        st.write(f"이유: {reason}")
        # 진행바로 설렘지수 시각화
        st.progress(score / 100.0)
        # 저장 버튼 (각 카드별)
        if st.button(f"♥ {mbti} 저장하기", key=f"save_{mbti}_{idx}"):
            st.session_state.favorites.append({
                "saved_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "my_mbti": my_mbti,
                "match_mbti": mbti,
                "score": score
            })
            st.success(f"{mbti} 저장완료! 💾")

st.markdown("---")
st.subheader("💾 저장한 추천 목록")
if st.session_state.favorites:
    df = pd.DataFrame(st.session_state.favorites)
    st.table(df)
    # CSV 다운로드
    csv = df.to_csv(index=False).encode('utf-8-sig')
    st.download_button("CSV로 다운로드 📥", data=csv, file_name="mbti_favorites.csv", mime="text/csv")
    if st.button("모두 삭제하기 🗑️"):
        st.session_state.favorites = []
        st.success("모두 삭제했어요")
else:
    st.write("아직 저장된 추천이 없어요. 마음에 드는 유형을 저장해봐요 💘")
