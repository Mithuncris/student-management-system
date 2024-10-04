from django.contrib import admin
from django.urls import path, include
from users import views as users_views  # Import views from the users app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', users_views.login_or_register, name='login_or_register'),  # Main entry point
    path('attendance/', include('attendance.urls')),
    path('classes/', include('classes.urls')),
    path('internal/', include('internal.urls')),
    path('users/', include('users.urls')),  # Correctly includes users app urls
    path('home/', users_views.home_view, name='home'),  # Ensure home view exists
]
