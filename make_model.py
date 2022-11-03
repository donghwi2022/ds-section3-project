import pandas as pd
from dotenv import load_dotenv
from pymongo import MongoClient
import os
from sklearn.linear_model import LinearRegression
import pickle

load_dotenv()
# 데이터 불러오기
HOST = 'cluster0.z2k4w6q.mongodb.net'
USER = 'donghwi'
PASSWORD = os.environ.get('PASSWORD')
DATABASE_NAME = 'Project'
COLLECTION_NAME = 'weather'
MONGO_URI = f"mongodb+srv://{USER}:{PASSWORD}@{HOST}/{DATABASE_NAME}?retryWrites=true&w=majority"

client = MongoClient(MONGO_URI)
database = client[DATABASE_NAME]
collection = database[COLLECTION_NAME]

data = collection.find_one()

# 전처리 진행
df = pd.json_normalize(data['item'])
df = df.astype({'temp':'float', 'humi':'float', 'rainProb':'float', 'windSpeed':'float'})

# 머신러닝 진행
model = LinearRegression()

features = ['temp', 'humi', 'windSpeed']
target = 'rainProb'
X_train = df[features]
y_train = df[target]

model.fit(X_train, y_train)

# 머신러닝 모델 인코딩
with open('model.pkl','wb') as pickle_file:
    pickle.dump(model, pickle_file)
