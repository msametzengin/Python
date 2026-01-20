import pandas as pd

#exceli oku
df = pd.read_excel(r'd:\GitRepo\Python\pandas\teknolojik_urunler.xlsx')

#ilk birkac satiri oku
# print(df.head())

# ortalamaFiyat = df['Fiyat (TL)'].mean()
# print(f"Ortalama Fiyat: {ortalamaFiyat} TL")

#En cok gelir getiren ürünü sırala
# kategoriBazliSatis = df.groupby('Kategori')['Satış'].sum()
# print(kategoriBazliSatis)

#En cok gelir getiren ürünü bulma
# maxGelir = df.loc[df["Toplam Fiyat (TL)"].idxmax()]
# print(f"En çok gelir getiren ürün : {maxGelir}")

#Belirli bir fiyat üstünü cek ve excel dosyasına yazdır.
fiyatUstUrunler = df[df['Fiyat (TL)'] >= 4000]
print('Fiyati 4000 tlnin üzerinde olan ürünler : ')
print(fiyatUstUrunler)
fiyatUstUrunler.to_excel('fiyati_4000_üstü_olanlar.xlsx',index=False)
