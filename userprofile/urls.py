from django.urls import path
from . import views
from fastapi_app import main

urlpatterns = [
    path('', views.home,name='home'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.Userlogout, name='logout'),
    path('registration/', views.registration, name='register'),

]
