import pandas as pd
from sklearn.preprocessing import LabelEncoder,StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

#veriyi yükle
df=pd.read_excel('veri_on_isleme_ve_ozellik_muhendisligi.xlsx')

#cinsiyet ve gelirleri ortalama ile doldurmak
df.fillna(df['Gelir'].mean(),inplace=True)

#cinsiyet ve meslek sütunlarını sayısal hale getirelim.
le = LabelEncoder()
df['Cinsiyet'] = le.fit_transform(df['Cinsiyet'])
df['Meslek'] = le.fit_transform(df['Meslek'])

#giriş ve çıktı verilerini gir
X = df[['Yaş',"Meslek"]] #gelir
y = df['Gelir'] #çıktı

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

#modeli oluştur ve eğit
model=LinearRegression()
model.fit(X_train,y_train)

#modeli test et
accuracy = model.score(X_test,y_test)
print(f"Modelin doğruluk oranı: {accuracy*100:.2f}%")

#kullanıcıdan veri al
print("Lütfen tahmin için aşağıdaki bilgileri girinz...")
yas = int(input("Yaş: "))
meslek = input("Meslek {Mühendis, Doktor, Öğretmen, Avukat}: ")

#kullanıcıdan alınan mesleği kodlayalım (Label Encoding)
meslek_kod = le.transform([meslek])[0]

yeni_veri = pd.DataFrame([[yas,meslek_kod]],columns=["Yaş","Meslek"])
tahmin = model.predict(yeni_veri)
print(f"Tahmini ortalama maaş: {tahmin[0]:.2f} TL")
