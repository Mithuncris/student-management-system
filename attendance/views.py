from django.shortcuts import render
from .models import Attendance, Course  # Import your models here
from django.contrib.auth.decorators import login_required
from django.db.models import Avg

@login_required
def hod_attendance_view(request):
    # Calculate attendance percentages
    attendance_by_department = (
        Attendance.objects
        .values('course__name')
        .annotate(percentage=Avg('present'))
    )
    
    attendance_by_year = (
        Attendance.objects
        .values('student__year')
        .annotate(percentage=Avg('present'))
    )
    
    attendance_by_section = (
        Attendance.objects
        .values('student__section')
        .annotate(percentage=Avg('present'))
    )
    
    attendance_by_student = (
        Attendance.objects
        .values('student__username')
        .annotate(percentage=Avg('present'))
    )
    
    context = {
        'attendance_by_department': attendance_by_department,
        'attendance_by_year': attendance_by_year,
        'attendance_by_section': attendance_by_section,
        'attendance_by_student': attendance_by_student,
    }
    
    return render(request, 'attendance/hod_attendance.html', context)

# Add similar views for staff and student as needed

# Staff Attendance Management View
def staff_attendance_view(request):
    if request.method == 'POST':
        # Logic for marking attendance period-wise for students
        course = Course.objects.get(id=request.POST['course_id'])
        students = request.POST.getlist('students')
        date = request.POST['date']
        period = request.POST['period']
        
        for student_id in students:
            present = student_id in request.POST.getlist('present_students')
            Attendance.objects.update_or_create(
                student_id=student_id,
                course=course,
                date=date,
                period=period,
                defaults={'present': present}
            )
    
    # Retrieve courses handled by the staff
    courses = Course.objects.filter(staff=request.user)
    context = {
        'courses': courses,
    }
    return render(request, 'attendance/staff_attendance.html', context)

# Student Attendance View
def student_attendance_view(request):
    attendance = Attendance.objects.filter(student=request.user)
    total_days = attendance.count()
    present_days = attendance.filter(present=True).count()
    attendance_percentage = (present_days / total_days * 100) if total_days > 0 else 0

    context = {
        'attendance': attendance,
        'attendance_percentage': attendance_percentage,
    }
    return render(request, 'attendance/student_attendance.html', context)
