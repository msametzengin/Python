import numpy as np

kitapFiyatlari = np.array([25,45,20,35,50,40,30])
satisAdetleri = np.array([100,150,200,120,130,80,110])
kategoriler = np.array(["Roman","Bilim","Tarih","Roman","Felsefe","Din","Mit"])

# toplamGelir = kitapFiyatlari*satisAdetleri
# print(kategoriler,'\n',toplamGelir)

#-------------------------------------

# ortalamaFiyat = np.mean(kitapFiyatlari)
# maxFiyat = np.max(kitapFiyatlari)
# minFiyat = np.min(kitapFiyatlari)

# print("Ortalama fiyat: ",ortalamaFiyat, "tl")
# print("max fiyat: ",maxFiyat, "tl")
# print("min fiyat: ",minFiyat,"tl")

#------------------------------------

# romanlar = kitapFiyatlari[kategoriler == "Roman"] # kategoriler == 'Roman' demek 4 demek bu örnekte
# print("Roman kategorisindeki kitap fiyatlari: ",romanlar)

# romanSatislari = satisAdetleri[kategoriler=="Roman"]
# print("Roman satis:  ",romanSatislari)

# romanToplamSatis = np.sum(romanlar * romanSatislari)
# print(romanToplamSatis)

#----------------------------------------

veri = np.array([kitapFiyatlari,satisAdetleri])
veriReShaped = np.reshape(veri,(2,7))
print(veriReShaped)
