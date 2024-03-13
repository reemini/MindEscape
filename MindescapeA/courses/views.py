from django.shortcuts import render, redirect, get_object_or_404
from .models import Course
from django.http import JsonResponse

def educator_courses(request):
    return render(request, 'educator_courses.html')

def course_detail(request):
    return render(request, 'course_detail.html')

def generated_course(request):
    return render(request, 'generated_course.html')

def courseinfo(request):
    return render(request,'courseinfo.html')

def courses(request):
    return render(request,'courses.html')
