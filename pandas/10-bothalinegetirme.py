import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

#Ornek veri
df = pd.read_excel('teknolojik_urunler_zamanli.xlsx')
df['Tarih'] = pd.to_datetime(df['Tarih'])
df.set_index('Tarih',inplace = True)

#menu fonksiyonu
def menu():
    print("Grafik seçenekleri: ")
    print("1. Satışların  zaman içindeki değişimi (Çizgi Grafik)")
    print("2. Aylık toplam satışlar (Bar Grafik)")
    print("3. Kategorilere göre satış dağılımı (Pasta Grafik)")
    print("4. Fiyat ve satış ilişkisi (Scatter Plot)")
    print("5. Fiyat dağılımı (Histogram)")
    print("6. Aylık satış miktarları (Çizgi Grafik)")
    print("7. Fiyat kategorisine göre toplam satışlar (Bar Grafik)")
    print("0. Çıkış.")

    return int(input("Seçiminizi yapın: "))

def ekranTemizleme():
    if os.name=="nt":
        os.system("cls")
    else:
        os.system("clear")


#kullanıcının seçimine göre ilgili işlemleri yapan fonksiyon

def grafikSeçim(secilen):

    if secilen == 1:
        #Çizgi Grafik
        df['Satış'].plot(title='Satışların zaman içindeki değişimi', xlabel='Tarih', ylabel='Satış Miktarı')
        plt.show()
    elif secilen ==2:
        #Scatter plot
        aylikSatis = df.resample('ME')['Satış'].sum()
        aylikSatis.plot(kind='bar', title='Aylık Toplam Satışlar',xlabel='Ay',ylabel='Toplam Satış')
        plt.show()
    elif secilen ==3:
        #Pasta grafiği
        kategoriSatis = df.groupby('Kategori')['Satış'].sum()
        kategoriSatis.plot(kind='pie',autopct='%1.1f%%', title='Kategorilere göre satış dağılımı')
        plt.ylabel('') #y eksenini gizleme
        plt.show()
    elif secilen==4:
        df.plot(kind='scatter', x='Fiyat (TL)',y='Satış',title='Fiyat ve Satış ilişkisi')
        z = np.polyfit(df['Fiyat (TL)'], df['Satış'], 1)
        p = np.poly1d(z)
        plt.plot(df['Fiyat (TL)'], p(df['Fiyat (TL)']), color='red')
        plt.show()
    elif secilen==5:
        # histogram
        df['Fiyat (TL)'].plot(kind='hist', bins=10 , title='Fiyat Dagilimi')
        plt.xlabel('Fiyat (TL)')
        plt.show()
    elif secilen==6:
        #aylik satis trendi
        aylikSatis = df.resample('ME')['Satış'].sum()
        aylikSatis.plot(kind='line',title="Aylık Satış Miktarları")
        plt.xlabel('Ay')
        plt.ylabel('Satış Miktarı')
        plt.show()
    elif secilen==7:
        #önemli 
        bins = [0,2000,5000,10000,20000,30000]
        labels = ['Düşük','Orta','Yüksek','Çok yüksek','Lüks']
        df['Fiyat Kategorisi'] = pd.cut(df['Fiyat (TL)'], bins = bins , labels = labels)
        # fiyat kategorisine göre satış dağılımı
        df.groupby('Fiyat Kategorisi')['Satış'].sum().plot(kind='bar',title='Fiyat Kategorisine Göre Toplam Satışlar')
        plt.xlabel('Fiyat Kategorisi')
        plt.ylabel('Toplam Satış')
        plt.show()

while True:
    ekranTemizleme()
    secim = menu()
    if secim == 0:
        print("Çıkış yapılıyor...")
        break
    elif 1 <= secim <= 7:
        grafikSeçim(secim)
    else:
        print("Geçersiz bir seçim yaptınız.")

