import streamlit as st
import pandas as pd

st.title('BDAV1 Big Data Analytics and Visualization')
st.write('Welcome to our project dashboard!')


# 데이터 로드
@st.cache_data
def load_data():
    data = pd.read_csv('data/combined_data.csv')
    return data

def main():
    st.title('데이터 익스플로러 앱')
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

if __name__ == "__main__":
    main()