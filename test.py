# ✨🌟💫⭐️🌠🌌 이거 만드느라 내 눈에서 레이저 나옴! 💥
# 아직 Streamlit 설치 안 됐으면 무조건 이거부터 외쳐!
# pip install streamlit
# (이미 되어 있다면 광속으로 패스!)

import streamlit as st # 덕질 앱의 심장! Streamlit!
import hashlib # 같은 이름엔 같은 아이돌 나오게 하는 마법 도구! (공평한 덕질을 위해!)
import datetime # 생년월일 처리용!
import random # 일치하는 멤버 없을 때 랜덤 추천!

# --- 💖 핵심 데이터: 아이돌 그룹 & 멤버 정보 (이모티콘 과다 심음!) 💖 ---
# 각 그룹별 멤버 이름과 생년월일(월, 일만) 정보를 딕셔너리로 저장!
# (정보가 부족한 경우 임의로 기입된 날짜가 있을 수 있으니 양해 부탁드립니다! 😭)
IDOL_DATA = [
    {
        "name": "방탄소년단 (BTS) 💜", "emoji": "💜",
        "group_desc": f"💜 당신의 운명은 바로 **글로벌 슈퍼스타 방탄소년단!** 🚀🚀🚀 퍼포먼스 장인에 가사까지 심금을 울리는 갓티에스! 🥺 멤버 한 명 한 명 매력 폭발이라 덕질 포인트가 끝도 없을 거예요! 💖 보라해! 💜💜💜💜💜",
        "members": [
            {"name": "RM", "birth_month": 9, "birth_day": 12}, # 1994년 9월 12일
            {"name": "진", "birth_month": 12, "birth_day": 4}, # 1992년 12월 4일
            {"name": "슈가", "birth_month": 3, "birth_day": 9}, # 1993년 3월 9일
            {"name": "제이홉", "birth_month": 2, "birth_day": 18}, # 1994년 2월 18일
            {"name": "지민", "birth_month": 10, "birth_day": 13}, # 1995년 10월 13일
            {"name": "뷔", "birth_month": 12, "birth_day": 30}, # 1995년 12월 30일
            {"name": "정국", "birth_month": 9, "birth_day": 1}, # 1997년 9월 1일
        ]
    },
    {
        "name": "블랙핑크 (BLACKPINK) 🖤💖", "emoji": "🖤💖",
        "group_desc": f"🖤💖 당신의 운명은 바로 **월드 클래스 걸크러쉬 블랙핑크!** ✨✨✨ 독보적인 아우라에 힙함이 뚝뚝! 무대 한 번 보면 그냥 입덕 확정! 👑 비주얼, 실력 다 가진 언니들 매력에 빠져보세요! 🎧🖤💖",
        "members": [
            {"name": "지수", "birth_month": 1, "birth_day": 3}, # 1995년 1월 3일
            {"name": "제니", "birth_month": 1, "birth_day": 16}, # 1996년 1월 16일
            {"name": "로제", "birth_month": 2, "birth_day": 11}, # 1997년 2월 11일
            {"name": "리사", "birth_month": 3, "birth_day": 27}, # 1997년 3월 27일
        ]
    },
    {
        "name": "세븐틴 (SEVENTEEN) 💎", "emoji": "💎",
        "group_desc": f"💎 당신의 운명은 바로 **자체 제작 아이돌 세븐틴!** 🕺🕺🕺 무대 장인에 떼창 유발하는 명곡들까지! 🎤 열세 명의 매력덩어리들 때문에 심장이 남아나질 않을 거예요! ✨ 입덕하는 순간 캐럿봉 흔들 준비 완료! 💎💎💎💎💎",
        "members": [
            {"name": "에스쿱스", "birth_month": 8, "birth_day": 8},
            {"name": "정한", "birth_month": 10, "birth_day": 4},
            {"name": "조슈아", "birth_month": 12, "birth_day": 30},
            {"name": "준", "birth_month": 6, "birth_day": 10},
            {"name": "호시", "birth_month": 6, "birth_day": 15},
            {"name": "원우", "birth_month": 7, "birth_day": 17},
            {"name": "우지", "birth_month": 11, "birth_day": 22},
            {"name": "디에잇", "birth_month": 11, "birth_day": 7},
            {"name": "민규", "birth_month": 4, "birth_day": 6},
            {"name": "도겸", "birth_month": 2, "birth_day": 18},
            {"name": "승관", "birth_month": 1, "birth_day": 16},
            {"name": "버논", "birth_month": 2, "birth_day": 18},
            {"name": "디노", "birth_month": 2, "birth_day": 11},
        ]
    },
    {
        "name": "뉴진스 (NewJeans) 👖🐰", "emoji": "👖",
        "group_desc": f"👖 당신의 운명은 바로 **대세 of 대세 뉴진스!** 🐰🐰🐰 Y2K 감성 뿜뿜에 청량함까지! 🎧 노래 한번 들으면 헤어나올 수 없을 거예요! 🎶 멤버들마다 매력이 넘쳐 흘러서 덕질 계정 필수 각! 🌈👖",
        "members": [
            {"name": "민지", "birth_month": 5, "birth_day": 7}, # 2004년 5월 7일
            {"name": "하니", "birth_month": 10, "birth_day": 6}, # 2004년 10월 6일
            {"name": "다니엘", "birth_month": 4, "birth_day": 11}, # 2005년 4월 11일
            {"name": "해린", "birth_month": 5, "birth_day": 15}, # 2006년 5월 15일
            {"name": "혜인", "birth_month": 4, "birth_day": 21}, # 2008년 4월 21일
        ]
    },
    {
        "name": "스트레이 키즈 (Stray Kids) ⚡️", "emoji": "⚡️",
        "group_desc": f"⚡️ 당신의 운명은 바로 **마라맛 퍼포먼스 스트레이 키즈!** 🐺🐺🐺 파워풀한 무대 장악력에 직접 만드는 음악까지! 💥 에너제틱한 스키즈 매력에 빠지면 답 없다! 진짜 없다! 💥 K-POP 최강자 스키즈 매력에 빠져보세요! 🤩⚡️",
        "members": [
            {"name": "방찬", "birth_month": 10, "birth_day": 3},
            {"name": "리노", "birth_month": 10, "birth_day": 25},
            {"name": "창빈", "birth_month": 8, "birth_day": 11},
            {"name": "현진", "birth_month": 3, "birth_day": 20},
            {"name": "한", "birth_month": 9, "birth_day": 14},
            {"name": "필릭스", "birth_month": 9, "birth_day": 15},
            {"name": "승민", "birth_month": 9, "birth_day": 22},
            {"name": "아이엔", "birth_month": 2, "birth_day": 8},
        ]
    },
    {
        "name": "IVE (아이브) 👑", "emoji": "👑",
        "group_desc": f"👑 당신의 운명은 바로 **Z세대의 워너비 아이브!** 🌟🌟🌟 우아하고 사랑스러운 매력으로 무대 다 씹어먹는 언니들! 💐 비주얼, 실력 다 갖춘 완벽돌! 아이브 노래 듣는 순간 당신은 이미 다이브! 🌊💖",
        "members": [
            {"name": "유진", "birth_month": 9, "birth_day": 1}, # 2003년 9월 1일
            {"name": "가을", "birth_month": 5, "birth_day": 22}, # 2002년 5월 22일
            {"name": "레이", "birth_month": 2, "birth_day": 3}, # 2004년 2월 3일
            {"name": "원영", "birth_month": 8, "birth_day": 31}, # 2004년 8월 31일
            {"name": "리즈", "birth_month": 11, "birth_day": 21}, # 2004년 11월 21일
            {"name": "이서", "birth_month": 2, "birth_day": 21}, # 2007년 2월 21일
        ]
    },
    {
        "name": "NCT 127 💚", "emoji": "💚",
        "group_desc": f"💚 당신의 운명은 바로 **서울의 심장, NCT 127!** 🌃 독보적인 음악 색깔과 파워풀한 퍼포먼스! 🎶 한 번 빠지면 출구 없는 매력에 헤어나올 수 없을 걸? 시즈니의 삶, 지금 바로 시작! 🚀💚💚💚",
        "members": [
            {"name": "태일", "birth_month": 6, "birth_day": 14}, # 1994년 6월 14일
            {"name": "쟈니", "birth_month": 2, "birth_day": 9}, # 1995년 2월 9일
            {"name": "태용", "birth_month": 7, "birth_day": 1}, # 1995년 7월 1일
            {"name": "유타", "birth_month": 10, "birth_day": 26}, # 1995년 10월 26일
            {"name": "도영", "birth_month": 2, "birth_day": 1}, # 1996년 2월 1일
            {"name": "재현", "birth_month": 2, "birth_day": 14}, # 1997년 2월 14일
            {"name": "정우", "birth_month": 2, "birth_day": 19}, # 1998년 2월 19일
            {"name": "마크", "birth_month": 8, "birth_day": 2}, # 1999년 8월 2일
            {"name": "해찬", "birth_month": 6, "birth_day": 6}, # 2000년 6월 6일
        ]
    },
    {
        "name": "NCT WISH 🌠", "emoji": "🌠",
        "group_desc": f"🌠 당신의 운명은 바로 **꿈을 향해 달려가는 NCT WISH!** 🌟 청량하고 순수한 매력으로 덕심 제대로 저격! 💫 희망찬 에너지 가득한 무대에 홀딱 반할 거야! 위시와 함께하는 행복한 덕질 라이프! 💖🌠",
        "members": [
            {"name": "시온", "birth_month": 5, "birth_day": 11}, # 2002년 5월 11일
            {"name": "리쿠", "birth_month": 6, "birth_day": 28}, # 2003년 6월 28일
            {"name": "유우시", "birth_month": 4, "birth_day": 5}, # 2004년 4월 5일
            {"name": "재희", "birth_month": 6, "birth_day": 21}, # 2005년 6월 21일
            {"name": "료", "birth_month": 8, "birth_day": 4}, # 2007년 8월 4일
            {"name": "사쿠야", "birth_month": 11, "birth_day": 18}, # 2007년 11월 18일
        ]
    },
    {
        "name": "올데이 프로젝트 (ALLDAY PROJECT) ☀️", "emoji": "☀️",
        "group_desc": f"☀️ 당신의 운명은 바로 **새로운 시작, 올데이 프로젝트!** 🌅 신선하고 독특한 컨셉으로 K-POP 판을 뒤흔들 뉴 페이스! 🚀 숨겨진 보석같은 매력을 발견하고 싶다면 바로 입덕! 매일매일이 기대될 걸? 🤩☀️",
        "members": [
            {"name": "애니", "birth_month": 1, "birth_day": 23}, # 2002년 1월 23일 (문서윤)
            {"name": "타잔", "birth_month": 7, "birth_day": 11}, # 임의
            {"name": "베일리", "birth_month": 8, "birth_day": 2}, # 임의
            {"name": "우찬", "birth_month": 2, "birth_day": 5}, # 2005년 2월 5일 (조우찬)
            {"name": "영서", "birth_month": 1, "birth_day": 18}, # 2005년 1월 18일 (이영서)
        ]
    },
    {
        "name": "제로베이스원 (ZEROBASEONE) 🌹", "emoji": "🌹",
        "group_desc": f"🌹 당신의 운명은 바로 **소년들의 꿈, 제로베이스원!** 💖 압도적인 비주얼과 청춘의 에너지가 넘쳐흘러! ✨ 성장돌의 표본을 보여줄 제베원에 지금 바로 탑승해! 우리원 평생 함께해! 🌟🌹",
        "members": [
            {"name": "성한빈", "birth_month": 6, "birth_day": 13}, # 2001년 6월 13일
            {"name": "김지웅", "birth_month": 11, "birth_day": 7}, # 1998년 11월 7일
            {"name": "장하오", "birth_month": 7, "birth_day": 25}, # 2000년 7월 25일
            {"name": "석매튜", "birth_month": 5, "birth_day": 28}, # 2002년 5월 28일
            {"name": "김태래", "birth_month": 7, "birth_day": 14}, # 2002년 7월 14일
            {"name": "박건욱", "birth_month": 1, "birth_day": 10}, # 2005년 1월 10일
            {"name": "한유진", "birth_month": 3, "birth_day": 20}, # 2007년 3월 20일
        ]
    },
    {
        "name": "라이즈 (RIIZE) 🌊", "emoji": "🌊",
        "group_desc": f"🌊 당신의 운명은 바로 **감각적인 힙합, 라이즈!** 🎶 트렌디한 음악과 자유분방한 매력에 풍덩 빠질 거야! 🕺 라이즈의 성장 스토리를 함께하며 새로운 경험을 쌓아가자! 🎧💙🌊",
        "members": [
            {"name": "쇼타로", "birth_month": 11, "birth_day": 25}, # 2000년 11월 25일
            {"name": "은석", "birth_month": 3, "birth_day": 19}, # 2001년 3월 19일
            {"name": "성찬", "birth_month": 9, "birth_day": 13}, # 2001년 9월 13일
            {"name": "원빈", "birth_month": 3, "birth_day": 2}, # 2002년 3월 2일
            {"name": "소희", "birth_month": 11, "birth_day": 21}, # 2003년 11월 21일
            {"name": "앤톤", "birth_month": 3, "birth_day": 21}, # 2004년 3월 21일
        ]
    },
    {
        "name": "아일릿 (ILLIT) 🌙", "emoji": "🌙",
        "group_desc": f"🌙 당신의 운명은 바로 **몽환적인 판타지, 아일릿!** 🧚‍♀️ 신비롭고 사랑스러운 매력으로 당신의 덕심을 자극할 거야! ✨ 나도 모르게 스며드는 아일릿의 세계로 떠나보자! 🚀💖🌙",
        "members": [
            {"name": "윤아", "birth_month": 1, "birth_day": 15}, # 2004년 1월 15일
            {"name": "민주", "birth_month": 5, "birth_day": 11}, # 2004년 5월 11일
            {"name": "모카", "birth_month": 10, "birth_day": 8}, # 2004년 10월 8일
            {"name": "원희", "birth_month": 6, "birth_day": 26}, # 2007년 6월 26일
            {"name": "이로하", "birth_month": 2, "birth_day": 4}, # 2008년 2월 4일
        ]
    },
]
# --- 💖 IDOL_DATA 끝! 💖 ---


def main():
    # 🌈 페이지 설정부터 이미 오타쿠 심장 폭격! 🌈
    st.set_page_config(
        page_title="💖 최애찾기 테스트: 너의 아이돌은?! 💖", # 브라우저 탭부터 심상치 않아!
        page_icon="✨", # 브라우저 탭 아이콘도 존예!
        layout="centered", # 화면 정중앙 배치! (내 최애를 위한 최고의 자리!)
        initial_sidebar_state="collapsed" # 사이드바는 나중에 생각! 덕질이 먼저다!
    )

    # st.session_state를 사용하여 페이지 재실행 시에도 값 유지!
    if 'recommended_group' not in st.session_state:
        st.session_state.recommended_group = None
    if 'user_name_input' not in st.session_state:
        st.session_state.user_name_input = ""
    if 'birth_date_input' not in st.session_state:
        st.session_state.birth_date_input = None # 날짜는 초기값이 오늘 날짜로 들어가는게 좋을 것 같음


    # 🤩 메인 타이틀: 시작부터 심장마비 각! 🤩
    st.title('👑 내 운명의 아이돌을 찾아줘! 💖✨')
    st.markdown("### 🤩 이름만 입력하면 덕통사고 유발 아이돌 자동 추천! 🚀") # 부제목도 핵과몰입!
    st.markdown("---") # 깔끔하게 구분선 쫙! (내 심장도 쫙!)

    # 📝 1단계: 이름 입력 필드 📝
    st.subheader('💫 1단계: 이름 입력하기 (벌써부터 행복하다! ㅠㅠ) 💫')
    st.markdown("👇 덕질의 시작은 여기서부터! 당신의 이름으로 덕메이트를 찾아보자! 👇")

    user_name = st.text_input(
        label='💖 당신의 심쿵 이름을 입력해줘! (예: 김덕후) 💖',
        placeholder='여기에 입력하고 덕질 로드 ON! 🚀',
        key="덕질이름입력칸", # 고유 키로 더 명확하게!
        value=st.session_state.user_name_input # 세션 상태 값으로 초기화
    )
    if user_name: # 이름이 입력되었을 때만 세션 상태 업데이트
        st.session_state.user_name_input = user_name

    st.markdown("---") # 또 다른 구분선 뿅! (긴장감 고조!)

    # 🚀 1단계 버튼: '최애 그룹 찾기!' 🚀
    if st.button('✨ 내 운명의 아이돌 그룹은 누구?! 지금 바로 확인! ✨'):
        if not user_name: # 이름 안 썼으면 철벽 방어!
            st.error('🚨 어... 이름을 입력 안 했잖아? 덕질은 이름부터! ㅠㅠ 얼른 써줘! 🥺🙏')
            st.session_state.recommended_group = None # 이름 없으면 그룹 추천 초기화
        else:
            # ✨ 1단계 결과: 풍선 파티 + 눈뽕 이모티콘 풀가동! ✨
            st.success(f"두구두구두구... {user_name}님의 최애 아이돌 그룹은 과연?! 🥁🥁🥁")
            st.balloons() # 풍선 팡팡! 축덕질 시작 축하! 🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈

            st.write("---") # 결과 구분선!

            # 이름으로 고유한 해시 값을 만들어서 아이돌 리스트에서 딱 한 그룹만 콕!
            name_hash = int(hashlib.md5(user_name.encode()).hexdigest(), 16)
            recommended_group = IDOL_DATA[name_hash % len(IDOL_DATA)]

            # 추천된 그룹을 세션 상태에 저장하여 다음 단계에서 활용
            st.session_state.recommended_group = recommended_group
            st.session_state.user_name_input = user_name # 현재 입력된 이름도 저장

            st.subheader(f"{recommended_group['emoji']} {user_name}님의 최애 그룹은 바로... 🤩 **{recommended_group['name']}** 입니다! {recommended_group['emoji']}")
            st.markdown(f"") # 간격 조절용!

            # 덕질 유발 그룹 설명
            st.markdown(f"##### {recommended_group['emoji']} {recommended_group['group_desc']}")

            st.markdown("---") # 덕질 그룹 결과 끝!
            st.info("🚨 1단계는 '재미'와 '덕질 유도'를 위한 것입니다! 너무 과몰입은 NO! (근데 이미 늦었을 수도? ㅋㅋ) 😉")
            st.markdown("🌈 덕질은 인생을 풍요롭게 한다! ✨ 행복한 덕질 라이프 시작해봐요! 🚀💖")
            
            # 다음 단계로 넘어가기 위해 빈 칸에 생년월일 입력창 표시
            st.markdown("### 💫 2단계: 최애 멤버 찾기 (두근두근 더 진심! 💖) 💫")
            st.write("👇 이제 당신의 생년월일을 입력하고 그룹 내 운명의 최애 멤버를 찾아보자! 👇")
            
            # 현재 연도 가져오기 (날짜 선택 시 기본값으로 설정)
            today = datetime.date.today()

            st.session_state.birth_date_input = st.date_input(
                "📅 당신의 생년월일을 선택해주세요! 📅",
                value=st.session_state.birth_date_input or today, # 세션에 저장된 값 or 오늘 날짜
                min_value=datetime.date(1950, 1, 1), # 최소값 설정 (너무 옛날은 좀...ㅎㅎ)
                max_value=today, # 오늘 날짜까지!
                key="birth_date_selector"
            )

            # 2단계 버튼: '내 운명의 최애 멤버 찾기!'
            if st.button(f"🚀 {recommended_group['name']}에서 내 운명의 최애 멤버 찾기! 💖"):
                if not st.session_state.birth_date_input:
                    st.error('🚨 으앙! 생년월일을 입력해줘야 최애 멤버를 찾아줄 수 있어! 😢')
                else:
                    # 사용자 생년월일 월/일 추출
                    user_birth_month = st.session_state.birth_date_input.month
                    user_birth_day = st.session_state.birth_date_input.day

                    found_member = None
                    # 추천된 그룹의 멤버 리스트에서 월/일이 일치하는 멤버 찾기
                    for member in recommended_group['members']:
                        if member["birth_month"] == user_birth_month and member["birth_day"] == user_birth_day:
                            found_member = member
                            break

                    # 결과 출력
                    st.success(f"두구두구두구... 당신의 운명의 최애 멤버는 과연?! 🥁🥁🥁")
                    st.balloons() # 다시 풍선 팡팡! 🎈🎈🎈

                    st.write("---")
                    if found_member:
                        st.subheader(f"💖 {st.session_state.user_name_input}님의 최애 멤버는 바로... 🤩 **{found_member['name']}** 입니다! {recommended_group['emoji']}")
                        st.markdown(f"##### ✨ **당신의 생일 ({user_birth_month}월 {user_birth_day}일)과 같은 달, 같은 날 태어난 운명의 멤버!** ✨\n\n**축하해요! 당신은 정말 선택받은 덕후! 🍀 이 멤버는 당신의 덕질 메이트가 될 운명!**")
                    else:
                        # 일치하는 멤버 없으면 그룹 멤버 중 랜덤으로 한 명 추천
                        random_member = random.choice(recommended_group['members'])
                        st.subheader(f"🤔 {st.session_state.user_name_input}님의 운명의 최애 멤버는... 🤩 **{random_member['name']}** 입니다! {recommended_group['emoji']}")
                        st.markdown(f"##### ✨ **아쉽게도 생일이 같은 멤버는 없네요! 😥 하지만 실망은 금물! 랜덤으로 뽑힌 이 멤버가 당신의 새로운 최애가 될지도?!** ✨\n\n**덕질은 원래 예측 불허의 재미! 😉**")
                    st.markdown("---")
                    st.info("⚠️ 이 멤버 추천 역시 '재미'로 보는 것입니다! 모든 멤버는 소중하니까! 😉")
                    st.markdown("💖 이제 진짜 최애와 함께하는 덕질 라이프 시작! 🚀✨")
    
    # --- 사이드바 ---
    with st.sidebar:
        st.header("✨ 덕질 팁! ✨")
        st.write("이 앱은 Streamlit으로 만들었어요! 파이썬 코드로 이렇게 재밌는 걸 만들 수 있다니! 개쩐다! 🐍")
        st.write("이름 해시 값과 생년월일로 최애를 추천해줘요! 완전 운명이지?! 💖")
        st.markdown("---")
        st.write("🎶 혹시 다음에 만들고 싶은 덕질 앱 아이디어가 있다면 언제든지 콜! 나는 항상 네 덕질 라이프를 응원해! 😜")
        st.image("https://raw.githubusercontent.com/streamlit/docs/main/docs/assets/streamlit-logo-light.svg", width=100) # Streamlit 로고도 간지나게!


# ✨ 이 부분이 있어야 파이썬 파일 실행하면 바로 Streamlit 앱이 뜨지! ✨
if __name__ == "__main__":
    main()
