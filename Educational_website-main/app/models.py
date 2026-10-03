
from django.db import models


class Parent(models.Model):
    name = models.CharField(max_length=255)
    phone = models.IntegerField()
    email = models.EmailField()
    stname = models.CharField(max_length=255)
    msg = models.TextField()

class Student(models.Model):
    name = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.EmailField()
    msg = models.TextField()
    

    def __str__(self):
        return self.name