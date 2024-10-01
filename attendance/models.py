from django.db import models
from users.models import CustomUser
from classes.models import Class

# Create your models here.
class Period(models.Model):
    name = models.CharField(max_length=10)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.name}  ({self.start_time} - {self.end_time})"
    
class Attendance(models.Model):
    date = models.DateField()
    period = models.ForeignKey(Period, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices = [('Present', 'Present'), ('Absent', 'Absent'), ('On-Duty', 'On-Duty')])
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="attendances")
    class_enrolled = models.ForeignKey(Class, on_delete=models.CASCADE)
    staff = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='attendance_records')

    def __str__(self):
        return f"Attendance for {self.student.username} on {self.date} during {self.period.name}: {self.status}"
    