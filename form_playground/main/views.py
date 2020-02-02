from django.shortcuts import render
from main import forms
from main import models
# Create your views here.

def index(request):
    context={
        "form": forms.FormName
    }
    return render(request,'index.html',context)

    
def students(request):
    students=models.Student.objects.all()

    context={
        "students":students
    }

    return render(request , "students.html",context)

def addstudent(request):
    studentform = forms.StudentForm()
    context={
        'studentform':studentform
    }

    return render(request,'addstudent.html',context)