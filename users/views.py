from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from .forms import CustomUserCreationForm
from django.contrib.auth.models import Permission
from django.core.exceptions import ValidationError


# Check if user is a student
def is_student(user):
    return user.role == 'student'

# Check if user is a staff member
def is_staff(user):
    return user.role == 'staff'

# Check if user is HOD
def is_hod(user):
    return user.role == 'hod'


@login_required
@permission_required('users.can_view_students', raise_exception=True)
def student_view(request):
    return render(request, 'student_dashboard.html')

@login_required
@permission_required('users.can_manage_staff', raise_exception=True)
def staff_view(request):
    return render(request, 'staff_dashboard.html')

@login_required
@permission_required('users.can_view_hod', raise_exception=True)
def hod_view(request):
    return render(request, 'hod_dashboard.html')


# Registration view
def assign_role_permissions(user):
    """ Assign permissions to the user based on their role """
    if user.role == 'student':
        permission = Permission.objects.get(codename='can_view_students')
        user.user_permissions.add(permission)
    elif user.role == 'staff':
        permission = Permission.objects.get(codename='can_manage_staff')
        user.user_permissions.add(permission)
    elif user.role == 'hod':
        permission = Permission.objects.get(codename='can_view_hod')
        user.user_permissions.add(permission)

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)  # Log the user in
                messages.success(request, f"Welcome back, {user.username}!")

                # Redirect based on user role
                if user.role == 'student':
                    return redirect('users:student_dashboard')  # Redirect to student dashboard
                elif user.role == 'staff':
                    return redirect('users:staff_dashboard')  # Redirect to staff dashboard
                elif user.role == 'hod':
                    return redirect('users:hod_dashboard')  # Redirect to HOD dashboard
                else:
                    return redirect('users:home')  # Default redirect if no role matches
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Please correct the form input.")
    else:
        form = AuthenticationForm()

    return render(request, 'registration/login.html', {'form': form})


# Logout view
@login_required
def logout_view(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('users:login')

# Home view (login required)
@login_required
def home_view(request):
    return render(request, 'home.html')

# For student registration:
@login_required
@user_passes_test(is_staff)
def register_student_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.role = 'student'  
            student.save()
            assign_role_permissions(student)  
            messages.success(request, f"Student {student.username} registered successfully!")
            return redirect('users:staff_dashboard')  
        else:
            messages.error(request, "Registration failed. Please correct the errors.")
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/register_student.html', {'form': form})

# For staff registration:
@login_required
@user_passes_test(is_hod)
def register_staff_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            staff = form.save(commit=False)
            staff.role = 'staff'  
            staff.save()
            assign_role_permissions(staff)  
            messages.success(request, f"Staff {staff.username} registered successfully!")
            return redirect('users:hod_dashboard')  
        else:
            messages.error(request, "Registration failed. Please correct the errors.")
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/register_staff.html', {'form': form})

# For HOD registration:
@login_required
def register_hod_view(request):
    if not request.user.is_superuser:  
        return redirect('users:home')

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            hod = form.save(commit=False)
            hod.role = 'hod' 
            hod.save()
            assign_role_permissions(hod)  
            messages.success(request, f"HOD {hod.username} registered successfully!")
            return redirect('users:home')
        else:
            messages.error(request, "Registration failed. Please correct the errors.")
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/register_hod.html', {'form': form})

@login_required
@user_passes_test(is_hod)  
def manage_staff_view(request):
    User = get_user_model()  
    staff_members = User.objects.filter(role='staff')  

    context = {
        'staff_members': staff_members
    }

    return render(request, 'manage_staff.html', context)

@login_required
@user_passes_test(is_hod)
def edit_staff_view(request, staff_id):
    staff_member = get_object_or_404(get_user_model(), id=staff_id, role='staff')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, instance=staff_member)
        if form.is_valid():
            try:
                form.save()  # This will now not raise an error for existing username
                messages.success(request, 'Staff member updated successfully.')
                return redirect('users:manage_staff')
            except ValidationError as e:
                form.add_error(None, e)  # Add error to the form if validation fails
    else:
        form = CustomUserCreationForm(instance=staff_member)

    return render(request, 'edit_staff.html', {'form': form})

@login_required
@user_passes_test(is_hod)
def delete_staff_view(request, staff_id):
    staff_member = get_object_or_404(get_user_model(), id=staff_id, role='staff')

    if request.method == 'POST':
        staff_member.delete()
        messages.success(request, 'Staff member deleted successfully.')
        return redirect('users:manage_staff')

    return render(request, 'delete_staff.html', {'staff_member': staff_member})