import numpy as np

# 1-10 rastgele 5 tam sayı
# randomNumb1 = np.random.randint(1,10,size=5)

# 0-1 rastgele 5 sayı float
# randomNumb2 = np.random.random(5)

# normalRakam = np.random.normal(0,1,5) # standart sapmaya yakın veri oluşturuyor.

randomArray = np.random.rand(3,3) # 3e3 
randomArray = randomArray.astype(int) # inte çevir.
print(randomArray)

