from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import CustomUserCreationForm

# Check if user is a student
def is_student(user):
    return user.role == 'student'

# Check if user is a staff member
def is_staff(user):
    return user.role == 'staff'

# Check if user is HOD
def is_hod(user):
    return user.role == 'hod'

# Registration view
def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"Welcome {user.username}, your registration was successful!")
            return redirect('home')
        else:
            messages.error(request, "Registration failed. Please correct the errors.")
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


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
                elif user.role == 'HOD':
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
    return redirect('login')

# Home view (login required)
@login_required
def home_view(request):
    return render(request, 'home.html')

# Example view for students
@login_required
@user_passes_test(is_student)
def student_view(request):
    return render(request, 'student_dashboard.html')  # Create this template

# Example view for staff
@login_required
@user_passes_test(is_staff)
def staff_view(request):
    return render(request, 'staff_dashboard.html')  # Create this template

# Example view for HOD
@login_required
@user_passes_test(is_hod)
def hod_view(request):
    return render(request, 'hod_dashboard.html')  # Create this template

def login_or_register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        return render(request, 'registration/login_or_register.html')
