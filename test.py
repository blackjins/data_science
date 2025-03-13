import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data_url = 'https://raw.githubusercontent.com/codingalzi/DataSci/refs/heads/master/data/'
housing_df = pd.read_csv(data_url + "california_housing.csv")


freq, bin_edges, _ = plt.hist(housing_df['median_income'], bins=100, range=(0, 20), rwidth=0.8)
plt.xlabel("median_income")
plt.ylabel("Frequency")
plt.title("California housing data")

plt.show()
