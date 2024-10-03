from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import InternalMarks
from .forms import InternalMarksForm

@login_required
def add_internal_marks(request):
    if request.method == "POST":
        form = InternalMarksForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('marks_list')
    else:
        form = InternalMarksForm()
    return render(request, 'internal/add_internal_marks.html', {'form': form})

@login_required        
def list_internal_marks(request):
    marks = InternalMarks.objects.all()  # Fixed the typo here
    return render(request, 'internal/list_internal_marks.html', {'marks': marks})

@login_required
def update_internal_marks(request, pk):  # Added 'pk' parameter
    mark = get_object_or_404(InternalMarks, pk=pk)
    
    if request.method == 'POST':
        form = InternalMarksForm(request.POST, instance=mark)  # Corrected form name
        if form.is_valid():
            form.save()
            return redirect('marks_list')  # Fixed typo
    else:
        form = InternalMarksForm(instance=mark)
    
    return render(request, 'internal/update_internal_marks.html', {'form': form})
