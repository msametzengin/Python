import pandas as pd
import matplotlib.pyplot as plt

#Ornek veri
df = pd.read_excel('teknolojik_urunler_zamanli.xlsx')
df['Tarih'] = pd.to_datetime(df['Tarih'])
df.set_index('Tarih',inplace = True)

#Satışların zaman içindeki değişimini gösteren bir çizgi grafiği
# df['Satış'].plot(title='Satışların zaman içindeki değişimi', xlabel='Tarih', ylabel='Satış Miktarı')
#plt.show()

# aylikSatis = df.resample('ME')['Satış'].sum()
# aylikSatis.plot(kind='bar', title='Aylık Toplam Satışlar',xlabel='Ay',ylabel='Toplam Satış')
# plt.show()

#Pasta grafiği
# kategoriSatis = df.groupby('Kategori')['Satış'].sum()
# kategoriSatis.plot(kind='pie',autopct='%1.1f%%', title='Kategorilere göre satış dağılımı')
# plt.ylabel('') #y eksenini gizleme
# plt.show()

# Scattor plot(dağılım grafiği)
# df.plot(kind='scatter',x='Fiyat (TL)',y='Satış',title='Fiyat ve Satış İlişkisi')
# plt.show()

# histogram
df['Fiyat (TL)'].plot(kind='hist', bins=10 , title='Fiyat Dagilimi')
plt.xlabel('Fiyat (TL)')
plt.show()