from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm  # Ensure this form is correctly defined in forms.py

# Registration view

def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after successful registration
            messages.success(request, "Registration successful. You are now logged in.")
            return redirect('home')  # Redirect to the home view
        else:
            messages.error(request, "Registration failed. Please correct the errors.")
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/register.html', {'form': form})

# Login view
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)  # Authenticate the user
            if user is not None:
                login(request, user)  # Log the user in
                messages.success(request, f"Welcome {user.username}!")
                return redirect('home')  # Redirect to the home page
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid form input.")
    else:
        form = AuthenticationForm()

    return render(request, 'registration/login.html', {'form': form})

# Logout view
@login_required
def logout_view(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('users:login')  # Redirect to login page after logout

# Login or Register view
def login_or_register(request):
    if request.user.is_authenticated:  # Check if the user is logged in
        return redirect('home')  # Redirect to home if logged in
    else:
        return render(request, 'registration/login_or_register.html')  # Render the login/register page

# Home view
@login_required  # Ensure that only authenticated users can access the home page
def home_view(request):
    return render(request, 'home.html')  # Ensure you have a home.html template
