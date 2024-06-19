import streamlit as st
import pandas as pd
import numpy as np
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_absolute_error
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os
import math
from menu import menu

# 데이터 로드
@st.cache_data
def load_data():
    data = pd.read_csv('data/data_cleaned_augmented.csv')
    return data

# 모델 학습
@st.cache_resource
def train_models():
    data = load_data()

    # Encode categorical variables
    le_sido = LabelEncoder()
    le_sigungu = LabelEncoder()

    data['시도_encoded'] = le_sido.fit_transform(data['시도'])
    data['시군구_encoded'] = le_sigungu.fit_transform(data['시군구'])

    # Define features and targets
    features = ['발생년도', '시도_encoded', '시군구_encoded']
    targets = ['전체발생량', '총계_재활용', '총계_소각', '총계_매립']
    X = data[features]
    y = data[targets]

    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train models
    models = {}
    for target in targets:
        model = xgb.XGBRegressor(objective='reg:squarederror', random_state=42)
        model.fit(X_train, y_train[target])
        models[target] = model

    return models, le_sido, le_sigungu

# Load trained models and label encoders
models, le_sido, le_sigungu = train_models()

# 데이터 로드
data = load_data()
# st.write(data)

# 한글 폰트 설정
font_path = os.path.join(os.getcwd(), "Nanum_Gothic/NanumGothic-Bold.ttf")
font_prop = fm.FontProperties(fname=font_path)
plt.rc('font', family=font_prop.get_name())
plt.rcParams['axes.unicode_minus'] = False

# 스트림릿 타이틀
st.title('시도/시군구 폐기물 발생량 예측')

sido_text = data['시도'].unique()

# Prediction function
def predict_waste(year, sido, sigungu):
    sido_encoded = le_sido.transform([sido])[0]
    sigungu_encoded = le_sigungu.transform([sigungu])[0]
    input_data = pd.DataFrame({
        '발생년도': [year],
        '시도_encoded': [sido_encoded],
        '시군구_encoded': [sigungu_encoded]
    })
    predictions = {}
    for target in models.keys():
        predictions[target] = models[target].predict(input_data)[0]
    return predictions

# User input
year = st.number_input('발생년도', min_value=2000, max_value=2050, value=2024)
selected_sido = st.selectbox('시도', options=sido_text)

# Filter sigungu based on selected sido
filtered_sigungu = data[data['시도'] == selected_sido]['시군구'].unique()
selected_sigungu = st.selectbox('시군구', options=filtered_sigungu)

# Predict button
if st.button('예측'):
    prediction_results = predict_waste(year, selected_sido, selected_sigungu)
    # 결과의 소수점 이하를 제거
    truncated_results = {key.replace('총계_', ''): int(np.floor(value)) for key, value in prediction_results.items()}
    st.write("예측 결과(단위: 톤):")
    st.table(pd.DataFrame([truncated_results]))

st.subheader('기대효과')
st.markdown("""
#### 1. 자원 효율성 및 비용 절감

#### 2. 환경 보호 및 지속 가능성 강화

#### 3. 정책 수립 및 주민 참여 촉진
""")

# Redirect to app.py if not logged in, otherwise show the navigation menu
menu()
