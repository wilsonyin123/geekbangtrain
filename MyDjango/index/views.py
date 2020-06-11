from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello Django!")

def myyear(request, year):
    return render(request, 'yearview.html')

def year(request, year):
    return HttpResponse(year)
    # return redirect('/2020.html')

def name(request, **kwargs):
    return HttpResponse(kwargs['name'])