from django.contrib import admin
from .models import Course, Section, Lesson, Content, Enrollment, Rate

admin.site.register(Course)
admin.site.register(Section)
admin.site.register(Lesson)
admin.site.register(Content)
admin.site.register(Rate)
admin.site.register(Enrollment)
