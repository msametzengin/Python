import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

#veriyi hazırlama : yaş,kan basıncı, kolestrol ve hastalık durumu verileri
data = {
    'Yaş':[25,50,45,30,60],
    'Kan_Basıncı':[120,140,130,110,150],
    'Kolesterol': [180,240,200,160,220],
    'Hastalik':[0,1,1,0,1] # 0 hayır saglam, 1 evet hasta
}

df = pd.DataFrame(data)

X = df[["Yaş","Kan_Basıncı","Kolesterol"]] #Girdi 
y = df["Hastalik"]                         #Çıktı

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

#karar ağacı sıfırlandırıcısını oluşturma ve eğitme
classifier = DecisionTreeClassifier()
classifier.fit(X_train,y_train)

#test verisi ile tahmin yapma
y_pred = classifier.predict(X_test)

#modelin doğruluğunu ölçme
accuracy = accuracy_score(y_test,y_pred)
# print(f"Modelin doğruluk oranı: {accuracy}")

#veriyi kullanıcıdan almalı örnek
yas = int(input("Yaşınızı giriniz: "))
kanBasinci = int(input("Kan basıncınızı giriniz: "))
kolesterol = int(input("YKolesterol seviyenizi giriniz: "))

#tahmin oluştur

kullaniciVerisi = pd.DataFrame([[yas,kanBasinci,kolesterol]], columns=["Yaş","Kan_Basıncı","Kolesterol"])
tahmin = classifier.predict(kullaniciVerisi)
sonuc = "Hastalık var" if tahmin[0] == 1 else "Hastalık yok"
print(f"Tahmin : {sonuc}")




