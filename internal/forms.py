from django import forms
from .models import InternalMarks

class InternalMarksForm(forms.ModelForm):
    class Meta:
        model = InternalMarks
        fields = ['student', 'exam_name', 'marks', 'staff', 'class_enrolled']
