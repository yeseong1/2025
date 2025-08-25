import streamlit as st
import random
from datetime import date

# 💖 앱 설정 및 제목 ✨
st.set_page_config(
    page_title="나에게 딱 맞는 인강 강사 추천! 💡",
    page_icon="🧑‍🏫",
    layout="centered"
)

st.title("나에게 딱 맞는 인강 강사 추천 앱! 📚✨")
st.markdown("---")

# 🎈 이모티콘 팡팡 터뜨리기! 🎉
emojis = ["💡", "📚", "✏️", "🎓", "🧑‍🏫", "✨", "📝", "💯", "✅", "💻", "🌐", "🧠", "👍", "🗣️", "🌍"]

# 세션 상태 초기화 (앱이 새로고침돼도 사용자 입력값 유지되도록)
if 'name' not in st.session_state:
    st.session_state.name = ""
if 'recommended_institute' not in st.session_state:
    st.session_state.recommended_institute = ""
if 'subject' not in st.session_state:
    st.session_state.subject = ""
if 'birthdate' not in st.session_state:
    st.session_state.birthdate = None

# --- 1단계: 이름 입력하고 인강 사이트 추천받기! ---
st.header(f"1단계: 이름 입력 ➡️ 인강 사이트 추천! {random.choice(emojis)}")
st.write("네 이름을 알려줘! 네게 딱 맞는 인강 사이트를 찾아줄게! 👇")

user_name = st.text_input("이름을 입력해주세요:", value=st.session_state.name, max_chars=20)

if user_name:
    st.session_state.name = user_name
    institutes = ["EBS", "이투스", "메가스터디", "대성마이맥"]

    # 이름을 해싱해서 매번 같은 사이트가 추천되도록! (랜덤성 유지하며)
    if not st.session_state.recommended_institute:
        random.seed(len(user_name) + sum(ord(c) for c in user_name)) # 이름에 따라 랜덤 시드 설정
        st.session_state.recommended_institute = random.choice(institutes)

    st.success(f"{user_name}아, 너에게 추천하는 인강 사이트는 바로 **{st.session_state.recommended_institute}** 이야! {random.choice(emojis)} 와우! 🎉")
    st.image("https://media.giphy.com/media/l0HlFZc9Xz1qjA5x6/giphy.gif", width=150) # 추천 gif 추가!
    st.markdown("---")

    # --- 2단계: 과목 선택하기! ---
    st.header(f"2단계: 과목 선택! {random.choice(emojis)}")
    st.write("이제 어떤 과목의 강사님을 찾고 싶어? 🧐")

    # 🔥 여기가 바뀐 부분! '영어' 추가! 🔥
    subjects = ["국어", "수학", "사탐", "영어"]
    selected_subject = st.selectbox(
        "과목을 선택해주세요:",
        subjects,
        index=subjects.index(st.session_state.subject) if st.session_state.subject else 0
    )
    st.session_state.subject = selected_subject
    st.info(f"✔️ {selected_subject} 과목을 선택했구나! {random.choice(emojis)}")
    st.markdown("---")

    # --- 3단계: 생년월일 입력하고 강사님 추천받기! ---
    st.header(f"3단계: 생년월일 입력 ➡️ 강사님 추천! {random.choice(emojis)}")
    st.write("생년월일을 입력하면 네 성향에 더 잘 맞는 강사님을 추천해줄게! (궁예 빙의 🔮)")

    today = date.today()
    user_birthdate = st.date_input(
        "생년월일을 선택해주세요:",
        value=st.session_state.birthdate if st.session_state.birthdate else today,
        min_value=date(1980, 1, 1),
        max_value=today,
        format="YYYY/MM/DD"
    )
    st.session_state.birthdate = user_birthdate
    
    if st.button(f"강사님 추천받기! {random.choice(emojis)}"):
        st.markdown("---")
        st.write(f"✨ 짜잔! **{st.session_state.name}**을 위한 강사님 추천 결과야! {random.choice(emojis)}")

        # 찐! 강사님 추천 로직 (예시 데이터)
        # 실제로는 여기서 방대한 강사 데이터베이스와 복잡한 추천 알고리즘이 필요하겠지만,
        # 여기선 예시로 간단하게 구현할게! 😜
        # 🔥 영어 강사님 데이터 추가! 🔥
        teachers_data = {
            "EBS": {
                "국어": ["윤혜정 선생님", "최은우 선생님", "김철회 선생님"],
                "수학": ["정승제 선생님", "이지원 선생님", "심주석 선생님"],
                "사탐": ["최태성 선생님", "이용희 선생님", "최명희 선생님"],
                "영어": ["주혜연 선생님", "이수련 선생님", "정대식 선생님"] # 영어 강사님 추가!
            },
            "이투스": {
                "국어": ["김민정 선생님", "김상훈 선생님", "강윤구 선생님"],
                "수학": ["정승제 선생님", "신승범 선생님", "한석원 선생님"],
                "사탐": ["이지영 선생님", "김성묵 선생님", "최진기 선생님"],
                "영어": ["주혜연 선생님", "심우철 선생님", "강원우 선생님"] # 영어 강사님 추가!
            },
            "메가스터디": {
                "국어": ["유대종 선생님", "김동욱 선생님", "강민철 선생님"],
                "수학": ["현우진 선생님", "김성은 선생님", "양승진 선생님"],
                "사탐": ["이다지 선생님", "조정식 선생님", "윤성훈 선생님"],
                "영어": ["조정식 선생님", "김동영 선생님", "김기철 선생님"] # 영어 강사님 추가!
            },
            "대성마이맥": {
                "국어": ["박광일 선생님", "김승리 선생님", "김찬호 선생님"],
                "수학": ["한석원 선생님", "정병호 선생님", "이창무 선생님"],
                "사탐": ["임정환 선생님", "윤리 이승헌 선생님", "박선 선생님"],
                "영어": ["이명학 선생님", "김찬휘 선생님", "은선진 선생님"] # 영어 강사님 추가!
            }
        }

        recommended_teacher_list = teachers_data.get(st.session_state.recommended_institute, {}).get(st.session_state.subject, ["아직 강사 정보가 없어 ㅠㅠ"])
        
        # 생년월일의 일(day)을 활용해서 픽하는 척 해보자!
        if user_birthdate and recommended_teacher_list:
            day_of_birth = user_birthdate.day
            teacher_index = (day_of_birth % len(recommended_teacher_list)) # 출생일에 따라 고르는 척!
            final_teacher = recommended_teacher_list[teacher_index]
        elif recommended_teacher_list:
            final_teacher = random.choice(recommended_teacher_list) # 생년월일 없으면 랜덤
        else:
            final_teacher = "아쉽게도 추천할 강사님이 없네요. 😅 다른 과목이나 사이트를 선택해보세요!"

        st.subheader(f"✨ **{st.session_state.recommended_institute}**에서 **{st.session_state.subject}** 과목의 {final_teacher}을(를) 추천합니다! {random.choice(emojis)}")
        st.success(f"생년월일({user_birthdate})까지 고려한 최고의 픽이야! 👍 열공해서 원하는 목표 꼭 이루길 바랄게! 🚀")
        st.balloons() # 축하 풍선 팡팡!

        st.markdown(f"궁금한 점 있으면 또 물어봐! {random.choice(emojis)} {random.choice(emojis)}")

else:
    st.info(f"이름을 입력하면 인강 사이트 추천이 시작돼! {random.choice(emojis)}")

st.markdown("---")
st.caption("© 2025 너만의 인강 강사 추천 앱! 💻💕")
