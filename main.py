# app.py
import streamlit as st
import random

st.set_page_config(page_title="MBTI 소개팅 추천", page_icon="💘")

MBTI_LIST = [
    "ISTJ","ISFJ","INFJ","INTJ",
    "ISTP","ISFP","INFP","INTP",
    "ESTP","ESFP","ENFP","ENTP",
    "ESTJ","ESFJ","ENFJ","ENTJ"
]

# 간단한 호환 맵 (필요하면 수정/확장)
COMPATIBILITY = {
    "ISTJ": ["ESFP","ESTP"],
    "ISFJ": ["ESFP","ENFP"],
    "INFJ": ["ENFP","ENTP"],
    "INTJ": ["ENFP","ENTP"],
    "ISTP": ["ESFJ","ISFJ"],
    "ISFP": ["ESTJ","ENTJ"],
    "INFP": ["ENFJ","ESFJ"],
    "INTP": ["ENFJ","ENTJ"],
    "ESTP": ["ISFJ","ISTJ"],
    "ESFP": ["ISTJ","ISFJ"],
    "ENFP": ["INFJ","INTJ"],
    "ENTP": ["INFJ","INTJ"],
    "ESTJ": ["ISFP","INFP"],
    "ESFJ": ["ISTP","INTP"],
    "ENFJ": ["INFP","INTP"],
    "ENTJ": ["ISFP","ISFJ"]
}

def recommend(mbti, n=2):
    candidates = COMPATIBILITY.get(mbti, [])
    # 후보가 n보다 적으면 다른 유형 섞어 채움
    if len(candidates) < n:
        extras = [m for m in MBTI_LIST if m not in candidates and m != mbti]
        random.shuffle(extras)
        candidates = candidates + extras[:max(0, n - len(candidates))]
    return candidates[:n]

st.title("💘 MBTI 소개팅 추천 앱")
st.write("자기 MBTI를 선택하면 잘 맞는 MBTI 타입을 추천해줄게!")

col1, col2 = st.columns([2,1])
with col1:
    selected = st.selectbox("내 MBTI 선택", MBTI_LIST, index=0)
with col2:
    count = st.number_input("추천 개수", min_value=1, max_value=5, value=2, step=1)

if st.button("추천 받기"):
    recs = recommend(selected, n=count)
    st.subheader("추천 MBTI")
    for r in recs:
        st.markdown(f"### {r}  ✅")
        # 간단한 이유 표시 (커스터마이즈 가능)
        reason = {
            "ENFP":"감성적이고 창의적이어서 서로 영감을 줌",
            "INFJ":"깊은 공감과 가치관이 맞음",
            "ISTJ":"균형 잡힌 실용성이 잘 맞음"
        }.get(r, "서로 보완적인 성향이 있어 균형이 잘 맞음")
        st.write(f"이유: {reason}")
    st.success("추천이 완료되었어요! 마음에 드는 유형을 저장하거나 다른 설정으로 다시 시도해보세요.")
