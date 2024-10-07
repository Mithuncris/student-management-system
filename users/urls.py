from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'users'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('student/', views.student_view, name='student_dashboard'),
    path('staff/', views.staff_view, name='staff_dashboard'),
    path('hod/', views.hod_view, name='hod_dashboard'),
    path('home/',views.home_view,name="home"),
    path('student_dashboard/', views.student_dashboard_view, name='student_dashboard'),
    path('staff_dashboard/', views.staff_dashboard_view, name='staff_dashboard'),
    path('hod_dashboard/', views.hod_dashboard_view, name='hod_dashboard'),
]
