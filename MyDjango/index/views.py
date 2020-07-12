from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.
from django.http import HttpResponse

###  从models取数据传给template  ###
from .models import Name

def index(request):
    return HttpResponse("Hello Django!")

def myyear(request, year):
    return render(request, 'yearview.html')

def year(request, year):
    return HttpResponse(year)
    # return redirect('/2020.html')

def name(request, **kwargs):
    return HttpResponse(kwargs['name'])

def books(request):
    ###  从models取数据传给template  ###
    n = Name.objects.all()
    return render(request, 'bookslist.html', locals())

def test1(request):
    # 已经引入了HttpResponse
    # from django.http import HttpResponse
    response1 = HttpResponse()
    response2 = HttpResponse("Text only, please.", content_type="text/plain")

    return response1

def test2(request):
    # 使用HttpResponse的子类
    from django.http import JsonResponse
    response3 = JsonResponse({'foo': 'bar'})  # response.content
    response3['Age'] = 120

    from django.http import HttpResponseNotFound
    response4 = HttpResponseNotFound('<h1>Page not found</h1>')
    return response4