"""MindescapeA URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('educator_courses/', views.educator_courses, name='educator_courses'),
    path('courses/<int:course_id>/', views.course_detail, name='course_detail'),
    path('generated_course/', views.generated_course, name='generated_course'),
    path('courseinfo',views.courseinfo, name = 'courseinfo'),
    path('courses',views.courses, name = 'courses'),
    path('firstPageOfCreateCourse',views.firstPageOfCreateCourse, name = 'firstPageOfCreateCourse'),
    path('CourseInner',views.CourseInner, name = 'CourseInner'),
    path('myCourses',views.myCourses, name = 'myCourses'),

]

