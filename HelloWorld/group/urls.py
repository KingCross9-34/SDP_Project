from django.urls import path

from . import views

urlpatterns = [
    path('pubRec',views.pubRec),
    path('region',views.region),path('empTime',views.empTime),
    path('dti',views.dti),path('acc_open',views.acc_open),
    path('home_ownership',views.home_ownership),
    path('avg_cur_bal',views.avg_cur_bal)
]