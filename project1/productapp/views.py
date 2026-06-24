from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def add(request):
    return HttpResponse("<h1> hii django <h1>")