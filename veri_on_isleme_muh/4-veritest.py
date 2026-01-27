import pandas as pd
from sklearn.preprocessing import LabelEncoder,StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

#veriyi yükle
df=pd.read_excel('veri_on_isleme_ve_ozellik_muhendisligi.xlsx')

#cinsiyet ve gelirleri ortalama ile doldurmak
df.fillna(df['Gelir'].mean(),inplace=True)

#cinsiyet ve meslek sütunlarını sayısal hale getirelim.
le = LabelEncoder()
df['Cinsiyet'] = le.fit_transform(df['Cinsiyet'])
df['Meslek'] = le.fit_transform(df['Meslek'])

#giriş ve çıktı verilerini gir
X = df[['Yaş',"Meslek","Cinsiyet"]] #gelir
y = df['Gelir'] #çıktı

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

# ÖLÇEKLENDİRME
scaler = StandardScaler()
X_train= scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# #modeli oluştur ve eğit
linear_model=LinearRegression()
linear_model.fit(X_train,y_train)

# modeli test et ve tahmin yap
y_pred = linear_model.predict(X_test)

# performansını değerlendir
mse = mean_squared_error(y_test,y_pred)

# performansı değerlendir
rmse = mse ** 0.5 #kök ortalamasını al
print(f"Linear Reg RMSE: {rmse:.2f}")

# daha karmaşık bir model ile eğitim
rf_model = RandomForestRegressor(n_estimators=100,random_state=1)
rf_model.fit(X_train,y_train)
y_pred_rf = rf_model.predict(X_test)
mse_rf = mean_squared_error(y_test,y_pred_rf)
rmse_rf = mse_rf **0.5
print(f"Random Forest RMSE: {rmse_rf:.2f}")