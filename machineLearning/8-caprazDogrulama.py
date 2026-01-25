import pandas as pd
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


df = pd.read_excel("karar_agaci_veri_100.xlsx")

X = df[["Yas","Kan_Basinci","Kolesterol"]] #Girdi 
y = df["Hastalik"]                         #Çıktı

# X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

#karar ağacı sıfırlandırıcısını oluşturma ve eğitme
# classifier = DecisionTreeClassifier()
# classifier.fit(X_train,y_train)

#test verisi ile tahmin yapma
# y_pred = classifier.predict(X_test)

#modelin doğruluğunu ölçme
# accuracy = accuracy_score(y_test,y_pred)
# print(f"Modelin doğruluk oranı: {accuracy}")

classifier = DecisionTreeClassifier(max_depth=1,min_samples_split=2,min_samples_leaf=2)
classifier.fit(X,y)
# cross_value_scor = cross_val_score(classifier,X,y,cv=5) # üstteki şey 1 kere fakat çapraz doğrulama 5 kere yapıyor.

# print(f"5-Katlamalı Çapraz Doğrulama Skorları: {cross_value_scor}")
# print(f"Ortalama doğruluk skoru: {cross_value_scor.mean():.2f}")

#kullanıcıdan veri alalım
print("Lütfen tahmin için aşağıdaki bilgileri giriniz: ")
yas = int(input("Yaş: "))
kanBasinci = float(input("Kan basıncı: "))
kolesterol = float(input("Kolesterol: "))

#kullanıcıdan alınan veriyi moelin anlayacağı formata çevirelim
yeniVeri = pd.DataFrame([[yas,kanBasinci,kolesterol]], columns=["Yas","Kan_Basinci","Kolesterol"])
tahmin = classifier.predict(yeniVeri)

#Tahmin sonucunu göster
if tahmin[0] == 1:
    print("Tahmin: Hastalık var")
else:
    print("Tahmin: Hastalık yok")

