import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

#veriyi yükle
df = pd.read_excel("veri_on_isleme_ve_ozellik_muhendisligi.xlsx")

#eksik verileri dolduralım
df.fillna(df['Gelir'].mean(),inplace=True)

#kümeleme
X= df[['Cinsiyet',"Meslek"]]

#veriyi ölçeklendir
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

#k-means modeli
kmeans = KMeans(n_clusters=3,random_state=42)
kmeans.fit(X_scaled)

#kümeyi tahmin et
df['Küme'] = kmeans.labels_ #dataframenin içine isimleriyle ekler

#görüntüleme
plt.figure(figsize=(8,6))
plt.scatter(df['Yaş'],df['Gelir'],c=df['Küme'],cmap='viridis')
plt.title('Kümeleme Algoritması Sonucu')
plt.xlabel('Yaş')
plt.ylabel('Gelir')
plt.show()