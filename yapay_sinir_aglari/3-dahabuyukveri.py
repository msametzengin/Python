import numpy as np
import pandas as pd
from tensorflow.keras.models import Sequential # type: ignore
from tensorflow.keras.layers import Dense #type: ignore
from tensorflow.keras.optimizers import Adam  # type: ignore
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

data = {
    'Yaş': [25, 30, 45, 50, 28, 35, 40, 60],
    'Gelir': [2000, 4000, 10000, 3000, 3500, 5000, 8000, 12000],
    'Medeni Durum': ['Bekar', 'Evli', 'Evli', 'Bekar', 'Bekar', 'Evli', 'Evli', 'Bekar'],
    'Meslek': ['Mühendis', 'Doktor', 'Öğretmen', 'Avukat', 'Mühendis', 'Doktor', 'Avukat', 'Öğretmen'],
    'Eğitim Durumu': ['Lisans', 'Lisans', 'Yüksek Lisans', 'Doktora', 'Lisans', 'Lisans', 'Yüksek Lisans', 'Doktora'],
    'Kredi Onayı': [0, 1, 1, 0, 1, 1, 1, 0]
}

#pandas veri çerçevesi
df = pd.DataFrame(data)

#sahte değişkenler oluştur 'bekar' 0 gibi
df = pd.get_dummies(df,columns=['Medeni Durum','Meslek','Eğitim Durumu'],drop_first=True)

#kesme işlemi çıkartma(kredi onayı)
X=df.drop('Kredi Onayı',axis=1).values

#çıkış verisi
y = df["Kredi Onayı"].values

#veriyi ikiye böl test ve eğitim
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=42)

#model oluştur
model = Sequential()
model.add(Dense(10,input_dim=X.shape[1],activation='relu'))
model.add(Dense(1,activation='sigmoid'))

#modeli derle ve öğrenme hızı eklemek
optimizer = Adam(learning_rate=0.005)
model.compile(loss='binary_crossentropy',optimizer = optimizer,metrics =['accuracy'])

#veriyi ölçeklendir
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train) #eğit ölçeklendir
X_test_scaled = scaler.transform(X_test) #ölçeklendir

#modeli eğitelim
model.fit(X_train_scaled,y_train,epochs = 200,verbose=1)

#₺ahminleme
y_pred = model.predict(X_test_scaled)
y_pred = (y_pred > 0.5).astype(int)

#doğruluk oranını ölç
accuracy = accuracy_score(y_test,y_pred)
print(f"Test doğruluk oranı: {accuracy*100:.2f}%")