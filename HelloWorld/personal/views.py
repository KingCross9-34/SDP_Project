from django.shortcuts import render
import pandas as pd
from django.http import HttpResponse
import json
# Create your views here.


#http://127.0.0.1:8000/personal/getUserById/id
#按照id搜索单个用户
def getUser(request,id):
    print(request)
    data=pd.read_csv('static/data.csv',nrows=8000)
    tmp=data.loc[id]
    result=tmp.to_json(orient="index")
    parsed = json.loads(result)
    
    return HttpResponse(json.dumps(parsed)) #返回该用户的所有信息


