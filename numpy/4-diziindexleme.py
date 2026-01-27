import numpy as np

dizi = np.array([10,20,30,40,50])
# eleman = dizi[2]  # İndex ile erişim
# print(eleman)

# matris = np.array([[1,2,3],[4,5,6],[7,8,9]])
# # # 2. satır => 4,5,6 ve 3. sütun => 3,6,9 yani 9
# # eleman = matris[1,2]  # 2. satır, 3. sütundaki eleman 6
# # eleman2 = matris[2,1] # 3. satır 2. sütun yani 8
# eleman = matris[-1,-2] # son satır sondan 2. i sütun yani 8

# # print("Son eleman: ",dizi[-1]) # son eleman
# print(eleman)

dilim = dizi[2:4] #30,40 olucak. yani 2. indexten 4. elemana kadar
dilim2 = dizi[0:-1]#10,20,30,40 olucak.
print("Dilim: ",dilim)

