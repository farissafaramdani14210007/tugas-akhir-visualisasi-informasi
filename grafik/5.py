import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

wisata = pd.read_csv('data_wisata.csv')
data3 = wisata['wilayah'].value_counts()

fig = plt.figure()
x = data3.index
y = data3.values
plt.bar(x, y, color = 'red', width = 0.6)
plt.xticks(rotation = 90)
plt.xlabel('wilayah')
plt.ylabel('value')
plt.title('banyak wilayah yang memiliki jenis usaha di jakarta')
plt
