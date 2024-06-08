import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# 데이터 로드
@st.cache_data
def load_data():
    data = pd.read_csv('data/combined_data.csv')
    return data

# 한글 폰트 다운로드 및 설정
font_path = os.path.join(os.getcwd(), "Nanum_Gothic/NanumGothic-Bold.ttf")
font_prop = fm.FontProperties(fname=font_path)
plt.rc('font', family=font_prop.get_name())
plt.rcParams['axes.unicode_minus'] = False  # 마이너스 기호 깨짐 방지

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

# 사이드바 메뉴 상태 초기화
if 'menu' not in st.session_state:
    st.session_state.menu = '소개'

# 사이드바 메뉴
st.sidebar.title('BDAV1 메뉴')
if st.sidebar.button('소개'):
    st.session_state.menu = '소개'
if st.sidebar.button('생활 폐기물 데이터 현황'):
    st.session_state.menu = '생활 폐기물 데이터 현황'
if st.sidebar.button('폐기물 처리 방법별 발생량 추이 분석'):
    st.session_state.menu = '폐기물 처리 방법별 발생량 추이 분석'
if st.sidebar.button('지역별 비교 분석'):
    st.session_state.menu = '지역별 비교 분석'

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

    st.subheader('년도별 전국 생활 폐기물 발생량 추이')
    # '시도'가 '전국'인 데이터만 필터링
    national_data = data[data['시도'] == '전국']

    # '발생년도'와 '전체발생량'을 기준으로 그룹화하여 합계 계산
    yearly_totals = national_data.groupby('발생년도')['전체발생량'].sum().reset_index()

    # 차트 그리기
    fig, ax = plt.subplots()
    ax.bar(yearly_totals['발생년도'], yearly_totals['전체발생량'], color='skyblue', label='전체 발생량')
    ax.plot(yearly_totals['발생년도'], yearly_totals['전체발생량'], color='red', marker='o', label='추이')

    # 차트 제목 및 레이블 설정
    ax.set_title('년도별 전국 폐기물 전체 발생현황 추이', fontproperties=font_prop)
    ax.set_xlabel('년도', fontproperties=font_prop)
    ax.set_ylabel('전체 발생량 (톤)', fontproperties=font_prop)
    ax.legend(prop=font_prop)

    # 스트림릿에 차트 표시
    st.pyplot(fig)

    st.subheader('폐기물 발생량 상위 10개 시도')
    # 폐기물 발생량 상위 10개 시도 표시
    # '전국' 데이터 제외
    data = data[data['시도'] != '전국']
    top_cities_data = data.groupby('시도')['전체발생량'].sum().nlargest(10).reset_index()
    
    # 발생량에 따라 데이터를 내림차순으로 정렬
    top_cities_data = top_cities_data.sort_values(by='전체발생량', ascending=True)
    
    fig, ax = plt.subplots()
    ax.barh(top_cities_data['시도'], top_cities_data['전체발생량'], color='green')
    
    # 폰트 설정을 위한 fontdict 생성
    fontdict = {'fontsize': 12, 'fontweight': 'bold', 'fontname': font_prop.get_name()}
    
    ax.set_title('폐기물 발생량 상위 10개 시도', fontdict=fontdict)
    ax.set_ylabel('시도', fontdict=fontdict)
    ax.set_xlabel('전체 발생량 (톤)', fontdict=fontdict)
    ax.tick_params(axis='y', rotation=0)  # y축 레이블 회전
    st.pyplot(fig)

elif st.session_state.menu == '폐기물 처리 방법별 발생량 추이 분석':
    st.title('폐기물 처리 방법별 연도별 추이')
    st.write('재활용, 소각, 매립의 연도별 추이를 각각 분석하고 시각화합니다.')
    data = load_data()

    # 연도별 폐기물 처리 방법별 발생량 추이 분석
    treatment_methods = ['총계_재활용', '총계_소각', '총계_매립']
    yearly_treatment_data = data.groupby('발생년도')[treatment_methods].sum().reset_index()

    # 시각화: 연도별 폐기물 처리 방법별 발생량 추이
    fig, ax = plt.subplots()

    for method in treatment_methods:
        ax.plot(yearly_treatment_data['발생년도'], yearly_treatment_data[method], marker='o', label=method)

    ax.set_title('연도별 폐기물 처리 방법별 발생량 추이', fontproperties=font_prop)
    ax.set_xlabel('발생년도', fontproperties=font_prop)
    ax.set_ylabel('발생량 (천 톤)', fontproperties=font_prop)
    ax.legend(prop=font_prop)
    ax.grid(True)

    # 스트림릿에 차트 표시
    st.pyplot(fig)
elif st.session_state.menu == '지역별 비교 분석':
    st.title('지역별 폐기물 발생량 비교 분석')
    st.write('서울, 부산, 대구 등 주요 도시의 폐기물 발생량과 처리 방법을 비교하고 시각화해 보겠습니다.')
    data = load_data()

    # 주요 도시들의 데이터 추출
    major_cities = ['서울', '부산', '대구', '인천', '광주', '대전', '울산']
    major_cities_data = data[data['시도'].isin(major_cities)]
    treatment_methods = ['총계_재활용', '총계_소각', '총계_매립']

    # 주요 도시별 폐기물 발생량 및 처리 방법 분석
    city_treatment_data = major_cities_data.groupby(['시도', '발생년도'])[treatment_methods].sum().reset_index()

    # 시각화: 주요 도시별 폐기물 처리 방법 비교 (2014년과 2021년을 예로 들어보겠습니다.)
    fig, axes = plt.subplots(nrows=2, ncols=1, sharex=True)

    for i, year in enumerate([2014, 2021]):
        city_data_year = city_treatment_data[city_treatment_data['발생년도'] == year]
        city_data_year = city_data_year.set_index('시도')

        ax = axes[i]
        city_data_year[treatment_methods].plot(kind='bar', stacked=True, ax=ax)
        ax.set_title(f'{year}년 주요 도시별 폐기물 처리 방법 비교', fontproperties=font_prop)
        ax.set_ylabel('발생량 (천 톤)', fontproperties=font_prop)
        ax.legend(prop=font_prop)

    plt.xlabel('시도', fontproperties=font_prop)
    plt.xticks(rotation=45, fontproperties=font_prop)
    plt.tight_layout()

    # 스트림릿에 차트 표시
    st.pyplot(fig)

