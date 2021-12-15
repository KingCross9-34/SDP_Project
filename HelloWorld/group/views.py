from django.shortcuts import render
import pandas as pd
from django.http import HttpResponse,JsonResponse

# Create your views here.

#pubRec数据
def pubRec(request):
    data=pd.read_csv('static/data.csv',nrows=10000)
    pubRec_count=data['pub_rec'].value_counts().values.tolist()
    result={
        'data':[
                {
                'class':1,
                'pubRec':[0],'amount':[pubRec_count[0]]
                },
                {
                'class':2,
                'pubRec':[1],'amount':[pubRec_count[1]]
                },
                {
                'class':3,
                'pubRec':[2,3,4],'amount':pubRec_count[2:5]
                },
                {
                'class':4,
                'pubRec':[5,6,7,8,9,10],'amount':pubRec_count[5:]
                }
        
        ]
    }
    return JsonResponse(result)


#按地区分组
def region(request):
    result_data=pubRec_func('addr_state')
    result={
        'data':result_data
    }
    return JsonResponse(result)

#按工作时长分组
def empTime(request):
    result_data=pubRec_func('emp_length')
    result={
        'data':result_data
    }
    return JsonResponse(result)

#按债务收入比分组
def dti(request):
    data=pd.read_csv('static/data.csv',nrows=10000)
    ran=[[0,1],[1,5],[5,10],[10,20],[20,50],[50,1000]]#设定的dti范围分类
    result_data=[]
    for r in ran:
        pubRec_dti=data[(data['dti']>=r[0]) & (data['dti']<r[1])]#取出该范围的所有行
        pubRec_index=pubRec_dti['pub_rec'].value_counts().index.tolist()#index--pub_rec的值
        pubRec_count=pubRec_dti['pub_rec'].value_counts()#按照pubRec分类
        #补全
        for i in range(11):
            if i not in pubRec_index:
                pubRec_count.loc[i]=0
        
        pubRec_count=pubRec_count.sort_index().values.tolist()
        tmp={
                'dti':r,
                'pubRec':[{
                'class':1,
                'pubRec':[0],'amount':[pubRec_count[0]]
                },
                {
                'class':2,
                'pubRec':[1],'amount':[pubRec_count[1]]
                },
                {
                'class':3,
                'pubRec':[2,3,4],'amount':pubRec_count[2:5]
                },
                {
                'class':4,
                'pubRec':[5,6,7,8,9,10],'amount':pubRec_count[5:]
                }]
        }
        result_data.append(tmp)

    result={
        'data':result_data
    }
    return JsonResponse(result)

#home_ownership  
def home_ownership(request):
    result_data=pubRec_func('home_ownership')
    result={
        'data':result_data
    }
    return JsonResponse(result)


#acc_open_past_24mths  
def acc_open(request):
    data=pd.read_csv('static/data.csv',nrows=10000)
    ran=[[0,2],[2,4],[4,5],[5,10],[10,31]]#设定的acc范围分类
    result_data=[]
    for r in ran:
        pubRec_acc=data[(data['acc_open_past_24mths']>=r[0]) & (data['acc_open_past_24mths']<r[1])]#取出该范围的所有行
        pubRec_index=pubRec_acc['pub_rec'].value_counts().index.tolist()#index--pub_rec的值
        pubRec_count=pubRec_acc['pub_rec'].value_counts()#按照pubRec分类
        #补全
        for i in range(11):
            if i not in pubRec_index:
                pubRec_count.loc[i]=0
        
        pubRec_count=pubRec_count.sort_index().values.tolist()
        tmp={
                'acc_open_past_24mths':r,
                'pubRec':[{
                'class':1,
                'pubRec':[0],'amount':[pubRec_count[0]]
                },
                {
                'class':2,
                'pubRec':[1],'amount':[pubRec_count[1]]
                },
                {
                'class':3,
                'pubRec':[2,3,4],'amount':pubRec_count[2:5]
                },
                {
                'class':4,
                'pubRec':[5,6,7,8,9,10],'amount':pubRec_count[5:]
                }]
        }
        result_data.append(tmp)

    result={
        'data':result_data
    }
    return JsonResponse(result)

#avg_cur_bal  
def avg_cur_bal(request):
    data=pd.read_csv('static/data.csv',nrows=10000)
    #50000一个间隔
    ran=[[0,10000],[10000,30000],[30000,100000],[100000,203201]]#设定的avg_cur_bal范围分类
    result_data=[]
    for r in ran:
        pubRec_avg=data[(data['avg_cur_bal']>=r[0]) & (data['avg_cur_bal']<r[1])]#取出该范围的所有行
        pubRec_index=pubRec_avg['pub_rec'].value_counts().index.tolist()#index--pub_rec的值
        pubRec_count=pubRec_avg['pub_rec'].value_counts()#按照pubRec分类
        #补全
        for i in range(11):
            if i not in pubRec_index:
                pubRec_count.loc[i]=0
        
        pubRec_count=pubRec_count.sort_index().values.tolist()
        tmp={
                'avg_cur_bal':r,
                'pubRec':[{
                'class':1,
                'pubRec':[0],'amount':[pubRec_count[0]]
                },
                {
                'class':2,
                'pubRec':[1],'amount':[pubRec_count[1]]
                },
                {
                'class':3,
                'pubRec':[2,3,4],'amount':pubRec_count[2:5]
                },
                {
                'class':4,
                'pubRec':[5,6,7,8,9,10],'amount':pubRec_count[5:]
                }]
        }
        result_data.append(tmp)

    result={
        'data':result_data
    }
    return JsonResponse(result)

#业务建议


#tool
#按照某个特征进行分组
def pubRec_func(fea):
    data=pd.read_csv('static/data.csv',nrows=10000)
    feaList=data[fea].value_counts().index.tolist()
    result_data=[]
    for feaItem in feaList:
        pubRec_fea=data[data[fea]==feaItem] #取出该地址的所有行
        pubRec_index=pubRec_fea['pub_rec'].value_counts().index.tolist()#index--pub_rec的值
        pubRec_count=pubRec_fea['pub_rec'].value_counts()#按照pubRec分类
        #补全
        for i in range(11):
            if i not in pubRec_index:
                pubRec_count.loc[i]=0
        pubRec_count=pubRec_count.sort_index().values.tolist()
        tmp={
                fea:feaItem,
                'pubRec':[{
                'class':1,
                'pubRec':[0],'amount':[pubRec_count[0]]
                },
                {
                'class':2,
                'pubRec':[1],'amount':[pubRec_count[1]]
                },
                {
                'class':3,
                'pubRec':[2,3,4],'amount':pubRec_count[2:5]
                },
                {
                'class':4,
                'pubRec':[5,6,7,8,9,10],'amount':pubRec_count[5:]
                }]
        }
        result_data.append(tmp)
    return result_data



    '''
#按地区分组
def region(request):
    data=pd.read_csv('static/data.csv',nrows=10000)
    class_=[[0],[1],[2,3,4],[5,6,7,8,9,10]]#pubRec分类
    regionList=data['addr_state'].value_counts().index.tolist() #所有的region
    result_data=[]
    for addr in regionList:
        pubRec_region=data[data['addr_state']==addr] #取出该地址的所有行
        pubRec_index=pubRec_region['pub_rec'].value_counts().index.tolist()#index--pub_rec的值
        pubRec_count=pubRec_region['pub_rec'].value_counts()#按照pubRec分类
        #补全
        for i in range(11):
            if i not in pubRec_index:
                pubRec_count.loc[i]=0
        pubRec_count=pubRec_count.sort_index().values.tolist()
        tmp={
                'region':addr,
                'pubRec':[{
                'class':1,
                'pubRec':[0],'amount':[pubRec_count[0]]
                },
                {
                'class':2,
                'pubRec':[1],'amount':[pubRec_count[1]]
                },
                {
                'class':3,
                'pubRec':[2,3,4],'amount':pubRec_count[2:5]
                },
                {
                'class':4,
                'pubRec':[5,6,7,8,9,10],'amount':pubRec_count[5:]
                }]
        }
        result_data.append(tmp)
    print(result_data)
    result={
        'data':result_data
    }
    return JsonResponse(result)
'''


'''
#按工作时长分组
def empTime(request):
    data=pd.read_csv('static/data.csv',nrows=10000)
    empTimeList=data['emp_length'].value_counts().index.tolist()
    result_data=[]
    for emptime in empTimeList:
        pubRec_region=data[data['emp_length']==emptime] #取出该地址的所有行
        pubRec_index=pubRec_region['pub_rec'].value_counts().index.tolist()#index--pub_rec的值
        pubRec_count=pubRec_region['pub_rec'].value_counts()#按照pubRec分类
        #补全
        for i in range(11):
            if i not in pubRec_index:
                pubRec_count.loc[i]=0
        pubRec_count=pubRec_count.sort_index().values.tolist()
        tmp={
                'empTime':emptime,
                'pubRec':[{
                'class':1,
                'pubRec':[0],'amount':[pubRec_count[0]]
                },
                {
                'class':2,
                'pubRec':[1],'amount':[pubRec_count[1]]
                },
                {
                'class':3,
                'pubRec':[2,3,4],'amount':pubRec_count[2:5]
                },
                {
                'class':4,
                'pubRec':[5,6,7,8,9,10],'amount':pubRec_count[5:]
                }]
        }
        result_data.append(tmp)
    result={
        'data':result_data
    }
    return JsonResponse(result)
'''
