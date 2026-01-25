import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay


#veriyi hazırlama : yaş,kan basıncı, kolestrol ve hastalık durumu verileri
# data = {
#     'Yaş':[25,50,45,30,60],
#     'Kan_Basıncı':[120,140,130,110,150],
#     'Kolesterol': [180,240,200,160,220],
#     'Hastalik':[0,1,1,0,1] # 0 hayır saglam, 1 evet hasta
# }

# df = pd.DataFrame(data)

df = pd.read_excel("karar_agaci_veri_100.xlsx")

X = df[["Yas","Kan_Basinci","Kolesterol"]] #Girdi 
y = df["Hastalik"]                         #Çıktı

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

#karar ağacı sıfırlandırıcısını oluşturma ve eğitme
classifier = DecisionTreeClassifier()
classifier.fit(X_train,y_train)

#test verisi ile tahmin yapma
y_pred = classifier.predict(X_test)

cm = confusion_matrix(y_test,y_pred)

display = ConfusionMatrixDisplay(confusion_matrix=cm)

display.plot()
plt.title('Matrix - Karar Ağacı')
plt.show()