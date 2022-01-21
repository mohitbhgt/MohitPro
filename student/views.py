from django.shortcuts import render, redirect
from .models import  Student
from .form import StudentForm


def student_list(request):
    students = Student.objects.all()
    context = {
        'students': students,
    }
    return render(request, 'list.html', context)

def create_student(request):
    form = StudentForm()

    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student-list')

    context = {
        'form': form,
    }
    return render(request, 'create.html',context)

def edit_student(request, pk):
    student = Student.objects.get(id=pk)
    form = StudentForm(instance=student)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student-list')

    context = {
        'student': student,
        'form': form,
    }
    return render(request, 'edit.html', context)

def delete_student(request, pk):
    student = Student.objects.get(id=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student-list')

    context = {
        'student': student,
    }
    return render(request, 'delete.html', context)