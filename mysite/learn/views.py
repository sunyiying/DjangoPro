
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import  reverse
# Create your views here.

def index(request):
    return HttpResponse(u"欢迎学习django课程")

def add(request):
    # a=request.GET["a"]
    a=request.GET.get("a",0)
    b=request.GET.get("b",0)
    c=int(a)+int(b)
    return  HttpResponse("a+b={}".format(c))

def add2(request,a,b):
    c=int(a)+int(b)
    return HttpResponse("a+b=%s"%str(c))

def add2_new(request,a,b):
    return  HttpResponseRedirect (
    reverse('add2',args=(a,b))
    )

def default(request):
    return  render(request,"home.html")