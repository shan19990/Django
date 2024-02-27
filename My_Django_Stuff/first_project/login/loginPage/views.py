from django.shortcuts import render
from loginPage.forms import FormLogin,RegisterAccount
from loginPage.models import loginCredential,AccountDetails

# Create your views here.

def login(request):
    if request.method == 'POST':
        form = FormLogin(request.POST)
        if form.is_valid():
            userId = form.cleaned_data['userId']
            password = form.cleaned_data['password']
            # Check if user exists
            if loginCredential.objects.filter(userId=userId, password=password).exists():
                print("User is here")
            else:
                print("User is not here")
    else:
        form = FormLogin()
    return render(request,"loginPage/login.html",{'form':form})

def register(request):
    if request.method == 'POST':
        form = RegisterAccount(request.POST)
        if form.is_valid():
            userId = form.cleaned_data['userId']
            password = form.cleaned_data['password']
            age = form.cleaned_data['age']
            name = form.cleaned_data['name']
            dob = form.cleaned_data['dob']
            login_details = loginCredential.objects.create(userId=userId,password=password)
            account_details = AccountDetails.objects.create(userId=login_details,name=name, age=age,dob=dob)
            
    else:
        form = RegisterAccount()
    return render(request,"loginPage/register.html",{'form':form})