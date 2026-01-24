import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

#veriyi hazırlama

data = {
    'Ev_Büyüklügü':[120,250,175,300,220],
    'Fiyat':[3000000,6000000,4000000,9000000,8000000]
}

df = pd.DataFrame(data) # veriyi df'e çevirme

X = df[['Ev_Büyüklügü']]
y = df['Fiyat']

#%20 test %80 eğit
X_train, X_test, y_train, y_test = train_test_split(X,y , test_size=0.2 , random_state=42)

#modeli oluştur

model = LinearRegression()
model.fit(X_train,y_train)

y_pred = model.predict(X_test)

#Hata ne kadar küçükse tahmin o kadar iyi
mse = mean_squared_error(y_test, y_pred)

rmse = np.sqrt(mse)
print(f"Ortalama Kare Hatasi (MSE) {rmse}")