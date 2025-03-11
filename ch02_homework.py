import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data_url = 'https://raw.githubusercontent.com/codingalzi/DataSci/refs/heads/master/data/'
housing_df = pd.read_csv(data_url + "california_housing.csv")
housing_total_rooms_arr = np.array(housing_df["total_rooms"])
total_rooms_mean = np.mean(housing_total_rooms_arr)
total_rooms_cen = np.median(housing_total_rooms_arr)
total_rooms_mode = housing_df["total_rooms"].mode()[0]
total_rooms_var = np.var(housing_total_rooms_arr)
total_rooms_std = np.std(housing_total_rooms_arr, ddof=0)
total_rooms_range = np.max(housing_total_rooms_arr) - np.min(housing_total_rooms_arr)
total_rooms_IQR = np.percentile(housing_total_rooms_arr, 75) - np.percentile(housing_total_rooms_arr, 25)
total_rooms_arr = [total_rooms_mean, total_rooms_cen, total_rooms_mode, total_rooms_var, total_rooms_std, total_rooms_range, total_rooms_IQR]
total_rooms_arr_norm = (total_rooms_arr - total_rooms_mean) / total_rooms_std
#total_rooms_df = pd.DataFrame({"total_rooms" : total_rooms_arr_norm}, index = pd.Index(['1', '2', '3', '4', '5', '6', '7'], name = 'number'))
#정규화 진행 한 total_rooms 어레이 데이터프레임으로 변환
housing_df.boxplot(column = ['total_rooms'], grid=False)
plt.show()
#print(total_rooms_arr)
#평균값, 중앙값, 최빈값, 분산, 표준편차, 범위, 사분범위, 상자그림 그리기, 정규화