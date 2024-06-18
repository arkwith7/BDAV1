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
st.subheader('기대효과')
st.markdown("""
#### 1. 자원 효율성 및 비용 절감
- **자원 관리 최적화**: 예측 데이터를 바탕으로 폐기물 처리 자원을 효율적으로 배치하고 활용할 수 있습니다. 재활용 시설, 소각장, 매립지의 용량을 사전에 예측하여 과부하를 방지하고 자원의 낭비를 줄일 수 있습니다.
- **비용 절감**: 폐기물 처리 비용을 사전에 예측하고 효율적인 예산을 편성함으로써 불필요한 지출을 줄일 수 있습니다. 특히, 처리 용량을 초과하는 경우 긴급 조치를 취해야 하는 비용을 줄일 수 있습니다.

#### 2. 환경 보호 및 지속 가능성 강화
- **환경 오염 방지**: 폐기물 발생량을 사전에 예측함으로써 환경 오염을 줄일 수 있습니다. 재활용을 극대화하고 소각 및 매립을 최소화함으로써 대기, 토양, 수질 오염을 방지할 수 있습니다.
- **지속 가능한 폐기물 관리**: 예측 데이터를 활용하여 지속 가능한 폐기물 관리 정책을 수립할 수 있습니다. 예를 들어, 재활용 가능 자원을 효율적으로 분리 수거하고, 매립지의 수명을 연장할 수 있는 방안을 마련할 수 있습니다.

#### 3. 정책 수립 및 주민 참여 촉진
- **정책 수립의 정확성 향상**: 지자체는 예측 데이터를 바탕으로 보다 정확한 폐기물 관리 정책을 수립할 수 있습니다. 이는 정책의 실효성을 높이고, 환경 목표 달성에 기여할 수 있습니다.
- **주민 참여 촉진**: 예측 데이터를 공개하고 주민들에게 정보를 제공함으로써, 주민들의 폐기물 관리 참여를 유도할 수 있습니다. 예를 들어, 재활용의 중요성을 강조하고, 올바른 폐기물 분리배출 방법을 교육할 수 있습니다.
- **지자체 협력 강화**: 시도 및 시군구별 데이터를 공유함으로써 지자체 간 협력을 강화할 수 있습니다. 특히, 인접 지자체 간의 폐기물 관리 협력체계를 구축하고, 공동 대처 방안을 마련할 수 있습니다.
""")
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