from django.db import models
from users.models import Educator, Student  # Assuming your Educator model is in an app called educators
from django.core.validators import MinValueValidator, MaxValueValidator

class Course(models.Model):
    courseID = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    instructor = models.ForeignKey(Educator, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.DurationField()
    difficultyLevel = models.CharField(max_length=20)
    coursePic = models.ImageField(upload_to='course_pics/', blank=True, null=True)
    isPublished = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
class Section(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    sectionID = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title
    
class Lesson(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    lessonID = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Content(models.Model):
    LESSON_CONTENT_CHOICES = [
        ('text', 'Text'),
        ('video', 'Video'),
        ('audio', 'Audio'),
        ('picture', 'Picture'),
        # Add more choices as needed
    ]

    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    content_type = models.CharField(max_length=20, choices=LESSON_CONTENT_CHOICES)
    content = models.TextField()  # This field can store content of any type

    # should i add ID?

    def __str__(self):
        return f"{self.lesson.title} - {self.content_type}"
    

#
class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateField(auto_now_add=True)
    comletion_date = models.DateField()
    progressPercentage = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)]    
        )



    def __str__(self):
        return f"{self.student.full_name} - {self.course.title}"
    

class Rate(models.Model):
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    stars = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    def __str__(self):
        return f"{self.student.full_name} rates {self.enrollment.course.title} with {self.stars} stars"
