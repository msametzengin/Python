import numpy as np

data = np.loadtxt('veri.txt', delimiter=' ')

#----------------------------------------

rowSums = np.sum(data, axis=1)
#axis=1 => satırları toplar.
#axis=0 => sütünları toplar.
# print("Her satirin toplami = ",rowSums)

# Toplamlarini baska output.txt'ye kaydetmek için:
# np.savetxt('output.txt', rowSums, fmt='%d')

# Toplamlarini datanin yanina yazmak ve yeni txt icin: 
outputData = np.column_stack((data, rowSums))

np.savetxt('outputWithSums.txt',outputData,fmt='%d',delimiter=' ')
print("Kayit tamamlandi.")