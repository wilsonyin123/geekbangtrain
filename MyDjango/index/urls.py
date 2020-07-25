from django.urls import path, re_path, register_converter
from . import views, converters

urlpatterns = [
    path('', views.index),
    path('test1', views.test1),
    path('test2', views.test2),
    path('login2', views.login2)
]
