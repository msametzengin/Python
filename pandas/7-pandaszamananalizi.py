import pandas as pd
#excel dosyasinin yolu
df = pd.read_excel('teknolojik_urunler_zamanli.xlsx')

#tarih sütünunu datetime formatina çevirme
#gerekli yoksa calismaz.

df['Tarih'] = pd.to_datetime(df['Tarih'])
#indexleme !!!!
df.set_index('Tarih',inplace = True)
df = df.sort_index()
# print(df)

# 1.en yuksek satisin yapildigi ay ve o ayda satilan ürünler!!

aylikSatis = df.resample('ME')['Satış'].sum()

maxAy = aylikSatis.idxmax()
maxSatisAy = aylikSatis.max()
maxSatisAyUrunler = df[df.index.to_series().between(maxAy - pd.offsets.MonthBegin(1),maxAy)]
# print(f"En yüksek satis yapilan ay: {maxAy} - Toplam satis: {maxSatisAy}")
# print("O ayda satilan ürünler")
# print(maxSatisAyUrunler[['Ürün Adı','Satış']])

# 2.en düsük satisin yapıldıgı ay ve o ayda satilan ürünler!!

minAy = aylikSatis.idxmin()
minSatisAy = aylikSatis.min()
minSatisAyUrunler = df[df.index.to_series().between(minAy - pd.offsets.MonthBegin(1),minAy)]
# print(f"En düsük satis yapilan ay: {minAy} - Toplam satis: {minSatisAy}")
# print("O ayda satilan ürünler")
# print(minSatisAyUrunler[['Ürün Adı','Satış']])

# 3. en fazla satis yapilan gün ve o gün satilan ürünler

günlükSatis = df.resample('D')['Satış'].sum()
maxGun = günlükSatis.idxmax()
maxSatisGun = günlükSatis.max()
maxSatisGunUrunler = df.loc[maxGun]
# print(f"\n En fazla satis yapilan gün: {maxGun} - Toplam satis: {maxSatisGun}")
# print("O gün satilan ürünler: ")
# print(maxSatisGunUrunler[["Ürün Adı","Satış"]])

# 4.haftalik en fazla satış yapılan ürünler

haftalikSatis = df.resample('W')['Satış'].sum()
maxHafta = haftalikSatis.idxmax()
maxSatisHafta = haftalikSatis.max()
maxSatisHaftaUrunler = df[df.index.to_series().between(maxHafta - pd.offsets.Week(1),maxHafta)]
# print(f"\nEn fazla satis yapılan hafta: {maxHafta} - Toplam Satış: {maxSatisHafta}")
# print("O hafta satılan ürünler: ")
# print(maxSatisHaftaUrunler[["Ürün Adı","Satış"]])

# 5. aylik ortalama satis
aylikOrtalamaSatis = df.resample('ME')["Satış"].mean()
# print("Aylık Ortalama Satışlar: ")
# print(aylikOrtalamaSatis)

# 6. belirli aralıkta ürünleri çekme
belirliAralikUrunler = df[df.index.to_series().between('2025-01-01','2025-3-31')]
# print("Ocak 2025 ile Mart 2025 arasında satılan ürünler: ")
# print(belirliAralikUrunler[["Ürün Adı","Satış","Fiyat (TL)","Toplam Fiyat (TL)"]])

# !!7. en yüksek toplam fiyatın olduğu ay ve o ayda satılan ürünler!!

aylikToplamFiyat = df.resample('ME')['Toplam Fiyat (TL)'].sum()
maxAyFiyat = aylikToplamFiyat.idxmax()
maxFiyatAy = aylikToplamFiyat.max()
maxFiyatAyUrunler = df[df.index.to_series().between(maxAyFiyat - pd.offsets.MonthBegin(1),maxAyFiyat)]
print(f"En yüksek toplam fiyata sahip ay: {maxAyFiyat} - Toplam fiyat: {maxFiyatAy}")
print("O ayda satılan ürünler: ")
print(maxFiyatAyUrunler[["Satış","Ürün Adı","Toplam Fiyat (TL)"]])

