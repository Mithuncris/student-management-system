from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType
from users.models import CustomUser  

def create_permissions():
    # Get the ContentType for the User model
    user_content_type = ContentType.objects.get_for_model(CustomUser)

    # Create the permissions
    can_view_students, _ = Permission.objects.get_or_create(
        codename='can_view_students',
        name='Can View Students',
        content_type=user_content_type,
    )

    can_manage_staff, _ = Permission.objects.get_or_create(
        codename='can_manage_staff',
        name='Can Manage Staff',
        content_type=user_content_type,
    )

    can_view_hod, _ = Permission.objects.get_or_create(
        codename='can_view_hod',
        name='Can View HOD',
        content_type=user_content_type,
    )

    # Get or create the HOD and Staff groups
    hod_group, _ = Group.objects.get_or_create(name='HOD')
    staff_group, _ = Group.objects.get_or_create(name='Staff')

    # Assign permissions to HOD group
    hod_group.permissions.add(can_manage_staff, can_view_students)

    # Assign permissions to Staff group
    staff_group.permissions.add(can_view_students)
