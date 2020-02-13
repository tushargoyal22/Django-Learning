from django.shortcuts import render
from django.urls import path
from auth import views
# Create your views here.

urlpatterns = [
    path('login/' , views.Login.as_view()),
    path('logout/' , views.Logout.as_view())

]