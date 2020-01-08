from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from crudApp.models import Student
from crudApp.forms import StudentForm
from django.contrib import messages

# Create your views here.


@login_required
def getStudents(request):
    students = Student.objects.all()
    return render(request, 'crudApp/home.html', {'stds': students})


@login_required
def createStudent(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student Created Successfully')
            return redirect('students_list')
    return render(request, 'crudApp/create.html', {'form': form})


@login_required
def updateStudent(request, id):
    student = Student.objects.get(id=id)
    if student:
        form = StudentForm(instance=student)
        if request.method == 'POST':
            form = StudentForm(request.POST, instance=student)
            if form.is_valid():
                form.save()
                messages.success(
                    request, 'Sudent Details Updated successfully')
                return redirect('students_list')
    return render(request, 'crudApp/update.html', {'form': form})


@login_required
def deleteStudent(request, id):
    student = Student.objects.get(id=id)
    if student:
        student.delete()
        messages.success(request, 'Sudent Deleted Successfully')
    else:
        messages.error(request, f'Student with {id} not avilable')
    return redirect('students_list')


def logout(request):
    return render(request, 'crudApp/logout.html')


# implementing crud operation using class based views
class StudentListView(ListView):
    model = Student
    # default template_name is modelName_list.html i.e student_list.html
    # default context_object_name is modelName_list i.e. student_list


class StudentDetailView(DetailView):
    model = Student
    # default template_name is modelName_detail.html i.e student_detail.html
    # default context_object_name is modelName in lower case i.e. student


class StudentCreateView(CreateView):
    model = Student
    fields = ('fullname', 'course', 'fee')
    # default template_name is modelName_form.html i.e student_form.html
    # default context_object_name is form


class StudentUpdateView(UpdateView):
    model = Student
    fields = ('course', 'fee')
    # default template_name is modelName_form.html i.e student_form.html
    # default context_object_name is form
    
