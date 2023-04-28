from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=29)
    email=models.EmailField(max_length=55)
    f_name=models.CharField(max_length=100)

    def __str__(self):
        return self.name
