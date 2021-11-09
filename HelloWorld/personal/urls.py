from django.urls import path

from . import views

urlpatterns = [
    path('getUserById/<int:id>',views.getUser)
]