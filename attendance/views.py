from django.shortcuts import render, get_object_or_404, redirect
from .models import Attendance, Period
from classes.models import Class
from users.models import CustomUser
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Avg

# 1. Student attendance view (for students to view their own attendance)
@login_required
def student_attendance_view(request):
    student = request.user  # Assuming the logged-in user is a student
    attendance_records = Attendance.objects.filter(student=student).order_by('date', 'period')
    context = {
        'attendance_records': attendance_records,
    }
    return render(request, 'attendance/student_attendance.html', context)

# 2. Staff attendance view (for staff to view attendance for a class and period)
@login_required
def staff_attendance_view(request, class_id, period_id):
    class_enrolled = get_object_or_404(Class, id=class_id)
    period = get_object_or_404(Period, id=period_id)
    students = CustomUser.objects.filter(role='student', classes=class_enrolled)
    attendance_records = Attendance.objects.filter(class_enrolled=class_enrolled, period=period).order_by('date')

    context = {
        'students': students,
        'attendance_records': attendance_records,
        'class_enrolled': class_enrolled,
        'period': period,
    }
    return render(request, 'attendance/staff_attendance.html', context)

# 3. Mark attendance view (for staff to mark attendance for a specific class and period)
@login_required
def mark_attendance_view(request, class_id, period_id):
    class_enrolled = get_object_or_404(Class, id=class_id)
    period = get_object_or_404(Period, id=period_id)
    students = CustomUser.objects.filter(role='student', classes=class_enrolled)

    if request.method == 'POST':
        date = request.POST.get('date')  # Assuming a date is selected in the form

        for student in students:
            status = request.POST.get(f'status_{student.id}')  # e.g., 'Present', 'Absent', etc.
            Attendance.objects.update_or_create(
                student=student,
                class_enrolled=class_enrolled,
                period=period,
                date=date,
                defaults={'status': status, 'staff': request.user},
            )
        return redirect('attendance:staff_attendance', class_id=class_id, period_id=period_id)

    context = {
        'students': students,
        'class_enrolled': class_enrolled,
        'period': period,
    }
    return render(request, 'attendance/mark_attendance.html', context)

# 4. Analyze class attendance view (for staff to view attendance summary of all students in a class)
@login_required
def staff_analyze_class_attendance_view(request):
    class_attendance_summary = Attendance.objects.values('class_enrolled', 'student__username') \
        .annotate(total_classes=Count('period'), avg_attendance=Avg('status'))  # Custom logic for attendance average

    context = {
        'class_attendance_summary': class_attendance_summary,
    }
    return render(request, 'attendance/analyze_class_attendance.html', context)

# 5. Analyze individual student attendance view (for staff to analyze attendance of a specific student)
@login_required
def staff_analyze_student_attendance_view(request, student_id):
    student = get_object_or_404(CustomUser, id=student_id, role='student')
    attendance_records = Attendance.objects.filter(student=student).order_by('date', 'period')

    context = {
        'student': student,
        'attendance_records': attendance_records,
    }
    return render(request, 'attendance/analyze_student_attendance.html', context)
