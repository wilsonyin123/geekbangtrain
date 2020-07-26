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

def login(request):
    return render(request, 'form1.html', locals())


from .form import LoginForm
from django.contrib.auth import authenticate, login
def login2(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            # 读取表单的返回值
            cd = login_form.cleaned_data 
            user = authenticate(username=cd['username'], password=cd['password'])
            if user:
                # 登陆用户
                login(request, user)  
                return HttpResponse('登录成功')
            else:
                return HttpResponse('登录失败')
    # GET
    if request.method == "GET":
        login_form = LoginForm()
        return render(request, 'form2.html', {'form': login_form})

from django.views.decorators.csrf import csrf_exempt, csrf_protect
@csrf_exempt
def result(request):
    return render(request, 'result.html')

# receiver
def my_callback1(sender, **kwargs):
    print("Request started!")
  
# connect
from django.core.signals import request_started
request_started.connect(my_callback1)

from django.core.signals import request_finished
from django.dispatch import receiver

@receiver(request_finished)
def my_callback2(sender, **kwargs):
    print("Request finished!")