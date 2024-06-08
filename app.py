import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 데이터 로드
@st.cache_data
def load_data():
    data = pd.read_csv('data/combined_data.csv')
    return data

# CSS 스타일 추가
st.markdown("""
<style>
.sidebar .button {  # 스트림릿 사이드바 내 버튼 스타일 지정
    display: block;
    width: 100%;
    margin: 1px 0;
    color: white;
    background-color: #008CBA;  # 버튼 배경색
    border: none;  # 초기 상태에서 테두리 없음
    padding: 10px 15px;  # 버튼 패딩
    transition: all 0.3s ease;  # 모든 변화에 애니메이션 적용
}

.sidebar .button:hover {  # 버튼에 마우스 오버 시
    border: 2px solid #ffffff;  # 흰색 테두리 표시
}
</style>
""", unsafe_allow_html=True)

# 폰트 경로 설정
font_path = '/usr/share/fonts/truetype/nanum/NanumBarunGothic.ttf'

# 폰트 설정
plt.rcParams['font.family'] = 'NanumBarunGothic'
plt.rcParams['axes.unicode_minus'] = False  # 마이너스 기호 깨짐 방지


# 사이드바 메뉴 상태 초기화
if 'menu' not in st.session_state:
    st.session_state.menu = '소개'

# 사이드바 메뉴
st.sidebar.title('BDAV1 메뉴')
if st.sidebar.button('소개'):
    st.session_state.menu = '소개'
if st.sidebar.button('생활 폐기물 데이터 현황'):
    st.session_state.menu = '생활 폐기물 데이터 현황'

# 선택된 메뉴에 따라 컨텐츠 표시
if st.session_state.menu == '소개':
    st.title('BDAV1 Big Data Analytics and Visualization')
    st.write('Welcome to our project dashboard!')

    st.header('생활 폐기물 배출량 예측 프로그램')

    st.subheader('추진 배경 및 목적')
    st.write('''
    - 공공데이터, 카드사 데이터를 통해 전국에서 발생하는 생활 폐기물 데이터를 수집하여 
      생활 폐기물 배출량 실태를 조사하고자 함   
    - 국내에 어디에서 생활폐기물이 가장 많이 발생하는지 데이터를 파악하여
      환경관련 비즈니스를 하는 기업체에 제공하고자 함
    ''')

    st.subheader('데이터 수집')
    st.write('''
    - 공공데이터, BC카드 데이터, 환경통계정보
    ''')

    st.subheader('목표')
    st.write('''
    - 비즈니스 인사이트 제안
    - 환경관련 공모전 출전
    ''')
elif st.session_state.menu == '생활 폐기물 데이터 현황':
    st.title('전국 생활 폐기물 발생 현황')
    data = load_data()

    if st.checkbox('데이터 보기'):
        st.write(data)

    # 간단한 데이터 요약 보기
    if st.button('데이터 요약'):
        st.write(data.describe())

    # 특정 컬럼 선택하여 보기
    if st.checkbox('특정 컬럼 보기'):
        selected_columns = st.multiselect('컬럼을 선택하세요.', data.columns)
        if selected_columns:
            selected_data = data[selected_columns]
            st.dataframe(selected_data)

    # '시도'가 '전국'인 데이터만 필터링
    national_data = data[data['시도'] == '전국']

    # '발생년도'와 '전체발생량'을 기준으로 그룹화하여 합계 계산
    yearly_totals = national_data.groupby('발생년도')['전체발생량'].sum().reset_index()

    # 차트 그리기
    fig, ax = plt.subplots()
    ax.bar(yearly_totals['발생년도'], yearly_totals['전체발생량'], color='skyblue', label='전체 발생량')
    ax.plot(yearly_totals['발생년도'], yearly_totals['전체발생량'], color='red', marker='o', label='추이')

    # 차트 제목 및 레이블 설정
    ax.set_title('년도별 전국 폐기물 전체 발생현황 추이')
    ax.set_xlabel('년도')
    ax.set_ylabel('전체 발생량 (톤)')
    ax.legend()

    # 스트림릿에 차트 표시
    st.pyplot(fig)