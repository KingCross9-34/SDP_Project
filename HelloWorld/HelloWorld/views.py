from django.shortcuts import render
import pandas as pd
from django.http import HttpResponse,JsonResponse
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
        return JsonResponse(response)
 
    data=pd.read_csv('static/data.csv',nrows=10000)
    userInfo=data.loc[id]
    #result=userInfo.to_json(orient="index")
    #parsed = json.loads(result) #object
    result={
    'emp_title':userInfo['emp_title'],'emp_length':userInfo['emp_length'],
    'annual_inc':userInfo['annual_inc'],'home_ownership':userInfo['home_ownership'],'loan_amnt':userInfo['loan_amnt']
    }
    result_object={'data':result,'status':200}
    return JsonResponse(result_object)




#用户标签
#post{data:id}
#http://localhost:8000/userTags
def getUserTags(request):
    id=int(request.POST['id'])
    if id>=10000:
        response={'status':404}
        return JsonResponse(response)
    
    data=pd.read_csv('static/data.csv',nrows=10000)
    userInfo=data.loc[id]
    #未决定标签
    incomeTag=''
    if userInfo['annual_inc']==0:
        incomeTag='无收入'
    elif userInfo['annual_inc']<=50000:
        incomeTag='低收入'
    elif 50000<userInfo['annual_inc']<=100000:
        incomeTag='中等收入'
    elif 100000<userInfo['annual_inc']<=150000:
        incomeTag='高收入'
    elif userInfo['annual_inc']>150000:
        incomeTag='极高收入'
    
    
    result={'data':[
        {
			"key": '收入等级',
			"label": incomeTag
		},
		{
			"key": '住房情况',
			"label": userInfo['home_ownership']
		},
		{
			"key": 2,
			"label": ""
		}
        ]}
    result_json=json.dumps(result)
    return HttpResponse(result_json)
    

#3.违约信息
#post{data:id}
#http://localhost:8000/loanDefault
def getLoanDefault(request):
    id=int(request.POST['id'])
    if id>=10000:
        response={'status':404}
        return JsonResponse(response)
 
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
    return JsonResponse(result_object)

#3.贷款情况
#http://localhost:8000/loanInfo
def getLoanInfo(request):
    id=int(request.POST['id'])
    if id>=10000:
        response={'status':404}
        return JsonResponse(response)
 
    data=pd.read_csv('static/data.csv',nrows=10000)
    userInfo=data.loc[id]
    loanData={
        "loan_amnt": userInfo["loan_amnt"],
		"term": userInfo["term"],
		"int_rate": userInfo["int_rate"],
		"installment": userInfo["installment"],
		"dti": userInfo["dti"],
		"loan_status": userInfo["loan_status"],
		"purpose": userInfo["purpose"],
		"revol_bal": userInfo["revol_bal"],
        "total_pymnt": userInfo["total_pymnt"],
		"issue_d": userInfo["issue_d"]
    }
    result_object={'data':loanData,'status':200}
    return JsonResponse(result_object)


#4.风险预测
#post{data:id}
#http://localhost:8000/riskProfile
def getRiskProfile(request):
    id=int(request.POST['id'])
    if id>=10000:
        response={'status':404}
        return JsonResponse(response)
 
    data=pd.read_csv('static/data.csv',nrows=10000)
    userInfo=data.loc[id]
    gradeData={
        'grade':userInfo['grade']
    }
    result_object={'data':gradeData,'status':200}
    return JsonResponse(result_object)



