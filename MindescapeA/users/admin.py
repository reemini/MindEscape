from django.contrib import admin
from .models import User, Educator, Admin, Student

admin.site.register(User)
admin.site.register(Educator)
admin.site.register(Admin)
admin.site.register(Student)
