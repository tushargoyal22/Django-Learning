from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_session
from django.http import HttpResponseRedirect
from auth import forms
from django.contrib.auth.views import LoginView,LogoutView

class Login(LoginView):
    template_name = 'auth/login.html'
    redirect_authenticated_user = True

class Logout(LogoutView):
    pass


def login(request):
    loginForm = forms.LoginForm()
    error=None

    if(request.method=='POST'):
        loginForm=forms.LoginForm(request.POST)
        if loginForm.is_valid():
            username=loginForm.cleaned_data['username']
            password=loginForm.cleaned_data['password']
            auth_user=authenticate(username=username,password=password)
        if(auth_user):
            login_session(request,auth_user)
            return HttpResponseRedirect('/')
        else:
            error = "Invalid Username or Password"


    context={
        "form": loginForm,
        "error": error
    }
    return render(request,'auth/login.html',context)