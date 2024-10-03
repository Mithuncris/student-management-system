from django.db import models
from users.models import CustomUser  
from classes.models import Class       

class InternalMarks(models.Model): 
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="internal_marks")
    exam_name = models.CharField(max_length=50)
    marks = models.IntegerField()
    staff = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="marks_recorded")
    class_enrolled = models.ForeignKey(Class, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.student} - {self.exam_name} - {self.marks}"
