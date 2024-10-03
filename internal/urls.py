from django.urls import path
from . import views

urlpatterns = [
     path('add/', views.add_internal_marks, name='add_internal_marks'),
    path('list/', views.list_internal_marks, name='marks_list'),
    path('update/<int:pk>/', views.update_internal_marks, name='update_internal_marks'),
]

