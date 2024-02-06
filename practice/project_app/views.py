from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hellow WOrld!")

def index(request):
    help_dict = {"insert":"Index Page"}
    return render(request,'index.html',context=help_dict)
