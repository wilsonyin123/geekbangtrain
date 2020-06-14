from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello Django!")

# path('<int:year>', views.year), 
def year(request, year):
    # return HttpResponse(year)
    return redirect('/2020.html')

# path('<int:year>/<str:name>', views.name),
def name(request, **kwargs):
    return HttpResponse(kwargs['name'])

# path('<myint:year>', views.year), 
# re_path('(?P<year>[0-9]{4}).html', views.myyear, name='urlyear'),
def myyear(request, year):
    return render(request, 'yearview.html')
