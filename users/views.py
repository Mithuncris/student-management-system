from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from .forms import CustomUserCreationForm
from django.contrib.auth.models import Permission
from django.core.exceptions import ValidationError
from .models import CustomUser, Year, Section
from django.http import Http404


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

@login_required
@user_passes_test(is_staff)
def register_student_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.role = 'student'  # Set role to student
            student.save()
            messages.success(request, f"Student {student.username} registered successfully!")
            return redirect('users:staff_dashboard')
        else:
            messages.error(request, "Registration failed. Please correct the errors.")
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/register_student.html', {'form': form})

@login_required
@user_passes_test(is_hod)
def register_staff_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            staff = form.save(commit=False)
            staff.role = 'staff'  # Set role to staff
            staff.save()
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
    staffs = CustomUser.objects.filter(role='staff')
    return render(request, 'manage_staff.html', {'staffs': staffs})

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

@login_required
@user_passes_test(is_hod)
def yearwise_sections_view(request):
    years = Year.objects.all()  # Get all Year objects
    return render(request, 'yearwise_sections.html', {'years': years})

# View to display sections for a specific year
@login_required
@user_passes_test(is_hod)
def sections_by_year_view(request, year_id):
    year = get_object_or_404(Year, id=year_id)
    sections = year.sections.all()  # Access the related sections using the related_name

    return render(request, 'sections_by_year.html', {'year': year, 'sections': sections})

# View to display students in a specific section
@login_required
@user_passes_test(is_hod)
def students_in_section_view(request, section_id):
    section = get_object_or_404(Section, id=section_id)
    # Assuming the relationship between CustomUser and Section is defined correctly
    students = CustomUser.objects.filter(section=section)  # Adjust if needed

    return render(request, 'students_in_section.html', {'section': section, 'students': students})

# View to edit a student
@login_required
@user_passes_test(lambda u: u.role == 'hod')
def edit_student_view(request, student_id):
    student = get_object_or_404(CustomUser, id=student_id, role='student')
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('users:sections_by_year_view', student.year.id)
    else:
        form = CustomUserCreationForm(instance=student)
    
    return render(request, 'edit_student.html', {'form': form, 'student': student})

# HOD can delete a student
@login_required
@user_passes_test(lambda u: u.role == 'hod')
def delete_student_view(request, student_id):
    try:
        student = CustomUser.objects.get(id=student_id, role='student')
    except CustomUser.DoesNotExist:
        raise Http404("Student not found")
    
    if request.method == 'POST':
        student.delete()
        return redirect('users:sections_by_year_view', student.year.id)

    return render(request, 'delete_student.html', {'student': student})

@login_required
@user_passes_test(lambda u: u.role == 'hod')
def add_student_view(request, section_id):

    section = get_object_or_404(Section, id=section_id)
    year = section.year 

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = 'student' 
            user.year = year        
            user.section = section  
            user.save()
            return redirect('users:sections_by_year_view', year.id)
    else:
        form = CustomUserCreationForm()

    return render(request, 'add_student.html', {'form': form, 'section': section, 'year': year})

@login_required
@user_passes_test(lambda u: u.role == 'hod')
def user_detail_view(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    return render(request, 'user_detail.html', {'user': user})