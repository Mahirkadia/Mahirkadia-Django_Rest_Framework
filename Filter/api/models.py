from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=100)
    roll=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    passby=models.CharField(max_length=100)
