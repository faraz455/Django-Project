from unittest import result
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import UserForms
from service.models import Service
from news.models import News

def homePage(request):
    newsData = News.objects.all()
    serviceData = Service.objects.all()
    # you can order it by .order_by(column name) 
    # if - before column name then order desending else assending

    # To limit data you can use slicing technique [:index till you want] (no negative index)

    data = {
        'title': "HOME PAGE",
        'bdata': "HOME PAGE",
        'serviceData': serviceData,
        'newsData': newsData
    }
    return render(request, "index.html", data)

def course(request):
    return HttpResponse("Welcome to course page")

def courseDetail(request, courseid):
    return HttpResponse(courseid)

def userform(request):
    fn = UserForms()
    result = 0
    data = {'form':fn}
    try:
        print(request.method)
        if request.method == "POST":
            n1 = int(request.POST.get('num1'))
            n2 = int(request.POST.get('num2'))
            result = n1+n2
            data = {
                'form':fn,
                'n1':n1,
                'n2':n2,
                'result': result}
            # url = '/submitform/'
            # return HttpResponseRedirect(url)
    except:
        pass
    return render(request, "userform.html", data)

def submitform(request):
    
    if request.method == "POST":
        num1 = int(request.POST.get("num1"))
        num2 = int(request.POST.get("num2"))
        sum = num1+num2
        data = {
            "num1": num1,
            "num2": num2,
            "result": sum
        }
    return render (request, 'submitform.html', data)

def calculator(request):
    result = 0
    data = {}
    try:
        if request.method == "POST":
            
            n1 = eval(request.POST.get("num1"))
            n2 = eval(request.POST.get("num2"))
            op = request.POST.get("op")
            if op == "+":
                result = n1+n2
            elif op == "-":
                result = n1-n2
            elif op == "*":
                result = n1*n2
            elif op == "/":
                result = n1/n2
            data = {
                "n1": n1,
                "n2":n2,
                "op":op,
                "result":result
            }
    except:
        pass

    return render (request,'calculator.html',data)



