from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'users'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/student/', views.register_student_view, name='register_student'),
    path('register/staff/', views.register_staff_view, name='register_staff'),
    path('register/hod/', views.register_hod_view, name='register_hod'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('home/',views.home_view,name="home"),
    path('student_dashboard/', views.student_view, name='student_dashboard'),
    path('staff_dashboard/', views.staff_view, name='staff_dashboard'),
    path('hod_dashboard/', views.hod_view, name='hod_dashboard'),
    path('manage_staff/', views.manage_staff_view, name='manage_staff'),
    path('hod_dashboard/staff/<int:staff_id>/edit/', views.edit_staff_view, name='edit_staff'),
    path('hod_dashboard/staff/<int:staff_id>/delete/', views.delete_staff_view, name='delete_staff'),
    path('hod_dashboard/yearwise/', views.yearwise_sections_view, name='yearwise_sections_view'),
    path('hod_dashboard/yearwise/<int:year_id>/sections/', views.sections_by_year_view, name='sections_by_year_view'),
    path('hod_dashboard/sections/<int:section_id>/students/', views.students_in_section_view, name='students_in_section_view'),
    path('hod_dashboard/sections/<int:section_id>/add_student/', views.add_student_view, name='add_student'),
    path('hod_dashboard/student/<int:student_id>/edit/', views.edit_student_view, name='edit_student'),
    path('hod_dashboard/student/<int:student_id>/delete/', views.delete_student_view, name='delete_student'),
    path('hod_dashboard/user/<int:user_id>/', views.user_detail_view, name='user_detail'),
]
