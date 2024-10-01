from django.db import models
#from users.models import CustomerUser   

class Class(models.Model): 
    students = models.ManyToManyField(CustomerUser, related_name='enrolled_classes', limit_choices_to={'role': 'student'})
    staff = models.ForeignKey(CustomerUser, on_delete=models.CASCADE, related_name="marks_recorded")
    class_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.student} - {self.staff} - {self.class_name}"
