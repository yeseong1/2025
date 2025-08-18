# ⭐️ 중요! Streamlit이 설치 안 되어 있다면 터미널에 이걸 입력해줘!
# pip install streamlit
# (이미 설치했다면 바로 다음 단계로 고고!)

import streamlit as st # Streamlit 라이브러리 불러오기
import random # 궁합 점수랑 멘트 랜덤하게 뽑을 때 쓸 거야!

def main():
    # 🌈 페이지 설정부터 심쿵하게! 🌈
    st.set_page_config(
        page_title="💖 두근두근! 이름 궁합 테스트! 💖", # 브라우저 탭 제목!
        page_icon="💘", # 브라우저 탭 아이콘!
        layout="centered", # 웹 앱 화면 가운데 정렬!
        initial_sidebar_state="collapsed" # 사이드바는 기본으로 접어 놓기! (심플하게!)
    )

    st.title('💖 두근두근! 이름 궁합 테스트! 💘') # 메인 타이틀부터 러블리하게!
    st.markdown("### 😊 당신과 상대방의 이름으로 알아보는 꿀케미 지수! 🥳") # 부제목도 완전 귀엽게!
    st.markdown("---") # 깔끔하게 구분선 하나 뿅!

    # 📝 이름 입력 섹션 📝
    st.subheader('📝 이름 입력하기')
    st.write('👇 재미로 보는 궁합이니까, 가볍게 즐겨줘! 👇')

    # 내 이름 입력 필드
    my_name = st.text_input(
        '👤 내 이름 (예: 김아름)',
        placeholder='여기에 당신의 이름을 입력해줘!' # 입력 전 힌트 메시지
    )

    # 상대방 이름 입력 필드
    your_name = st.text_input(
        '👩‍❤️‍👨 상대방 이름 (예: 박지훈)',
        placeholder='여기에 상대방 이름을 입력해줘!' # 입력 전 힌트 메시지
    )

    st.markdown("---") # 구분선 또 뿅!

    # 🔮 궁합 결과 보기 버튼 🔮
    if st.button('✨ 궁합 결과 보기! ✨'):
        # 이름 입력 안 했을 때 경고 메시지!
        if not my_name or not your_name: # 둘 중 하나라도 비어있으면!
            st.error('😥 흑... 이름 두 개 다 입력해줘야 궁합을 봐줄 수 있어! 부탁해! 🙏')
        else:
            # 💖 궁합 점수 계산 (feat. 랜덤)! 💖
            # 0에서 100 사이의 랜덤 점수 생성 (재미용!)
            compatibility_score = random.randint(0, 100)

            # 멘트 풀 (점수에 따라 다른 멘트 보여줄 거야!)
            if compatibility_score >= 90:
                ment_pool = [
                    f"세상에... {my_name}님과 {your_name}님은 천생연분 짝꿍! 💖 심장이 쿵! 운명인가봐! 🤩",
                    "이 궁합 실화냐? 💯 이 정도면 소울메이트 아니겠어? 찐친, 찐사랑 예약! 💫",
                    "두 분의 궁합은 우주가 인정한 케미! 뭘 해도 척하면 척! 핵꿀조합! ✨"
                ]
            elif compatibility_score >= 70:
                ment_pool = [
                    f"{my_name}님과 {your_name}님은 환상의 짝꿍! 🥳 앞으로 더 좋은 일만 가득할 거야! 힘내! 💪",
                    "오! 꽤 괜찮은 궁합인데? 노력하면 더 좋은 사이가 될 수 있을 거야! 응원할게! 🙌",
                    "서로에게 좋은 영향을 주는 사이! 조금만 더 가까워지면 완전 베프각! 👯‍♀️"
                ]
            elif compatibility_score >= 40:
                ment_pool = [
                    f"{my_name}님과 {your_name}님은 알아가면 알아갈수록 매력 터지는 사이! 🍀 조금만 더 노력해볼까? 😊",
                    "음... 😅 아직은 조금 서먹해도 괜찮아! 서로 다른 점이 매력 포인트가 될 수 있지! 개성을 존중해줘! 🤝",
                    "이런 궁합도 저런 궁합도 다 있는 법! 너무 상심하지 마! 인연은 만들어가는 거야! 🌱"
                ]
            else:
                ment_pool = [
                    f"아... {my_name}님과 {your_name}님... 이것은 시련인가? 🤔 농담이야! 서로 이해하면 돼! 😜",
                    "이번 생은... 쿨한 비즈니스 관계? 🤣 재미로 보는 거니까 진지 노노! 다음 기회에? 😅",
                    "아직 서로를 덜 알아봐서 그래! 더 많은 이야기를 나누면 분명 좋아질 거야! 😊"
                ]
            
            # 멘트 중에서 랜덤으로 하나 뽑기
            chosen_ment = random.choice(ment_pool)

            # 🎉 결과 출력 섹션 🎉
            st.success(f"💖 {my_name}님과 {your_name}님의 궁합 결과! 💖")
            st.balloons() # 풍선 팡팡! 축하해주는 느낌! 🎈

            st.write("---") # 또 구분선!
            st.subheader(f"✨ 궁합 점수: {compatibility_score}점! ✨")
            st.write(chosen_ment) # 위에서 뽑은 멘트 출력!
            
            st.markdown("---") # 깔끔하게 마무리!
            st.info("⚠️ 이 궁합 테스트는 '재미'로 보는 심심풀이입니다! 결과에 너무 일희일비하지 마세요! 🤣")
            st.markdown("😉 인연은 만들고 가꿔가는 거지, 정해져 있는 게 아니잖아? 사랑해! 응원할게! 💖")

    # 💡 사이드바에 추가 메시지! 💡
    with st.sidebar:
        st.header("✨ 개발자 노트 ✨")
        st.write("이 앱은 Streamlit을 활용하여 파이썬으로 만들었어! 코딩은 생각보다 쉽고 재밌다구! 😉")
        st.write("궁금한 점 있으면 언제든지 물어봐줘! 🧑‍💻")
        st.image("https://raw.githubusercontent.com/streamlit/docs/main/docs/assets/streamlit-logo-light.svg", width=100) # Streamlit 로고 이미지 (선택사항)


# 이 부분이 있어야 파이썬 파일 실행할 때 Streamlit 앱이 짠! 하고 실행됨!
if __name__ == "__main__":
    main()
