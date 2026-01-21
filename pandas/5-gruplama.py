import pandas as pd

#exceli oku
df = pd.read_excel(r'd:\GitRepo\Python\pandas\teknolojik_urunler.xlsx')

gruplar = df.groupby('Kategori')

# toplamSatis = df.groupby('Kategori')["Satış"].sum()
# toplamSatisFiyat = df.groupby('Kategori')["Fiyat (TL)"].sum()
# ortalamaSatisFiyati = df.groupby('Kategori')["Fiyat (TL)"].mean()


# toplam = df.groupby('Kategori').agg(
#     {
#         'Satış':'sum',
#         'Fiyat (TL)':'mean'
#     })
# print(toplam)

# enPahaliUrun = df.loc[df.groupby('Kategori')['Fiyat (TL)'].idxmax()]
# print(enPahaliUrun)

satisUstGruplar = df.groupby('Kategori').filter(lambda x: x['Satış'].sum() > 50)
#İlgili sütünları seçerek yazdır.
print(satisUstGruplar[['Kategori','Ürün Adı','Satış','Fiyat (TL)']])