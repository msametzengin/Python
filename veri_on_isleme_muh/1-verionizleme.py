import pandas as pd
from sklearn.preprocessing import LabelEncoder,StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns
#veriyi yükle
df = pd.read_excel("veri_on_isleme_ve_ozellik_muhendisligi.xlsx")

#eksik gelir verilerini ortalama ile doldur (mean())
df['Gelir'].fillna(df['Gelir'].mean(),inplace=True)
# print(df)

#erkek kadın 0-1 yap
le = LabelEncoder()
df['Cinsiyet'] = le.fit_transform(df['Cinsiyet'])
# print(df)

scaler = StandardScaler()
# # df[['Yaş','Gelir']] = scaler.fit_transform(df[['Yaş','Gelir']])
# print(df)

#id sütununu sil
df.drop('ID',axis=1,inplace=True)

#gelir grubu diye yeni excel aç
df['Gelir_Grubu'] = pd.cut(df['Gelir'],bins = [0,3000,5000,7000],labels = ['Düşük','Orta','Yüksek'])
# df.to_excel('Kategorik_Gelir.xlsx', index=False)

#görsellestirme
plt.figure(figsize=(10,6))
plt.hist(df["Yaş"],bins=10,color='skyblue',edgecolor='black') #"Yaş" ı değiştirerek diğerlerine de bakılabilir.
plt.title('Yaş dağılımı')
plt.xlabel('Yaş')
plt.ylabel('Frekans')
plt.show()

#cinsiyet ve gelir grubu arasındaki iliski
plt.figure(figsize=(10,6))
sns.countplot(x='Gelir_Grubu',hue='Cinsiyet',data=df) #hue'i meslek vs. değiştirilebilir.
plt.title('Gelir grubu ve cinsiyet ilişkisi')
plt.xlabel('Gelir grubu')
plt.ylabel('Kişi sayısı')
plt.show()