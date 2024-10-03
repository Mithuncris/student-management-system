from django.db import models
from users.models import CustomUser

class Class(models.Model):
    name = models.CharField(max_length=100)  
    subject = models.CharField(max_length=100)  
    teacher = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  

    def __str__(self):
        return self.name

class StudentClassEnrollment(models.Model):
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  
    class_enrolled = models.ForeignKey(Class, on_delete=models.CASCADE)  

    def __str__(self):
        return f"{self.student.username} enrolled in {self.class_enrolled.name}"
