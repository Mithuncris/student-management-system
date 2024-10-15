from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)  # Course code like 'CS101'
    description = models.TextField()
    credits = models.IntegerField()  # Number of credits for the course
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.code} - {self.name}"

class Instructor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='instructors')

    def __str__(self):
        return self.name

class Enrollment(models.Model):
    student = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments')
    enrollment_date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        unique_together = ('student', 'course')

    def __str__(self):
        return f"{self.student.username} enrolled in {self.course.code}"
