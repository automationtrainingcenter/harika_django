from django.shortcuts import render, redirect
from crudApp.models import Student
from crudApp.forms import StudentForm
from django.contrib import messages

# Create your views here.


def getStudents(request):
    students = Student.objects.all()
    return render(request, 'crudApp/home.html', {'stds': students})


def createStudent(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student Created Successfully')
            return redirect('students_list')
    return render(request, 'crudApp/create.html', {'form': form})


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


def deleteStudent(request, id):
    student = Student.objects.get(id=id)
    if student:
        student.delete()
        messages.success(request, 'Sudent Deleted Successfully')
    else:
        messages.error(request, f'Student with {id} not avilable')
    return redirect('students_list')
