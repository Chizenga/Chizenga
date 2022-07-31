from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    pass 

class program(models.Model):
    program_name=models.CharField(max_length=300)
    department=models.CharField(max_length=300)
    faculty=models.CharField(max_length=300)
    year_published=models.IntegerField(default=0)
    requirements=models.CharField(max_length=300)
    duration=models.IntegerField(default=0)
    fees_for_certificate_per_year=models.IntegerField(default=0)
    def __str__(self) -> str: 
        return self.program_name 
    

class Student(models.Model):
    student_name=models.CharField(max_length=300)
    surname=models.CharField(max_length=300)
    student_age=models.IntegerField(default=0)
    student_contact_address=models.CharField(max_length=200)
    program_of_study=models.CharField(max_length=300)
    Instirution=models.ForeignKey("Institution", on_delete=models.CASCADE)

    profile_picture=models.ImageField(blank=True , null=True)
    special_file=models.FileField(blank=True, null=True)
    def __str__(self) -> str:
        return self.student_name 

class Institution(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    Location=models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return f"{self.name}"
