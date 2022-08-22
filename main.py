import numpy as np
import pandas as pd
import matplotlib.pyplot


veriler = pd.read_csv('veriler.csv')

print(veriler)


ulke = veriler.iloc[:,0:1].values
print(ulke)

from sklearn import preprocessing

le = preprocessing.LabelEncoder()

ulke[:,0] = le.fit_transform(veriler.iloc[:,0])
print(ulke)

ohe = preprocessing.OneHotEncoder()

ulke = ohe.fit_transform(ulke).toarray()
print(ulke)


c = veriler.iloc[:,-1:].values
print(ulke)

from sklearn import preprocessing

le = preprocessing.LabelEncoder()

c[:,-1] = le.fit_transform(veriler.iloc[:,-1])
print(c)

ohe = preprocessing.OneHotEncoder()

c = ohe.fit_transform(c).toarray()
print(c)


sonuc = pd.DataFrame(data = ulke, index=range(22), columns = ['fr', 'tr', 'us'])
print(sonuc)

sonuc2 = pd.DataFrame(data = Yas, index=range(22), columns=['boy','kilo','yas'])
print(sonuc2)

cinsiyet = veriler.iloc[:,-1].values
print(cinsiyet)

sonuc3 = pd.DataFrame(data =c[:,:1], index = range(22), columns = ['cinsiyet'])
print(cinsiyet)




#dataframe birleştirme işlemi
s = pd.concat([sonuc,sonuc2],axis = 1)
print(s)

s2 = pd.concat([s,sonuc3], axis = 1) # concat fonksiyonu ile dataframeleri birleştiriyoruz
print(s2)