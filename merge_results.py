import pandas as pd

data1 = pd.read_csv('./results_time.csv')
data2 = pd.read_csv('./results_mem.csv')

data3 = pd.merge(data1, data2)
data3.to_csv('result.csv', index=False)
