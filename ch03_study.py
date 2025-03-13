import numpy as np
import pandas as pd
import matplotlib as plt

data_url = 'https://raw.githubusercontent.com/codingalzi/DataSci/refs/heads/master/data/'

df = pd.read_csv(data_url+'ch02_scores_em.csv', index_col='student number')
english_scores = np.array(df['english'])

print(english_scores    )