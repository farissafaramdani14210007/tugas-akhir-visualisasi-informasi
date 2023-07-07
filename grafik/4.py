import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

wisata = pd.read_csv('data_wisata.csv')
data2 = wisata['kecamatan'].value_counts()

fig = plt.figure()
x = data2.index
y = data2.values
plt.bar(x, y, color = 'red', width = 0.6)
plt.xticks(rotation = 90)
plt.xlabel('kecamatan')
plt.ylabel('value')
plt.title('banyak kecamatan yang memiliki jenis usaha di jakarta')
plt
