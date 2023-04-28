from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=20)
    f_name=models.CharField(max_length=45)
    email=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    