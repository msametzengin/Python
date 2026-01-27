import numpy as np

# dizi1 = np.array([1,2,3])
# dizi2 = np.array([4,5,6])

# birlesenDizi = np.concatenate((dizi1,dizi2)) #concatenate tek boyutlu dizileri birleştirir.
# print(birlesenDizi) 

#---------------------------------------------

# iki boyutlu dizi birleştirme:

# dizi1 = np.array([[1,2,3],[4,5,6]])
# dizi2 = np.array([[7,8,9],[10,11,12]])

# birlestirilenDizi1 = np.hstack((dizi1,dizi2)) # hstack yatay birlestirir.
# birlestirilenDizi2 = np.vstack((dizi1,dizi2)) # vstack dikey birlestirir.
# print(birlestirilenDizi2)

#---------------------------------------------

# dizi = np.array([1,2,3,4,5,6])
# bd = np.split(dizi,3) # 3 eşit parçaya böler. tek boyutlu

# dizi = np.array([[1,2,3,4],[5,6,7,8]])
# bd = np.hsplit(dizi,2) # 2 eşit parçaya böler çift boyut.
# h olursa yatay , v olursa dikey böler.


