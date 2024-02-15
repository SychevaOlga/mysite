from django.shortcuts import render, redirect

from .form import TaskForm
from .models import Task


def index(request):
    tasks = Task.objects.all()
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})

def about(request):
    return render(request, 'main/about.html' )

def blog(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            error = 'Форма была неверной'

    form = TaskForm()
    context = {
        'form': form
    }
    return render(request,'main/blog.html', context )

def contacts(request):
    return render(request,'main/contacts.html' )