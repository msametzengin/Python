import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

#veriyi hazırlama

data = {
    'Ev_Büyüklügü':[120,250,175,300,220],
    'Oda_Sayisi':[3,5,4,6,4],
    'Fiyat':[2400000,5000000,3500000,6000000,4400000]
}

df = pd.DataFrame(data) # veriyi df'e çevirme

X = df[['Ev_Büyüklügü','Oda_Sayisi']]
y = df['Fiyat']

#%20 test %80 eğit
X_train, X_test, y_train, y_test = train_test_split(X,y , test_size=0.2 , random_state=42)

model = LinearRegression()
model.fit(X_train,y_train)

# y_pred = model.predict(X_test)  #burası test yeri
# mse = mean_squared_error(y_test, y_pred)
# rmse = np.sqrt(mse)
# print(f"Ortalama Kare Hatasi (MSE) {rmse}")

evBuyuklugu = float(input("Lütfen evin büyüklüğünü metrekare cinsinden giriniz: "))
odaSayisi = int(input("Lütfen oda sayisini giriniz: "))

tahminiFiyat = model.predict([[evBuyuklugu,odaSayisi]])
print(f"Bu evin tahmini fiyatı {tahminiFiyat[0]:.2f} TL")