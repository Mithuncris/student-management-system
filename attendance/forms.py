from django import forms
from .models import Attendance, Period

class AttendanceForm(forms.ModelForm):
    period = forms.ModelChoiceField(queryset=Period.objects.all(), label="Select Period")
    
    class Meta:
        model = Attendance
        fields = ['date', 'period', 'status', 'student', 'class_enrolled']
