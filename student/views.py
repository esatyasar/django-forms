from .forms import StudentForm
from django.shortcuts import render


def index(request):
    return render(request, 'student/index.html')


def student_page(request):
    form = StudentForm()
    context = {
        	'form': form
    }
    return render(request,'student/student.html', context)