import pandas as pd
data_url = 'https://raw.githubusercontent.com/codingalzi/DataSci/refs/heads/master/data/'
#dataset 기본 주소
sports_df = pd.read_csv(data_url + 'ch01_sport_test.csv')
print(sports_df.loc[1]) 