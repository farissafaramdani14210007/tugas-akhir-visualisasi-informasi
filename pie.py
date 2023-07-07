import matplotlib.pyplot as plt
import pandas as pd

table = pd.read_csv('data_wisata.csv')
table.head()
fig = plt.figure()
wilayah = table['kecamatan']
wilayah.value_counts().plot(kind='pie')
fig