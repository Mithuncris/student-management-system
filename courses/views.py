from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Course
from users.models import CustomUser
from django.contrib import messages
from .forms import CourseForm

# Check if user is a teacher
def is_teacher(user):
    return user.role == 'staff'

# Check if user is HOD
def is_hod(user):
    return user.role == 'hod'

# View to list all courses (HOD and staff access)
@login_required
@user_passes_test(lambda user: is_hod(user) or is_teacher(user))
def course_list_view(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})

# View to add a new course (HOD only)
@login_required
@user_passes_test(is_hod)
def add_course_view(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Course added successfully.")
            return redirect('courses:course_list')
        else:
            messages.error(request, "Failed to add course. Please correct the errors.")
    else:
        form = CourseForm()
    return render(request, 'courses/add_course.html', {'form': form})

# View to edit a course (HOD only)
@login_required
@user_passes_test(is_hod)
def edit_course_view(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, "Course updated successfully.")
            return redirect('courses:course_list')
        else:
            messages.error(request, "Failed to update course. Please correct the errors.")
    else:
        form = CourseForm(instance=course)
    return render(request, 'courses/edit_course.html', {'form': form, 'course': course})

# View to delete a course (HOD only)
@login_required
@user_passes_test(is_hod)
def delete_course_view(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
        course.delete()
        messages.success(request, "Course deleted successfully.")
        return redirect('courses:course_list')
    return render(request, 'courses/delete_course.html', {'course': course})

# View for a teacher to view their assigned courses
@login_required
@user_passes_test(is_teacher)
def teacher_courses_view(request):
    teacher = request.user
    courses = Course.objects.filter(teacher=teacher)
    return render(request, 'courses/teacher_courses.html', {'courses': courses})

# View for students to view the courses they are enrolled in
@login_required
def student_courses_view(request):
    student = request.user
    courses = Course.objects.filter(students=student)
    return render(request, 'courses/student_courses.html', {'courses': courses})


def create_course_view(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('courses:course_list')  # Redirect to a list of courses
    else:
        form = CourseForm()
    
    return render(request, 'courses/create_course.html', {'form': form})


def view_course_view(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(request, 'courses/view_course.html', {'course': course})