from django.db import models

# Create your models here.

class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

class Student(models.Model):
    name = models.CharField(max_length= 200)
    grade = models.IntegerField()
    essay = models.FileField(upload_to = 'uploads/', blank = True)
