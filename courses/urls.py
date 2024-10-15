from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [
    path('list/', views.course_list_view, name='course_list'),
    path('add/', views.add_course_view, name='add_course'),
    path('edit/<int:course_id>/', views.edit_course_view, name='edit_course'),
    path('delete/<int:course_id>/', views.delete_course_view, name='delete_course'),
    path('teacher-courses/', views.teacher_courses_view, name='teacher_courses'),
    path('student-courses/', views.student_courses_view, name='student_courses'),
     path('view/<int:course_id>/', views.view_course_view, name='view_course'),

]
