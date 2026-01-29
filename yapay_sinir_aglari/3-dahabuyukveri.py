import numpy as np
import pandas as pd
from tensorflow.keras.models import Sequential # type: ignore
from tensorflow.keras.layers import Dense #type: ignore
from tensorflow.keras.optimizers import Adam  # type: ignore
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

data = pd.read_excel('genisletilmisveri.xlsx')

#pandas veri çerçevesi
df = pd.DataFrame(data)

#sahte değişkenler oluştur 'bekar' 0 gibi
df = pd.get_dummies(df,columns=['Medeni Durum','Meslek','Eğitim Durumu'],drop_first=True)

#kesme işlemi çıkartma(kredi onayı)
X=df.drop('Kredi Onayı',axis=1).values

#çıkış verisi
y = df["Kredi Onayı"].values

#veriyi ikiye böl test ve eğitim
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.4,random_state=42)

#model oluştur
model = Sequential()
model.add(Dense(2,input_dim=X.shape[1],activation='relu'))
model.add(Dense(1,activation='sigmoid'))

#modeli derle ve öğrenme hızı eklemek
optimizer = Adam(learning_rate=0.001)
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

#kullanıcıdan veri alma
while True:
    user_input_1=float(input('Yaşınızı giriniz: '))
    user_input_2=float(input('Maşşınızı giriniz: '))
    user_input_3=input('Medeni durumunuzu giriniz: ')
    user_input_4=input('Mesleğiniz(Mühendis, Doktor, Öğretmen, Avukat) giriniz: ')
    user_input_5=input('Eğitim durumunuzu giriniz(Lisans, Yüksek Lisans, Doktora) giriniz: ')

    user_data = pd.DataFrame({
        'Yaş':[user_input_1],
        'Gelir':[user_input_2],
        'Medeni Durum' + user_input_3:[1],
        'Meslek' + user_input_4:[1],
        'Eğitim Durumu'+user_input_5:[1]
    })

    #kredi onayı kısmını sil
    user_Data=user_data.reindex(columns=df.drop('Kredi Onayı', axis=1).columns,fill_value=0)

    #veriyi ölçeklendirelim
    user_data_scaled = scaler.transform(user_Data)

    #tahminleme
    prediction = model.predict(user_data_scaled)
    print(f"Tahmin sonucu: {prediction[0][0]:.4f}")
    
