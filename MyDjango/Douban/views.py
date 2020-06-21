from django.shortcuts import render

# Create your views here.
from .models import T1

def books_short(request):
    ###  从models取数据传给template  ###
    shorts = T1.objects.all()
    return render(request, 'douban.html', locals())