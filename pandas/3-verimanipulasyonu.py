import pandas as pd

#exceli oku
df = pd.read_excel(r'd:\GitRepo\Python\pandas\teknolojik_urunler_manipule.xlsx')

# eksik_veriler = df.isnull()
# # print(eksik_veriler)

# temiz_df = df.dropna()
# # print(temiz_df)

# doldurulmus_df = df.fillna("Deger yok")
# print(doldurulmus_df)

# df["Fiyat (TL)"] = df["Fiyat (TL)"].astype("Int64")
# print(df.dtypes)

# df.insert(2,"Yeni Sütun",range(1,21))
# print(df.head())

# df.to_excel("toexcel.xlsx",index=False)
# print("Veri kaydedildi.")

df_dusukFiyat = df.sort_values(by="Fiyat (TL)",ascending=False)
print(df_dusukFiyat)