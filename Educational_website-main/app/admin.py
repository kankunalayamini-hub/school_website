from django.contrib import admin
from .models import *

@admin.register(Parent)
class Parent_regAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'stname', 'msg')
    search_fields = ('name', 'email', 'stname')

@admin.register(Student)
class Student_regAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'msg')
    search_fields = ('name', 'email')