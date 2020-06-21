from django.urls import path
from . import views


urlpatterns = [
    path('douban', views.books_short),

]
