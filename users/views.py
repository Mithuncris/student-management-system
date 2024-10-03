from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth import login, authenticate
from .models import CustomUser
from django.http import HttpResponse

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Set the password correctly
            user.save()
            login(request, user)  # Log the user in after registration
            return HttpResponse("")  # Redirect to a success page
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})

def update_user(request, user_id):
    user = CustomUser.objects.get(pk=user_id)
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('some-view-name')  # Redirect to a success page
    else:
        form = CustomUserChangeForm(instance=user)
    return render(request, 'users/update_user.html', {'form': form})
