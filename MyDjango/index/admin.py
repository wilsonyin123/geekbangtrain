from django.contrib import admin

# Register your models here.

from .models import Type, Name

admin.site.register(Type)
admin.site.register(Name)