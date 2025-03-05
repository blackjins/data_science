import pandas as pd
import numpy as np
data_url = 'https://raw.githubusercontent.com/codingalzi/DataSci/refs/heads/master/data/'
#------------------1번 문제
#아래 링크를 참고하여 Pandas의 데이터프레임에 대해 알아보아라.
#참고 문서: (코딩알지) 판다스 데이터프레임
#공부 제외: 17.3.
#------------------2번 문제
#기본 데이터 저장소에 있는 california_housing.csv 파일은 미국 캘리포니아 주의 주택 정보를 담고 있다.
#------------------2-1번 문제
#위 파일의 내용을 데이터프레임으로 불러와서 housing_df 변수에 할당하라. 단, 인덱스는 별도로 지정하지 않는다.
housing_df = pd.read_csv(data_url + "california_housing.csv")
#------------------2-2번 문제
#캘리포니아 주택 정보 데이터의 기초 정보를 확인하라.
housing_df.info()
housing_df.describe()
#------------------2-3번 문제
#데이터셋에 포함된 특성을 다음 네 종류의 특성으로 구분하라.
#수치형 특성, 범주형 특성, 이산형 특성, 연속형 특성
############################################################
#longitude(경도)
#범주
#latitude(위도)
#범주
#housing_median_age(건축물 중위 연령)	
#수치형, 이산형
#total_rooms(방의 총 개수)
#수치형, 이산형    
#total_bedrooms(침실 총 개수)
#수치형, 이산형	
#population(인구수)
#수치형, 이산형	
#households(가구수)
#수치형, 이산형
#median_income(중위소득)
#수치형, 연속형	
#median_house_value(주택 중위 가격)
#수치형, 이산형
#ocean_proximity(해안 근접도)
#범주형
############################################################
#------------------4번 문제
#99번 인덱스의 샘플을 구하라.
print(housing_df.loc[99])
#------------------5번 문제
#ocean_proximity 특성값만 포함한 데이터프레임을 구하라.
print(housing_df['ocean_proximity'])
#------------------6번 문제
#median_income, median_house_value, ocean_proximity 특성값만 데이터프레임을 구하라.
print(housing_df[["median_income", "median_house_value", "ocean_proximity"]])




