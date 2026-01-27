import numpy as np

dizi1 = np.array([1,2,3,4])
dizi2 = np.array([3,4,5,6])

# toplam = dizi1 + dizi2
# cikarma = dizi1 - dizi2
# carpma = dizi1 * dizi2
# bolme = dizi1 / dizi2
# print(toplam)
# print(cikarma)
# print(carpma)
# print(bolme)

# Toplama fonksiyonu
toplam = np.sum(dizi1)
carpim = np.prod(dizi2)
karekokAl = np.sqrt(dizi1) # karekokunu alır

# Aritmetik ortalama
aritmetikOrt = np.mean(dizi1)

# Medyan
medyanAl = np.median(dizi1)

# Standart Sapma
standartSapma = np.std(dizi1)

print(standartSapma)