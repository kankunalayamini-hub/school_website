from django import forms
from app.models import *

class Parent_regForm(forms.ModelForm):
    class Meta:
        model = Parent
        fields = "__all__"
        

class Student_regForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"