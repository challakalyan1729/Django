from django.shortcuts import render
def fun1(request):
    name = request.GET.get('name','')
    return render(request,'firstpage.html')
def fun2(request):
    name = request.GET.get('name','')
    return render(request,'hello.html',context={'name':name})