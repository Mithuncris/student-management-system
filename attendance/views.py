from django.shortcuts import render
from .models import Attendance

def student_attendance_view(request, student_id):
    attendance_records = Attendance.objects.filter(student_id=student_id).order_by('date', 'period')
    context = {
        'attendance_records': attendance_records,
    }
    return render(request, 'attendance/student_attendance.html', context)
