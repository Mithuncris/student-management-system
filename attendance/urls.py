from django.urls import path
from .views import hod_attendance_view, staff_attendance_view, student_attendance_view

urlpatterns = [
    path('hod/', hod_attendance_view, name='hod_attendance'),
    path('staff/', staff_attendance_view, name='staff_attendance'),
    path('student/', student_attendance_view, name='student_attendance'),
]
