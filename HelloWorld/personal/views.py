from django.http.response import JsonResponse
from django.shortcuts import render
import pandas as pd
from django.http import HttpResponse
import json
import joblib
# Create your views here.


#http://127.0.0.1:8000/personal/getUserById/id
#按照id搜索单个用户
def getUser(request,id):
    data=pd.read_csv('static/data.csv')
    tmp=data.loc[id]
    result=tmp.to_json(orient="index")
    parsed = json.loads(result)
    
    return HttpResponse(json.dumps(parsed)) #返回该用户的所有信息


def predict_svm(request):
    id=int(request.POST['id'])
    data=pd.read_csv('static/final.csv')
    svm=joblib.load('static/model/svm.pkl')
    x=data.loc[id]
    result=svm.predict([x.to_numpy()])[0]
    object={
        'risk':int(result)
    }
    return JsonResponse(object)


def predict_mlp(request):
    id=int(request.POST['id'])
    data=pd.read_csv('static/final.csv')
    mlp=joblib.load('static/model/mlp.pkl')
    x=data.loc[id]
    result=mlp.predict([x.to_numpy()])[0]
    object={
        'risk':int(result)
    }
    return JsonResponse(object)
    
    



def predict_logictic(request):
    id=int(request.POST['id'])
    data=pd.read_csv('static/final.csv')
    logictic=joblib.load('static/model/logisticRegression.pkl')
    x=data.loc[id]
    result=logictic.predict([x.to_numpy()])[0]
    object={
        'risk':int(result)
    }
    return JsonResponse(object)
    
