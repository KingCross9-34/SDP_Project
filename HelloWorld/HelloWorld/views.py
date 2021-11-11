from django.shortcuts import render
import pandas as pd
from django.http import HttpResponse
import json
# Create your views here.
 
#10000个用户数据

#1.用户信息
#post{data:id}
#http://localhost:8000/userInfo
#按照id搜索单个用户
def getUserInfo(request):
    id=int(request.POST['id'])
    if id>=10000:
        response={'status':404}
        return_json=json.dumps(response)
        return HttpResponse(return_json)
 
    data=pd.read_csv('static/data.csv',nrows=10000)
    userInfo=data.loc[id]
    #result=userInfo.to_json(orient="index")
    #parsed = json.loads(result) #object
    result={
    'emp_title':userInfo['emp_title'],'emp_length':userInfo['emp_length'],
    'annual_inc':userInfo['annual_inc'],'home_ownership':userInfo['home_ownership']
    }
    result_object={'data':result,'status':200}
    result_json=json.dumps(result_object)
    return HttpResponse(result_json) #返回该用户的所有信息




#用户标签
#post{data:id}
#http://localhost:8000/userTags
def getUserTags(request):
    id=int(request.POST['id'])
    if id>=10000:
        response={'status':404}
        return_json=json.dumps(response)
        return HttpResponse(return_json)
    
    data=pd.read_csv('static/data.csv',nrows=10000)
    #未决定标签
    result={'data':[
        {
			"key": 0,
			"label": ""
		},
		{
			"key": 1,
			"label": ""
		},
		{
			"key": 2,
			"label": ""
		}
        ]}
    result_json=json.dumps(result)
    return HttpResponse(result_json)
    

#3.贷款信息
#post{data:id}
#http://localhost:8000/loanInfo
def getLoanInfo(request):
    id=int(request.POST['id'])
    if id>=10000:
        result_object={'status':404}
        return_json=json.dumps(result_object)
        return HttpResponse(return_json)
 
    data=pd.read_csv('static/data.csv',nrows=10000)
    userInfo=data.loc[id]
    loanData={
        "delinq_2yrs": userInfo["delinq_2yrs"],
		"pub_rec": userInfo["pub_rec"],
		"all_util": userInfo["all_util"],
		"revol_bal": userInfo["revol_bal"],
		"dti": userInfo["dti"],
		"delinq_amnt": userInfo["delinq_amnt"],
		"acc_now_delinq": userInfo["acc_now_delinq"],
		"loan_status": userInfo["loan_status"]
    }
    result_object={'data':loanData,'status':200}
    result_json=json.dumps(result_object)
    return HttpResponse(result_json)


#4.风险预测
#post{data:id}
#http://localhost:8000/riskProfile
def getRiskProfile(request):
    id=int(request.POST['id'])
    if id>=10000:
        result_object={'status':404}
        return_json=json.dumps(result_object)
        return HttpResponse(return_json)
 
    data=pd.read_csv('static/data.csv',nrows=10000)
    userInfo=data.loc[id]
    gradeData={
        'grade':userInfo['grade']
    }
    result_object={'data':gradeData,'status':200}
    result_json=json.dumps(result_object)
    return HttpResponse(result_json)



