from django import forms
from .models import Course, Instructor, Enrollment

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'code', 'description', 'credits', 'start_date', 'end_date']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'name': 'Course Name',
            'code': 'Course Code',
            'description': 'handling staff',
            'credits': 'Credits',
            'start_date': 'Start Date',
            'end_date': 'End Date',
        }

class InstructorForm(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = ['name', 'email', 'phone_number', 'course']
        labels = {
            'name': 'Instructor Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'course': 'Course Assigned',
        }

class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['student', 'course']
        labels = {
            'student': 'Student',
            'course': 'Course',
        }
