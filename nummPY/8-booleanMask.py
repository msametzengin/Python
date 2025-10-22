import numpy as np

dizi = np.array([10,20,30,40,50,60,70,24,11,33,75])
# booleanMask = dizi>50
# print(booleanMask)

#boolean maskeyi kullanarak dizideki elemanları seçmek
# secilmis = dizi[booleanMask]
# print("50'den büyük olanlar: ",secilmis)

#coklu eleme
booleanMask = (dizi>30) & (dizi<70)
# & bu and, | bu or
print("30 ile 70 arasi elemanlar: ",dizi[booleanMask])