from django.shortcuts import render
from .models import Student
# Create your views here.
def details(request):
    st=Student.objects.all()
    return render(request,'enroll/student.html',{'form':st})