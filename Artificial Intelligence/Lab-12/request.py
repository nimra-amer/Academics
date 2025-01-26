import requests

url = 'http://localhost:5000/predict_api'

r = requests.post(url,json={'Pclass':1, 'Sex' : 0 , 'age':42, 'SibSp':1,'Parch':0,'Cabin':8 , 'Embarked':0})

print(r.json())