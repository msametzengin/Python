import numpy as np

dizi = np.array([10,20,30,40,50])

matris = np.array([[1,2,3],[4,5,6],[7,8,9]])

# matriste dilimleme
altMatris = matris[0:2,1:3] # 2,3 ve 5,6 start dahil end değil.
# çünkü 0 ve 1. satırdaki 2. ve 3. sütündaki verileri ver yani 2,3 ve 5,6
alt1Matris = matris[0:3,1:3] # 2,3 ve 5,6 ve 8,9
# !! 0:3 demek 0-1-2 demektir. 0 dahil ama 3 değil.
# çünkü 0,1 ve 2. satırdaki 2. ve 3. sütündaki verileri ver.

print(altMatris)
