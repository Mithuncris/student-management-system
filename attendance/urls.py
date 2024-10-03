from django.urls import path
from . import views

app_name = 'attendance'

urlpatterns = [
    #this is for student's view
    path('student/', views.student_attendance_view, name='student_attendance'),

    #this is for staff
    path('staff/<int:class_id>/<int:period_id>/', views.staff_attendance_view, name='staff_attendance'),
    path('staff/mark/<int:class_id>/<int:period_id>/', views.mark_attendance_view, name='mark_attendance'),
    path('staff/analyse/', views.staff_analyze_class_attendance_view, name='analyse_class_attendance'),
    path('staff/analyse/student/<int:student_id>/', views.staff_analyze_student_attendance_view, name='analyse_student_attendance'),
]