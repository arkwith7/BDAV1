import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os
from menu import menu

# 데이터 로드
@st.cache_data
def load_summary_data():
    data = pd.read_csv('data/data_cleaned_augmented.csv')
    return data

# 데이터 로드
data = load_summary_data()

# 한글 폰트 설정
font_path = os.path.join(os.getcwd(), "Nanum_Gothic/NanumGothic-Bold.ttf")
font_prop = fm.FontProperties(fname=font_path)
plt.rc('font', family=font_prop.get_name())
plt.rcParams['axes.unicode_minus'] = False  # 마이너스 기호 깨짐 방지

# 스트림릿 타이틀
st.title('폐기물 발생량 예측 모델 생성')

st.markdown("""
            
**모델 초기화:** 
 - 세 가지 모델 (LinearRegression, RandomForestRegressor, XGBRegressor)을 딕셔너리에 저장
 - 이를 통해 반복문을 사용하여 각 모델을 동일한 방식으로 학습 및 평가.
            
**모델 학습 및 평가:**
 - 각 모델에 대해 모든 타겟 변수 (targets)에 대해 학습을 수행하고, 테스트 데이터에 대한 예측을 생성한 후, 평균 절대 오차 (MAE)를 계산.
            
#### 모델 성능 비교
1. 전체발생량 (MAE)
- Linear Regression: 141.87
- Random Forest: 141.93
- XGBoost: 140.63
            
XGBoost 모델이 전체발생량 예측에서 가장 낮은 MAE를 보여주며, 가장 좋은 성능을 나타냄.
            
2. 총계_재활용 (MAE)
- Linear Regression: 93.91
- Random Forest: 93.93
- XGBoost: 93.30
            
여기에서도 XGBoost가 가장 낮은 MAE를 기록하며, 가장 정확한 예측을 제공.
            
3. 총계_소각 (MAE)
- Linear Regression: 44.35
- Random Forest: 44.56
- XGBoost: 44.09
            
소각량 예측에서도 XGBoost가 가장 우수한 성능을 보임.
            
4. 총계_매립 (MAE)
- Linear Regression: 24.41
- Random Forest: 24.73
- XGBoost: 24.39
            
매립량 예측에서는 XGBoost와 Linear Regression의 성능이 비슷하지만, XGBoost가 약간 더 낮은 MAE를 보여줌.
            
#### 종합 평가
XGBoost 모델이 모든 지표에서 가장 낮은 MAE 값을 보여주며, 전반적으로 가장 우수한 성능을 나타냄. 
이는 XGBoost가 복잡한 비선형 관계와 다양한 데이터 패턴을 잘 처리할 수 있기 때문일 수 있습니다.
Linear Regression은 매립량 예측에서는 XGBoost와 비슷한 성능을 보이지만, 다른 지표에서는 상대적으로 더 높은 MAE 값을 보여주고,
Random Forest는 세 모델 중에서 일관되게 가장 높은 MAE 값을 보여주며, 상대적으로 가장 낮은 성능을 나타냄.
            
이러한 결과를 바탕으로, **XGBoost 모델을 선택하여 폐기물 발생량 예측에 사용**하는 것이 가장 효과적일 것으로 판단됩니다.

""")

# 코드 표시
st.code("""
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
import xgboost as xgb
from sklearn.metrics import mean_absolute_error

# 모델 학습 및 평가
models = {
    'Linear Regression': LinearRegression(),
    'Random Forest': RandomForestRegressor(random_state=42),
    'XGBoost': xgb.XGBRegressor(objective='reg:squarederror', random_state=42)
}

model_evaluations = {}

for model_name, model in models.items():
    model_fits = {}
    model_maes = {}
    for target in targets:
        # 모델 학습
        model.fit(X_train, y_train[target])
        model_fits[target] = model
        
        # 평가
        y_pred = model.predict(X_test)
        mae = mean_absolute_error(y_test[target], y_pred)
        model_maes[target] = mae
    
    model_evaluations[model_name] = model_maes

# 결과 출력
for model_name, evaluations in model_evaluations.items():
    print(f"Model: {model_name}")
    for target, mae in evaluations.items():
        print(f"  {target}: MAE = {mae:.2f}")
    print()
""", language='python')

# Redirect to app.py if not logged in, otherwise show the navigation menu
menu()