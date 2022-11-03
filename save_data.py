import requests
import xmltodict, json
from dotenv import load_dotenv
from pymongo import MongoClient
import os

load_dotenv()
# api로 데이터 불러오기
serviceKey = os.environ.get('serviceKey')
url = 'http://apis.data.go.kr/3160000/guroPointFocInfoSvc/getGuro10PointFocInfoSvc'
params ={'serviceKey' : serviceKey, 'returnType' : 'xml', 'numOfRows' : '1000', 'pageNo' : '1'}
response = requests.get(url, params=params)

# json 형태로 데이터 변경
parse_data = xmltodict.parse(response.content) 
json_data = json.loads(json.dumps(parse_data))

# 몽고DB에 데이터 저장
HOST = 'cluster0.z2k4w6q.mongodb.net'
USER = 'donghwi'
PASSWORD = os.environ.get('PASSWORD')
DATABASE_NAME = 'Project'
COLLECTION_NAME = 'weather'
MONGO_URI = f"mongodb+srv://{USER}:{PASSWORD}@{HOST}/{DATABASE_NAME}?retryWrites=true&w=majority"

client = MongoClient(MONGO_URI)
database = client[DATABASE_NAME]
collection = database[COLLECTION_NAME]

collection.delete_many({}) # 기존에 있는 데이터 삭제
collection.insert_one(json_data['response']['body']['items'])
