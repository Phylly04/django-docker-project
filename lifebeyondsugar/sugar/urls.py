from django.contrib import admin
from django.urls import path
from .import views

app_name = 'sugar'

urlpatterns = [
    path('', views.home, name= 'base'),
    path('home/', views.home, name='home'),
    path('user_login/', views.user_login, name='user_login'),
    path('registration/',views.registration, name='registration'),
    path('about/', views.about, name='about'),
    path('quiz/', views.quiz, name='quiz'),
    path('accounts/login/', views.login_view, name='login')
    
]
