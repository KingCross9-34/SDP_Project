from django.shortcuts import render
import pandas as pd
from django.http import JsonResponse
import numpy as np
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
    emp_title=userInfo['emp_title']
    emp_length=userInfo['emp_length']
    if pd.isna(emp_title):
        emp_title=""
        emp_length=""
    
    acc_open_past_24mths=userInfo['acc_open_past_24mths']
    inq_last_12m=userInfo['inq_last_12m']
    inq_last_6mths=userInfo['inq_last_6mths']
    if np.isnan(acc_open_past_24mths):
        acc_open_past_24mths=''
    if np.isnan(inq_last_12m):
        inq_last_12m=''
    if np.isnan(inq_last_6mths):
        inq_last_6mths=''

    tags=userInfo['DIYTags']
    if pd.isna(tags):
        tags=''
    print('tags:',tags)
    result={
    'emp_title':emp_title,
    'emp_length':emp_length,
    'annual_inc':userInfo['annual_inc'],
    'home_ownership':userInfo['home_ownership'],
    'loan_amnt':userInfo['loan_amnt'],
    'id':id,
    "acc_open_past_24mths": acc_open_past_24mths,
	"inq_last_12m": inq_last_12m,
	"inq_last_6mths": inq_last_6mths,
	"addr_state": userInfo["addr_state"],
    'DIYTags':tags.split()
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
    
    #标签
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

    chargeoff_within_12_mths_Tag='少'
    if userInfo['chargeoff_within_12_mths']!=0:
        chargeoff_within_12_mths_Tag='多'
    
    acc_open_past_24mths_Tag='交易数量中等'
    if userInfo['acc_open_past_24mths']<=5:
        acc_open_past_24mths_Tag='交易数量少'
    elif userInfo['acc_open_past_24mths_Tag']>=10:
        acc_open_past_24mths_Tag='交易频繁'

    acc_now_delinq_Tag='无逾期账户'
    if userInfo['acc_now_delinq']>=1:
        acc_now_delinq_Tag='逾期账户多'

    result={
        'data':{
        'annual_inc':{
            'annual_inc':userInfo['annual_inc'],
            'incomeTag':incomeTag,
            'rank':data[data['annual_inc']<userInfo['annual_inc']].shape[0]/10000 #排名
            },
        'acc_open_past_24mths':{
            'acc_open_past_24mths':userInfo['acc_open_past_24mths'],
            'Tag':acc_open_past_24mths_Tag
            },
        'acc_now_delinq':{
            'acc_now_delinq':userInfo['acc_now_delinq'],
            'Tag':acc_now_delinq_Tag
            },
        'chargeoff_within_12_mths':{
            'chargeoff_within_12_mths':userInfo['chargeoff_within_12_mths'],
            'Tag':chargeoff_within_12_mths_Tag        
            },
        'home_ownership': userInfo['home_ownership'],
        'addr_state': userInfo['addr_state'],
        'all_util':userInfo['all_util'],
        'delinq_2yrs':userInfo['delinq_2yrs'],
        'delinq_amnt':userInfo['delinq_amnt'],
        'dti':userInfo['dti'],
        'emp_length':userInfo['emp_length'],
        'emp_title':userInfo['emp_title'],
        'loan_status':userInfo['loan_status'],
        'pct_tl_nvr_dlq':userInfo['pct_tl_nvr_dlq'],
        'pub_rec':userInfo['pub_rec'],
        'revol_bal':userInfo['revol_bal'],
        'hardship_flag':userInfo['hardship_flag'],
        'hardship_type':userInfo['hardship_type'],
        'disbursement_method':userInfo['disbursement_method'],
        'settlement_status':userInfo['settlement_status']		
        }
        }
    return JsonResponse(result)
    

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


#post tags
def DIYTags(request): 
    json_data=json.loads(request.body.decode('utf-8'))
    id=json_data['id']
    tags=json_data['tags']
    tags_string=' '.join(tags)
    data=pd.read_csv('static/data.csv',nrows=10000)
    data.loc[id,'DIYTags']=tags_string
    data.to_csv('static/data.csv')

    return_object={
        'id':id,
        'tags':data.loc[id,'DIYTags'].split()
    }
    return JsonResponse(return_object) 


    


def test(request):
    print(request)
    return JsonResponse(1)
