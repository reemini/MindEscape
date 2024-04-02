from django.shortcuts import render, redirect, get_object_or_404
from courses.models import Course

def home(request):
    return render(request, 'home.html')

def signup(request):
    return render(request,'signup.html')

def login(request):
    return render(request, 'login.html')

def header(request):
    return render(request,'header.html')

def forgetpass(request):
    return render(request, 'forgetpass.html')

def confirmpass(request):
    return render(request, 'confirmpass.html')

def student(request):
    return render(request, 'student.html')

def teacher(request):
    return render(request, 'teacher.html')

def EditStudentProfile(request):
    return render(request, 'EditStudentProfile.html')

def EditTeacherProfile(request):
    return render(request, 'EditTeacherProfile.html')

def AdminPanel(request):
    return render(request,'AdminPanel.html')

def AIrequest(request):
    return render(request,'AI-Request.html')

def EduRequest(request):
    return render(request,'Edu-Request.html')

def userMang(request):
    return render(request,'userMang.html')