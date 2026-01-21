import pandas as pd

#exceli oku
df = pd.read_excel(r'd:\GitRepo\Python\pandas\teknolojik_urunler.xlsx')

# df_fiyatUst = df[df["Fiyat (TL)"] > 5000]
# print(df_fiyatUst)

# df_filtre = df[(df["Fiyat (TL)"] > 5000) & (df["Kategori"] == "Bilgisayarlar")]
# print(df_filtre)

# df_Secili = df.loc[:,["Ürün Adı", "Fiyat (TL)"]]
# print(df_Secili)
# index numarasına göre seçer.
# df_ilkbes = df.iloc[:12,:]
# print(df_ilkbes)

# sql tarzı sorgulama query basit
# df_sorgu = df.query("Satış > 10")
# print(df_sorgu)

# isin str için
df_kategoriler = df[df["Kategori"].isin(["Bilgisayar","Mobil Cihazlar"])]
print(df_kategoriler)