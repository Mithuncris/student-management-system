from django.db import models
from django.conf import settings  # Import settings to use AUTH_USER_MODEL

class Course(models.Model):
    name = models.CharField(max_length=100)
    staff = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='courses')  # Update this line

    def __str__(self):
        return self.name

class Attendance(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='attendance_records')  # Update this line
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='attendance_records')
    date = models.DateField()
    period = models.CharField(max_length=10)  # To indicate the period (e.g., "1st", "2nd")
    present = models.BooleanField(default=False)  # Indicates if the student was present

    class Meta:
        unique_together = ('student', 'course', 'date', 'period')  # Prevents duplicate entries

    def __str__(self):
        return f"{self.student.username} - {self.course.name} - {self.date} - {self.period}"

    def get_attendance_percentage(student):
        total_classes = Attendance.objects.filter(student=student).count()
        present_classes = Attendance.objects.filter(student=student, present=True).count()
        return (present_classes / total_classes * 100) if total_classes > 0 else 0
