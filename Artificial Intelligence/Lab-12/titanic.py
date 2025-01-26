# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 03:02:18 2021

@author: Usman
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression 
from seaborn import load_dataset
import pickle


df=pd.read_csv("Titanic-Dataset.csv")
print(df.head())

df['Age'] = df['Age'].fillna(df['Age'].mode()[0])
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
df['Cabin'] = df['Cabin'].fillna(df['Cabin'].mode()[0])
df.isna().sum()

encoder = LabelEncoder()
df['Sex'] = encoder.fit_transform(df['Sex'])
df['Ticket'] = encoder.fit_transform(df['Ticket'])
df['Cabin'] = encoder.fit_transform(df['Cabin'])
df['Embarked'] = encoder.fit_transform(df['Embarked'])

Y = df['Survived']
X = df[['Pclass' , 'Sex' , 'Age' , 'SibSp' , 'Parch' , 'Cabin' , 'Embarked']]

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.3,random_state=101)
model = LogisticRegression()
model.fit(X_train , Y_train)

pickle.dump(model, open('model_titanic.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('model_titanic.pkl','rb'))

print(model.predict([[2, 1, 48,0,0 , 6 , 1]]))

