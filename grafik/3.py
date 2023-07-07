import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

wisata = pd.read_csv('data_wisata.csv')
data1 = wisata['jenis_usaha'].value_counts()

fig = plt.figure()
x = data1.index
y = data1.values
plt.bar(x, y, color = 'red', width = 0.6)
plt.xticks(rotation = 90)
plt.xlabel('jenis usaha')
plt.ylabel('value')
plt.title('banyak jenis usaha di jakarta')
plt
