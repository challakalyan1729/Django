from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def fun(resquest):
    return HttpResponse("home page")
def fun2(resquest):
    return HttpResponse("page1")
def fun3(resquest):
    return HttpResponse("page2")