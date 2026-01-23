import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Ornek veri
df = pd.read_excel('teknolojik_urunler_zamanli.xlsx')
df['Tarih'] = pd.to_datetime(df['Tarih'])
df.set_index('Tarih',inplace = True)

#aylik satis trendi
# aylikSatis = df.resample('ME')['Satış'].sum()
# aylikSatis.plot(kind='line',title="Aylık Satış Miktarları")
# plt.xlabel('Ay')
# plt.ylabel('Satış Miktarı')
# plt.show()

#çizgi çekmek
# df.plot(kind='scatter', x='Fiyat (TL)',y='Satış',title='Fiyat ve Satış ilişkisi')
# z = np.polyfit(df['Fiyat (TL)'], df['Satış'], 1)
# p = np.poly1d(z)
# plt.plot(df['Fiyat (TL)'], p(df['Fiyat (TL)']), color='red')
# plt.show()

#önemli 

bins = [0,2000,5000,10000,20000,30000]
labels = ['Düşük','Orta','Yüksek','Çok yüksek','Lüks']
df['Fiyat Kategorisi'] = pd.cut(df['Fiyat (TL)'], bins = bins , labels = labels)

#fiyat kategorisine göre satış dağılımı
df.groupby('Fiyat Kategorisi')['Satış'].sum().plot(kind='bar',title='Fiyat Kategorisine Göre Toplam Satışlar')
plt.xlabel('Fiyat Kategorisi')
plt.ylabel('Toplam Satış')
plt.show()


