# -*- coding: utf-8 -*-
"""empsalary.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1zhHJPUfb8ddnZbfCHhNaY212TuXpS6TR
"""

import pandas as pd

data=pd.read_csv("/content/drive/MyDrive/adult 3.csv")

from google.colab import drive
drive.mount('/content/drive')

data

data.shape

data.head(7)

data.tail(7)

data.isna()

data.isna().sum()

print(data.occupation.value_counts())

print(data.gender.value_counts())

print(data.education.value_counts())

print(data['marital-status'].value_counts())

print(data.workclass.value_counts())

data.occupation.replace({"?":"Others"},inplace=True)

print(data.occupation.value_counts())

data.workclass.replace({"?":"Not Listed"},inplace=True)

print(data.workclass.value_counts())

data=data[data['workclass']!='Without-pay']

print(data.workclass.value_counts())

data=data[data['workclass']!='Never-worked']

print(data.workclass.value_counts())

data.shape

data=data[data['education']!='1st-4th']
data=data[data['education']!='Preschool']
data=data[data['education']!='5th-6th']

print(data.education.value_counts())

data.shape

data.drop(columns=['education'],inplace=True)

data

import matplotlib.pyplot as plt
plt.boxplot(data['age'])
plt.show()

data=data[(data['age']<=75)&(data['age']>=17)]

plt.boxplot(data['age'])
plt.show()

from sklearn.preprocessing import LabelEncoder
encoder=LabelEncoder()
data['workclass']=encoder.fit_transform(data['workclass'])
data['marital-status']=encoder.fit_transform(data['marital-status'])
data['occupation']=encoder.fit_transform(data['occupation'])
data['relationship']=encoder.fit_transform(data['relationship'])
data['race']=encoder.fit_transform(data['race'])
data['gender']=encoder.fit_transform(data['gender'])
data['native-country']=encoder.fit_transform(data['native-country']) # Encode native-country
data

x=data.drop(columns=['income'])
y=data['income']

y

x

from sklearn.preprocessing import MinMaxScaler
scaler=MinMaxScaler()
x=scaler.fit_transform(x)
x

from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.2,random_state=23,stratify=y)

xtrain

from sklearn.neighbors import KNeighborsClassifier
knn=KNeighborsClassifier()
knn.fit(xtrain,ytrain)
predict=knn.predict(xtest)
predict

import sklearn.metrics as metrics
print(metrics.accuracy_score(ytest,predict))

from sklearn.linear_model import LogisticRegression
lr=LogisticRegression()
lr.fit(xtrain,ytrain)
predict1=lr.predict(xtest)
predict1

from sklearn.metrics import accuracy_score
print(accuracy_score(ytest,predict1))

from sklearn.neural_network import MLPClassifier
mlp=MLPClassifier(solver='adam',hidden_layer_sizes=(5,2),random_state=2,max_iter=2000)
mlp.fit(xtrain,ytrain)
predict2=mlp.predict(xtest)
predict2

from sklearn.metrics import accuracy_score
print(accuracy_score(ytest,predict2))

from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,classification_report
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier,GradientBoostingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler,OneHotEncoder

X_train,X_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=23,stratify=y)

models={
    "LogisticRegression":LogisticRegression(),
    "RandomForestClassifier":RandomForestClassifier(),
    "GradientBoostingClassifier":GradientBoostingClassifier(),
    "KNN":KNeighborsClassifier(),
    "SVC":SVC()
}

results={}
for model_name,model in models.items():
  pipe=Pipeline([
      ("scaler",StandardScaler()),
      ("model",model)
  ])
  pipe.fit(X_train,y_train)
  y_pred=pipe.predict(X_test)
  acc=accuracy_score(y_test,y_pred)
  results[model_name]=acc
  print(f"{model_name}:{acc}")
  print(classification_report(y_test,y_pred))

import matplotlib.pyplot as plt
plt.bar(results.keys(),results.values(),color="red")
plt.xlabel("Models")
plt.ylabel("Accuracy")
plt.title("Model Accuracy Comparison")
plt.xticks(rotation=45)
plt.grid(True)
plt.show()