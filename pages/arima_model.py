import streamlit as st
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os
from menu import menu

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

st.subheader('ARIMA 모델 시각화')
summary_data = load_summary_data()

summary_data.set_index('YEAR', inplace=True)

# 데이터 시각화
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(summary_data.index, summary_data['총계_계'], marker='o')
ax.set_title('Yearly Data')
ax.set_xlabel('Year')
ax.set_ylabel('Count')
ax.grid(True)
st.pyplot(fig)

# ARIMA 모델 피팅
model = ARIMA(summary_data['총계_계'], order=(1, 1, 1))
model_fit = model.fit()

# 요약 출력
st.write(model_fit.summary())

# 예측
forecast = model_fit.forecast(steps=5)  # 향후 5년 예측
forecast_years = [2022, 2023, 2024, 2025, 2026]
forecast_df = pd.DataFrame({'YEAR': forecast_years, 'Forecast': forecast})
forecast_df.set_index('YEAR', inplace=True)

# 예측 결과 시각화
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(summary_data.index, summary_data['총계_계'], marker='o', label='Actual')
ax.plot(forecast_df.index, forecast_df['Forecast'], marker='o', linestyle='--', color='red', label='Forecast')
ax.set_title('Yearly Data and Forecast')
ax.set_xlabel('Year')
ax.set_ylabel('Count')
ax.legend()
ax.grid(True)
st.pyplot(fig)

# Redirect to app.py if not logged in, otherwise show the navigation menu
menu()