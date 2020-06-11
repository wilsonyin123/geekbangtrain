from django.urls import path, re_path, register_converter
from . import views, converters

register_converter(converters.IntConverter,'myint')
register_converter(converters.FourDigitYearConverter, 'yyyy')

urlpatterns = [
    path('', views.index),
    re_path('(?P<year>[0-9]{4}).html', views.myyear, name='urlyear'),
    ### 带变量的URL
    path('<int:year>', views.year),  # 只接收整数，其他类型返回404
    path('<int:year>/<str:name>', views.name),
    # path('<myint:year>', views.year), # 自定义过滤器
    path('books', views.books),

]
