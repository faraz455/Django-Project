from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from .forms import UserForms
from service.models import Service
from news.models import News
from rest_framework.views import APIView
from rest_framework import generics, viewsets
from django.forms.models import model_to_dict
from .serializers import NewsSerializer

class Simple(APIView):

    # CREATE
    def post(self, request):
        news = News.objects.create(
            news_title = request.data['news_title'],
            news_des = request.data['news_des']
        )
        return JsonResponse({'data': model_to_dict(news)})
    
    # READ
    def get(self,request):
        newsData = News.objects.all().values()
        return JsonResponse({'data': list(newsData)})

class NewsClass(APIView):
    # CREATE
    def post(self, request):
        serializer = NewsSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return JsonResponse({'data': serializer.data})
    
    # READ
    def get(self,request):
        newsData = News.objects.all().values()
        # print(NewsSerializer(newsData, many = True).data)
        return JsonResponse({'data': NewsSerializer(newsData, many = True).data})

    # UPDATE
    def put(self,request, *args, **kwargs):
        model_id = kwargs.get('id', None)
        if not model_id:
            return JsonResponse({"error": "method /PUT/ not allowed" })
        try:
            instance = News.objects.get(id = model_id)
        except:
            return JsonResponse({"error": "object does not exist", "model id": model_id})

        serializer = NewsSerializer(data = request.data, instance = instance)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return JsonResponse({"data": serializer.data})

class NewsGenerics(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

class NewsGenericsUpdate(generics.UpdateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    lookup_field = "id"

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

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

def detailPage(request, newsid):
    newsdetails = News.objects.get(id = newsid)
    data = {
        'newsdetail': newsdetails
    }
    return render(request, 'newsdetail.html', data)

def course(request):
    return HttpResponse("Welcome to course page")

def courseDetail(request, courseid):
    return HttpResponse(courseid)

def userform(request):
    fn = UserForms()
    result = 0
    data = {'form':fn}
    try:
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

def aboutus(request):
    return render(request, 'aboutus.html')
