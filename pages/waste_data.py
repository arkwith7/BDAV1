import streamlit as st
from streamlit import components
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os
from menu import menu


# 데이터 로드
@st.cache_data
def load_data():
    data = pd.read_csv('data/combined_data.csv')
    return data

# 데이터 로드
@st.cache_data
def load_summary_data():
    data = pd.read_csv('data/연도별전국폐기물총계.csv')
    return data

# 한글 폰트 다운로드 및 설정
font_path = os.path.join(os.getcwd(), "Nanum_Gothic/NanumGothic-Bold.ttf")
font_prop = fm.FontProperties(fname=font_path)
plt.rc('font', family=font_prop.get_name())
plt.rcParams['axes.unicode_minus'] = False  # 마이너스 기호 깨짐 방지

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
summary_data = load_summary_data()


# 차트 그리기
fig, ax = plt.subplots()
# 막대그래프
ax.bar(summary_data['YEAR'], summary_data['총계_계'], color='skyblue', label='Total Generated (tons)', alpha=0.7)

# 꺾은선그래프
ax.plot(summary_data['YEAR'], summary_data['총계_계'], color='r', marker='o', label='Total Generated (tons)')

# 제목과 레이블 추가
ax.set_title('Total Waste Generated in Korea (2014-2021)')
ax.set_xlabel('Year')
ax.set_ylabel('Total Waste Generated (tons)')
ax.legend(prop=font_prop)

# # '발생년도'와 '전체발생량'을 기준으로 그룹화하여 합계 계산
# yearly_totals = national_data.groupby('발생년도')['전체발생량'].sum().reset_index()

# # 차트 그리기
# fig, ax = plt.subplots()
# ax.bar(yearly_totals['발생년도'], yearly_totals['전체발생량'], color='skyblue', label='전체 발생량')
# ax.plot(yearly_totals['발생년도'], yearly_totals['전체발생량'], color='red', marker='o', label='추이')

# # 차트 제목 및 레이블 설정
# ax.set_title('년도별 전국 폐기물 전체 발생현황 추이', fontproperties=font_prop)
# ax.set_xlabel('년도', fontproperties=font_prop)
# ax.set_ylabel('전체 발생량 (톤)', fontproperties=font_prop)
# ax.legend(prop=font_prop)

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
    
# 폰트 설정을 위한 fontproperties 사용
ax.set_title('폐기물 발생량 상위 10개 시도', fontproperties=font_prop)
ax.set_ylabel('시도', fontproperties=font_prop)
ax.set_xlabel('전체 발생량 (톤)', fontproperties=font_prop)
# y축 tick labels에 폰트 적용
ax.set_yticklabels(top_cities_data['시도'], fontproperties=font_prop)

ax.tick_params(axis='y', rotation=90)  # y축 레이블 회전

st.pyplot(fig)

# Redirect to app.py if not logged in, otherwise show the navigation menu
menu()