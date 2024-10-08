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
    path('edit_staff/<int:staff_id>/', views.edit_staff_view, name='edit_staff'),
    path('delete_staff/<int:staff_id>/', views.delete_staff_view, name='delete_staff'),
]
