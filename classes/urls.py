from django.urls import path
from . import views

app_name = 'classes' 
urlpatterns = [
    path('', views.class_list_view, name='class_list'),
    path('create/', views.class_create_view, name='class_create'),
    path('update/<int:class_id>/', views.class_update_view, name='class_update'),
    path('delete/<int:class_id>/', views.class_delete_view, name='class_delete'),
]
