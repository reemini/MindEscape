from django.db import models

class User(models.Model):
    userEmail = models.EmailField(primary_key=True)
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    password = models.CharField(max_length=100)
    birthday = models.DateField()
    role = models.CharField(max_length=20)  # No default value defined here
    full_name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.userEmail
    
    def save(self, *args, **kwargs):
        # Set default value for role based on the type of user
        if self.__class__ == Student:
            self.role = 'student'
        elif self.__class__ == Educator:
            self.role = 'educator'
        elif self.__class__ == Admin:
            self.role = 'admin'
        
        super().save(*args, **kwargs)

class Educator(User):
    educatorID = models.AutoField(primary_key=True)
    company = models.CharField(max_length=100)
    professional_title = models.CharField(max_length=100)
    linkedIn_account = models.URLField(max_length=200)
    isOfficialReviewer = models.BooleanField(default=False)
    areas_of_specialization = models.TextField()
    
class Admin(User):
    adminID = models.AutoField(primary_key=True)
    
class Student(User):
    stdID = models.AutoField(primary_key=True)
    areas_of_interest = models.TextField()
