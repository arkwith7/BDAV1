#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


df_1 = pd.read_csv('data/combined_data.csv')

# 2014 ~ 2018 년도 폐기물 총계
df_14_18 = df_1[df_1['구분_시도']=='전국'][['총계_계', 'YEAR']]


# In[33]:


df_2 = pd.read_csv('./2019_2021.csv')

# 컬럼명 동일시
df_2.rename(columns = {'2019년 발생량':'총계_계'},inplace=True)

# 2019 ~ 2021 년도 폐기물 총계
df_19_21 = df_2[(df_2['시도']=='전국')&(df_2['폐기물 종류_대']=='합계')][['총계_계','YEAR']]


# In[27]:


# union
df = pd.concat([df_14_18, df_19_21]).reset_index(drop=True)


# In[41]:


df


# In[53]:


import matplotlib.pyplot as plt
# 그래프 크기 설정
plt.figure(figsize=(14, 7))

# plt.grid(True)

# 막대그래프
plt.bar(df['YEAR'], df['총계_계'], color='skyblue', label='Total Generated (tons)', alpha=0.7)

# 꺾은선그래프
plt.plot(df['YEAR'], df['총계_계'], color='r', marker='o', label='Total Generated (tons)')

# 제목과 레이블 추가
plt.title('Total Waste Generated in Korea (2014-2021)')
plt.xlabel('Year')
plt.ylabel('Total Waste Generated (tons)')
plt.legend()

# 그래프 표시

plt.show()


# In[ ]:




