from django.db import models

# Create your models here.
class Student(models.Model):
    empID=models.IntegerField()
    name=models.CharField(max_length=40)
    email=models.EmailField(max_length=55)

    def __str__ (self):
        return str(self.empID)

    
