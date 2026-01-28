import numpy as np
from tensorflow.keras.models import Sequential # type: ignore
from tensorflow.keras.layers import Dense #type: ignore

#giriş verilerini (XOR problemi olarak al)
X = np.array([[0,0],[0,1],[1,0],[1,1]]) #problem
y = np.array([[0],[1],[1],[0]]) #çözüm

#basit model
model = Sequential()
model.add(Dense(3,input_dim = 2,activation='relu'))
model.add(Dense(1, activation='sigmoid'))

#modeli derleme
model.compile(loss='binary_crossentropy', optimizer='adam' , metrics = ['accuracy'])

#modeli eğitme
model.fit(X,y,epochs=200, verbose=1)

#tahminleme
tahmin = model.predict(X)
print('Tahminler: \n',tahmin)

