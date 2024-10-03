from django.shortcuts import render, get_object_or_404, redirect
from .models import Class
from .forms import ClassForm

# View for listing all classes
def class_list_view(request):
    classes = Class.objects.all()  # Get all classes
    context = {'classes': classes}
    return render(request, 'classes/class_list.html', context)

# View for adding a new class
def class_create_view(request):
    if request.method == 'POST':
        form = ClassForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('class_list')  # Redirect to the class list after saving
    else:
        form = ClassForm()
    
    return render(request, 'classes/class_form.html', {'form': form})

# View for updating an existing class
def class_update_view(request, class_id):
    class_instance = get_object_or_404(Class, id=class_id)
    
    if request.method == 'POST':
        form = ClassForm(request.POST, instance=class_instance)
        if form.is_valid():
            form.save()
            return redirect('class_list')
    else:
        form = ClassForm(instance=class_instance)

    return render(request, 'classes/class_form.html', {'form': form})

# View for deleting a class (optional)
def class_delete_view(request, class_id):
    class_instance = get_object_or_404(Class, id=class_id)
    if request.method == 'POST':
        class_instance.delete()
        return redirect('class_list')
    
    return render(request, 'classes/class_confirm_delete.html', {'class': class_instance})
