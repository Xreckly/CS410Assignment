from django.db import models
from django.contrib.auth.models import User

# Create your models here.

teach_subject = (
    ("MATH", "Math"),
    ("ENGLISH", "English"),
    ("SCIENCE", "Science"),
    ("HISTORY", "History"),
    )

class_subject = (
    ("MATH", "Math"),
    ("ENGLISH", "English"),
    ("SCIENCE", "Science"),
    ("HISTORY", "History"),
    )

class member(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    title = models.CharField(max_length=15, default="student")

class teach(member):
    Subject = teach_subject

class student(member):
    Class = class_subject

    
