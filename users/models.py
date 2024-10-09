from django.contrib.auth.models import AbstractUser
from django.db import models

class Year(models.Model):
    name = models.CharField(max_length=10, unique=True)
    
    def __str__(self):
        return self.name

class Section(models.Model):
    name = models.CharField(max_length=10)
    year = models.ForeignKey(Year, on_delete=models.CASCADE, related_name='sections')

    def __str__(self):
        return f"{self.name} ({self.year.name})"

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('staff', 'Staff'),
        ('hod', 'HOD'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    department = models.CharField(max_length=100, null=True, blank=True)
    year = models.ForeignKey(Year, null=True, blank=True, on_delete=models.SET_NULL)
    section = models.ForeignKey(Section, null=True, blank=True, on_delete=models.SET_NULL)

    roll_number = models.CharField(max_length=10, unique=True, null=True, blank=True)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


    def __str__(self):
        return self.username  
