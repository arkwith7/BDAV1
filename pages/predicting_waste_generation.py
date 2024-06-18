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
st.title('폐기물 발생량 데이터 전처리')

st.markdown("""
### 데이터를 분석하고 예측 모델을 만들기 위해 다음과 같은 단계로 진행 합니다:

#### 1. 데이터 이해 및 전처리:
- 데이터의 컬럼을 분석하고, 결측값을 처리합니다.
- 명목형, 범주형 변수와 수치형 변수를 식별합니다.
- 데이터의 분포를 시각화하고, 이상치를 탐지합니다.

#### 2. 특성 엔지니어링:
- 필요에 따라 새로운 변수를 생성하거나 기존 변수를 변환합니다.
- 카테고리형 변수를 원-핫 인코딩(one-hot encoding) 또는 라벨 인코딩(label encoding)으로 변환합니다.
- 수치형 변수를 표준화 또는 정규화합니다.

#### 3. 모델 구축 및 평가:
- 데이터를 학습용(train)과 테스트용(test)으로 분할합니다.
- 적절한 회귀(regression) 또는 분류(classification) 모델을 선택합니다.
- 모델을 학습시키고 평가합니다.

먼저, 데이터의 기본 통계를 살펴보고 결측값을 처리한 다음, 시각화를 통해 데이터의 분포를 이해해 보겠습니다.
""")

# 데이터 표시
st.write("데이터셋 보기:")
st.dataframe(data)

# 데이터 기술적 통계 표시
st.write("데이터 기술적 통계:")
st.dataframe(data.describe())

# 수치형 컬럼 정의
numerical_cols = ['전체발생량', '총계_재활용', '총계_소각', '총계_매립', '총계_기타']

# 데이터 시각화
st.write("수치형 컬럼의 분포:")
fig, axs = plt.subplots(3, 2, figsize=(15, 10))  # 3x2 subplot grid 생성
for i, col in enumerate(numerical_cols):
    ax = axs[i // 2, i % 2]  # subplot 위치 결정 (3x2 grid에 맞게 인덱싱 수정)
    ax.hist(data[col], bins=50, alpha=0.75)
    ax.set_title(f'{col} Histogram')
    ax.set_xlabel(f'{col} (톤)')
    ax.set_ylabel('Frequency')
plt.tight_layout()
st.pyplot(fig)

# 데이터 전처리
#  - 범주형 변수 인코딩을 사용하여 변환합니다.
#  - 수치형 변수는 표준화합니다.
st.markdown("""
데이터 전처리
- 범주형 변수 인코딩을 사용하여 변환합니다.
- 수치형 변수는 표준화합니다.
""")
# 코드 표시
st.code("""
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_absolute_error

# 데이터 불러오기
file_path = './data/data_cleaned_augmented.csv'
data = pd.read_csv(file_path)

# 범주형 변수 인코딩
le_sido = LabelEncoder()
le_sigungu = LabelEncoder()

data['시도'] = le_sido.fit_transform(data['시도'])
data['시군구'] = le_sigungu.fit_transform(data['시군구'])

# 특징 및 타겟 변수 정의
features = ['발생년도', '시도', '시군구']
targets = ['전체발생량', '총계_재활용', '총계_소각', '총계_매립']

X = data[features]
y = data[targets]

# 데이터 분할
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
""", language='python')

# Redirect to app.py if not logged in, otherwise show the navigation menu
menu()