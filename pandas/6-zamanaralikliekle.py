import pandas as pd
import numpy as np
#exceli oku
df = pd.read_excel(r'd:\GitRepo\Python\pandas\teknolojik_urunler.xlsx')

df['Tarih'] = pd.to_datetime(np.random.choice(pd.date_range('2025-01-01','2025-12-31'), size=len(df)))

# print(df[['Ürün Adı','Tarih']])

# df.to_excel('teknolojik_urunler_zamanli.xlsx',index=False)
# print('Veri dosyaya aktarildi.')
