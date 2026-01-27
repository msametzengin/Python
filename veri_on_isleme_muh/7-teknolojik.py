import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

#veriyi yükel
df = pd.read_excel('teknolojik_urunler_zamanli.xlsx')

#fiyat ve satış sütünlarını seç
X = df[['Fiyat (TL)','Satış']]

#veriyi ölçeklendirelim
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

#Kümeleme
kmeans = KMeans(n_clusters=1,random_state=42)
df['Küme'] = kmeans.fit_predict(X_scaled) #çevirdiğim veriyi eğitiyorum analiz

#görselleştirme
plt.figure(figsize=(10,6))
plt.scatter(df['Fiyat (TL)'],df["Satış"],c=df['Küme'],cmap = 'viridis')
plt.title('Ürünler için Analiz Edilmiş Kümeleme')
plt.xlabel('Fiyat (TL)')
plt.ylabel('Satış')

#ÖNEMLİ
for i in range(len(df)):
    urun_adi_tarih_satis = f"{df['Ürün Adı'][i]} ({df['Tarih'][i].strftime('%d-%m-%Y')}) [{df['Satış'][i]} adet] {df['Fiyat (TL)'][i]} TL"
    plt.text(df['Fiyat (TL)'][i]+200,df['Satış'][i]+0.5, urun_adi_tarih_satis,fontsize=7,ha='right')
plt.show()
#1800-5000 arası akıllı ev bilgisayar mobil oyun cihazları vs. önemli olduğunu görürüz.