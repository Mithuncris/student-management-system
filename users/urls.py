from django.urls import path 
from . import views

app_name = 'users'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('update/<int:user_id>/', views.update_user, name='update_user'),
]
