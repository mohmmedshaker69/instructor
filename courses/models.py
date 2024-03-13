from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class InstructorDepartment(models.Model):
    name=models.CharField(max_length=255)

    class Meta:
        ordering=('name',)
        

    def __str__(self):
        return self.name


class Instructor(models.Model):

    NUM_OF_COURSES_TECH_BEFORE = (
        (0,'0 courses'),
        (1, '1 course'),
        (2, '2 courses'),
        (3, '3 courses'),
        (4, '4 courses'),
        (5, '5 or more than 5 courses'),
    )
    category=models.ForeignKey(InstructorDepartment, related_name='instructors',on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    phone_number = models.CharField(max_length=14)
    email = models.CharField(max_length=150, default='test')  # Provide a default value here
    courses_teched_before = models.IntegerField(choices=NUM_OF_COURSES_TECH_BEFORE, default=0)
    description=models.TextField()

    class Meta:
        ordering=('name',)
    
    def __str__(self):
        return self.name

    


class CourseCategory(models.Model):
    name=models.CharField(max_length=255)

    class Meta:
        ordering=('name',)
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Course(models.Model):

    RATING_CHOICES = (
        (1, '1 star'),
        (2, '2 stars'),
        (3, '3 stars'),
        (4, '4 stars'),
        (5, '5 stars'),
    )

    taked_by=models.ManyToManyField(User, related_name='course')
    teached_by=models.ForeignKey(Instructor, related_name='course', on_delete=models.CASCADE)
    category=models.ForeignKey(CourseCategory, related_name='course',on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    description=models.TextField()
    rating = models.IntegerField(choices=RATING_CHOICES, null=True, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    

    class Meta:
        ordering=('updated_at',)
    def __str__(self):
        return self.name


class Chapter(models.Model):
    course=models.ForeignKey(Course, related_name='chapters', on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering=('id',)
    def __str__(self):
        return self.name
    
class Lesson(models.Model):
    chapter = models.ForeignKey(Chapter, related_name = 'lessons', on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    video = models.FileField(upload_to='videos/', null=True, blank=True)
    pdf = models.FileField(upload_to='pdfs/', null=True, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    class Meta:
        ordering=('id',)
    def __str__(self):
        return self.name
