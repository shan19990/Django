from django.shortcuts import render,redirect
from login.forms import LoginForm
from django.contrib.auth import authenticate,login,logout
from login.forms import RegisterForm

def loginView(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            userName = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            print(userName)
            print(password)
            user = authenticate(request,username = userName, password=password)
            if user is not None:
                login(request,user)
                print("success")
                return redirect("marketplace")
            else:
                print("fail")
    else:
        form = LoginForm()
    return render(request,"login/login.html",{"form":form})     

def registerUser(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            print('account registered')
        else:
            print('cannot register')
    else:
        form = RegisterForm()
    return render(request,"login/register.html",{"form":form})