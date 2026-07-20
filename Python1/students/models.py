from django.db import models
from django.conf import settings


class Department(models.Model):
    name = models.CharField(max_length=100)
    building = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    credits = models.IntegerField()

    def __str__(self):
        return self.name


class Student(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)
    dob = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    cgpa = models.DecimalField(max_digits=4, decimal_places=2)
    photo = models.ImageField(upload_to='student/', blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='students')
    courses = models.ManyToManyField(course, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"