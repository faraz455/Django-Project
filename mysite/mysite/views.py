from unittest import result
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import UserForms
def homePage(request):
    output = 0
    if request.method == "GET":
        output = request.GET.get('output')

    data = {
        'title': "Home Page",
        'bdata': "This is home page",
        'clist' : ['php', 'Java', 'Django'],
        'output' :output

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