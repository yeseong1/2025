# 🌳🌲🌱 이모티콘 심기 작업 준비 🌿🌴🍀
# 먼저 터미널이나 명령 프롬프트에서 'pip install streamlit' 해주는 거 잊지 마!
# (이미 했다면 패스!)

import streamlit as st # Streamlit 라이브러리 심기!
import hashlib # 이름을 해싱해서 매번 같은 나무가 나오게 할 때 쓸 거야!

def main():
    # 🌟 앱 페이지 설정: 시작부터 이모티콘 밭! 🌟
    st.set_page_config(
        page_title="🌳 나와 찰떡궁합 나무 찾기! 🌲", # 브라우저 탭 제목!
        page_icon="🍀", # 브라우저 탭 아이콘!
        layout="centered", # 웹 앱 화면을 중앙에 정렬!
        initial_sidebar_state="collapsed" # 사이드바는 일단 숨겨두자!
    )

    # 🤩 메인 타이틀: 시작부터 나무나무해! 🤩
    st.title('🌲🌳🌱 나의 나무 친구를 찾아줘! 🌿🌴🍀')
    st.markdown("### 🤩 이름만 입력하면 찰떡같은 나무를 추천해줄게! ✨")
    st.markdown("---") # 깔끔한 구분선!

    # 📝 이름 입력 필드: 여기에 당신의 아름다운 이름을! 📝
    st.subheader('💫 이름 입력하기 (두근두근) 💫')
    
    # 여기서 귀여운 글씨체 시도! (모든 글씨체는 아니지만 특정 부분에 적용!)
    # Streamlit에서 직접 폰트 파일을 불러오는 건 복잡해서, HTML+CSS를 마크다운에 심어서 임시로 해볼게!
    # 하지만 모든 시스템에 설치된 폰트만 적용되거나, 구글 폰트 연동 등 복잡해질 수 있다는 점!
    st.markdown("""
        <style>
        .custom-font-input input {
            font-family: "Nanum Pen Script", cursive; /* 예시로 나눔펜스크립트 또는 웹폰트 이름 */
            font-size: 1.5em; /* 글씨 크기 조절 */
            color: #4CAF50; /* 초록색으로! */
        }
        .cute-text {
            font-family: "Gothic A1", sans-serif; /* 다른 예시 폰트 */
            font-size: 1.2em;
            color: #6a0dad; /* 보라색으로! */
            font-weight: bold;
        }
        </style>
        """, unsafe_allow_html=True) # HTML 허용!

    user_name = st.text_input(
        label='💚 당신의 소중한 이름을 입력해주세요! 💚',
        placeholder='예: 초록이 🌲 / 이름에 따라 운명이 바뀔 수도...? 🤔',
        key="name_input" # HTML 커스텀 폰트를 위한 고유 키
    )

    st.markdown("---") # 또 다른 구분선!

    # 🚀 '나의 나무 찾기' 버튼: 신나는 발견의 순간! 🚀
    if st.button('🌱 나의 나무 친구 찾기! 🌳'):
        if not user_name: # 이름이 입력 안 됐으면 경고!
            st.error('앗! 이름을 입력해야 나무 친구를 찾아줄 수 있어! 😢 빨리 입력해줘! 🥺')
        else:
            # ✨ 결과 출력 섹션: 풍선 파티 + 눈뽕 이모티콘! ✨
            st.success(f"두구두구... {user_name}님과 찰떡궁합 나무는 과연?! 💫")
            st.balloons() # 풍선 팡팡! 축하해주는 느낌! 🎈🎈🎈

            st.write("---") # 결과 구분선!

            # 🌳 나무 리스트와 성격/특징 (이모티콘 과다 투입!) 🌴
            trees = [
                {"name": "느티나무 🌳", "emoji": "🌳", "desc": f"{user_name}님은 🌳 듬직하고 포근한 느티나무같아요! 🌳 항상 그 자리를 지키며 모두에게 시원한 그늘과 쉼터를 제공하죠. 🌳 친구나 가족들에게 늘 안정감을 주는 든든한 존재예요! 🌳 따뜻한 마음과 인내심이 깊어서 주변 사람들이 기댈 수 있는 큰 나무랍니다! 🌳"},
                {"name": "소나무 🌲", "emoji": "🌲", "desc": f"{user_name}님은 🌲 푸른 기상과 강인함을 지닌 소나무같아요! 🌲 어떤 어려움 속에서도 굴하지 않고 꿋꿋하게 자신의 길을 가죠. 🌲 절개와 의리가 뛰어나서 한번 인연을 맺으면 평생 가는 스타일! 🌲 주변에 긍정적인 에너지를 주는 멋진 솔잎향 가득한 사람이에요! 🌲"},
                {"name": "벚나무 🌸", "emoji": "🌸", "desc": f"{user_name}님은 🌸 화려하고 아름다운 벚나무같아요! 🌸 잠깐이라도 눈을 뗄 수 없는 매력을 지녔고, 사람들에게 기쁨과 행복을 선사하죠. 🌸 로맨틱하고 감수성이 풍부해서 작은 것에도 크게 감동받는답니다. 🌸 당신이 있는 곳은 언제나 축제 분위기! 🌸"},
                {"name": "대나무 🎋", "emoji": "🎋", "desc": f"{user_name}님은 🎋 곧고 유연한 대나무같아요! 🎋 어떤 상황에도 흔들리지 않는 굳은 의지를 가졌지만, 바람처럼 부드럽게 대처할 줄 아는 지혜도 있죠. 🎋 겸손하고 지혜로워서 많은 이들에게 존경을 받는답니다. 🎋 빠르게 성장하는 당신의 미래가 기대돼요! 🎋"},
                {"name": "버드나무 🍃", "emoji": "🍃", "desc": f"{user_name}님은 🍃 부드러운 선율의 버드나무같아요! 🍃 섬세하고 유연한 사고방식을 가졌으며, 주변의 변화에 잘 적응하죠. 🍃 온화하고 차분한 성격으로 누구에게나 편안함을 주는 매력이 있어요. 🍃 때로는 의외의 강단있는 모습으로 모두를 놀라게 한답니다! 🍃"},
                {"name": "야자수 🌴", "emoji": "🌴", "desc": f"{user_name}님은 🌴 활기차고 여유로운 야자수같아요! 🌴 에너지가 넘치고 자유로운 영혼의 소유자죠. 🌴 어떤 환경에서도 긍정적인 태도를 잃지 않으며, 사람들에게 즐거움을 주는 분위기 메이커예요. 🌴 당신과 함께라면 언제나 휴가 온 기분! 🌴"},
                {"name": "은행나무 🍂", "emoji": "🍂", "desc": f"{user_name}님은 🍂 찬란하고 웅장한 은행나무같아요! 🍂 시간이 지날수록 더욱 깊어지는 매력을 지녔고, 자신만의 확고한 신념이 있죠. 🍂 지혜롭고 현명해서 어떤 고민이든 잘 들어주고 현명한 조언을 해준답니다. 🍂 황금빛 미래가 당신을 기다리고 있어요! 🍂"},
            ]

            # 이름으로 고유한 해시 값 생성 (매번 같은 이름에 같은 나무가 나오게!)
            # 이걸 랜덤으로 하면 매번 바뀔 수 있어서 해시를 쓰는 게 좀 더 '정확한 궁합'처럼 느껴질 거야!
            name_hash = int(hashlib.md5(user_name.encode()).hexdigest(), 16)
            
            # 해시 값을 이용해서 나무 리스트에서 하나의 나무를 선택
            recommended_tree = trees[name_hash % len(trees)]

            st.subheader(f"{recommended_tree['emoji']} {user_name}님과 찰떡인 나무는 바로... 🤩 **{recommended_tree['name']}** 입니다! {recommended_tree['emoji']}")
            st.markdown(f"") # 간격 조절용!
            
            # 추천 나무에 대한 자세한 설명
            st.markdown(f"##### {recommended_tree['emoji']} {recommended_tree['desc']}")
            
            st.markdown("---") # 마무리 구분선!
            st.info("🚨 이 추천은 '재미'와 '힐링'을 위한 것입니다! 너무 진지하게 생각하지 말아요! 😉")
            st.markdown("💖 세상 모든 나무들처럼, 당신도 고유하고 아름다운 존재랍니다! 💖")

    # 💡 사이드바에도 이모티콘 파티! 💡
    with st.sidebar:
        st.header("✨ 더 알아보기! ✨")
        st.write("이 앱은 Streamlit과 파이썬으로 만들었어요! 🐍")
        st.write("이름을 해싱(Hashing)해서 매번 같은 나무가 나오게 했답니다! 신기하죠? 😮")
        st.markdown("---")
        st.write("🌿 다음엔 어떤 앱을 만들어볼까? 아이디어를 마구마구 줘! 🍄")
        st.image("https://raw.githubusercontent.com/streamlit/docs/main/docs/assets/streamlit-logo-light.svg", width=100) # Streamlit 로고 이미지


# 파이썬 파일을 실행하면 Streamlit 앱이 실행되게 하는 부분!
if __name__ == "__main__":
    main()
