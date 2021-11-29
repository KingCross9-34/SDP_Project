from django.urls import path

from . import views

urlpatterns = [
    path('getUserById/<int:id>',views.getUser),
    path('svm_predict',views.predict_svm),
    path('mlp_predict',views.predict_mlp),
    path('logistic_predict',views.predict_logictic)

]