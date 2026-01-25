import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#excel dosyalarini ekle

df = pd.read_excel('karar_agaci_veri_100.xlsx')

#yaş ile hastalık arasındaki ilişkiyi görselleştir

plt.figure(figsize=(10,6))
sns.histplot(data=df, x='Yas',hue='Hastalik',multiple='stack',kde=False)
plt.title("Yaş dağılımı ve hastalık durumu")
plt.xlabel("Yaş")
plt.ylabel("Kişi sayısı")
plt.show()

#kan basıncı ile hastalık arasındaki ilişkiyi görselleştir

plt.figure(figsize=(10,6))
sns.histplot(data=df, x='Kan_Basinci',hue='Hastalik',multiple='stack',kde=True)
plt.title("Kan basıncı ve hastalık durumu")
plt.xlabel("Kan basıncı")
plt.ylabel("Kişi sayısı")
plt.show()

#kolesterol ile hastalık arasındaki ilişkiyi görselleştir

plt.figure(figsize=(10,6))
sns.histplot(data=df, x='Kolesterol',hue='Hastalik',multiple='stack',kde=False)
plt.title("Kolesterol ve hastalık durumu")
plt.xlabel("Kolesterol")
plt.ylabel("Kişi sayısı")
plt.show()
