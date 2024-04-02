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
from users import views
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path ('signup',views.signup, name = 'signup'),
    path ('login',views.login, name = 'login'),
    path ('header',views.header, name = 'header'),
    path ('forgetpass',views.forgetpass, name = 'forgetpass'),
    path ('confirmpass',views.confirmpass, name = 'confirmpass'),
    path ('teacher',views.teacher, name = 'teacher'),
    path ('student',views.student, name = 'student'),
    path ('EditStudentProfile',views.EditStudentProfile, name = 'EditStudentProfile'),
    path ('EditTeacherProfile',views.EditTeacherProfile, name = 'EditTeacherProfile'),
    path('AdminPanel',views.AdminPanel, name = 'AdminPanel'),
    path('AIrequest',views.AIrequest, name = 'AIrequest'),
    path('EduRequest',views.EduRequest, name = 'EduRequest'),
    path('userMang',views.userMang, name = 'userMang'),




]
