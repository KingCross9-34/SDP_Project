from django.urls import path

from . import views

urlpatterns = [
    path('pubRec',views.pubRec),
    path('region',views.region),path('empTime',views.empTime),
    path('dti',views.dti)
]