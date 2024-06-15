import streamlit as st
from menu import menu

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
# Initialize st.session_state.role to None
if "role" not in st.session_state:
    st.session_state.role = None

# # Retrieve the role from Session State to initialize the widget
# st.session_state._role = st.session_state.role

# def set_role():
#     # Callback function to save the role selection to Session State
#     st.session_state.role = st.session_state._role


# # Selectbox to choose role
# st.selectbox(
#     "Select your role:",
#     [None, "user", "admin", "super-admin"],
#     key="_role",
#     on_change=set_role,
# )
menu() # Render the dynamic menu!