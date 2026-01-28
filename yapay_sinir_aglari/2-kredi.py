import numpy as np
from tensorflow.keras.models import Sequential # type: ignore
from tensorflow.keras.layers import Dense #type: ignore
from tensorflow.keras.optimizers import Adam  # type: ignore
from sklearn.preprocessing import StandardScaler

#giriş verilerini (Yaş ve gelir)
X = np.array([[25,2000],[30,4000],[45,10000],[50,3000]]) #problem
y = np.array([[0],[1],[1],[0]]) #çözüm

#basit model
model = Sequential()
model.add(Dense(3,input_dim = 2,activation='relu'))
model.add(Dense(1, activation='sigmoid'))

#modeli derleme
optimizer = Adam(learning_rate=0.005)
model.compile(loss='binary_crossentropy', optimizer=optimizer , metrics = ['accuracy'])

#veriyi ölçeklendir
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

#modeli eğitme
model.fit(X_scaled,y,epochs=200, verbose=1)

# #tahminleme
# tahmin = model.predict(X_scaled)
# print('Tahminler: \n',tahmin)

while True:
    #kullanıcıdan veri al
    user_input_1 = float(input('Yaşınızı girin: '))
    user_input_2 = float(input('Maaşınızı girin: '))

    #kullanıcıdan alınan girdileri modele uygun hale getirme
    user_data = np.array([[user_input_1,user_input_2]])
    #girdileri ölçeklendirme
    user_data_scaled = scaler.transform(user_data)
    #tahmin oluştur
    prediction = model.predict(user_data_scaled)
    #sonucu yazdır
    if(prediction[0][0]<0.50):
        print(f"Kredi alamaz")
    else:
        print("Alabilir")
    print(f"Tahmin sonucu: {prediction[0][0]:.4f}")
