from django.contrib.auth.models import Permission

def create_permissions():
    Permission.objects.get_or_create(codename='can_view_students', name='Can View Students')
    Permission.objects.get_or_create(codename='can_manage_staff', name='Can Manage Staff')
    Permission.objects.get_or_create(codename='can_view_hod', name='Can View HOD')
