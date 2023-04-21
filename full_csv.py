import pandas as pd
from pandas import DataFrame

data1 = pd.read_csv('./results_time.csv')
data2 = pd.read_csv('./results_mem.csv')

data3 = pd.merge(data1, data2)
data3.to_csv('full.csv', index=False)