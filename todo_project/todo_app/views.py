# todo_app/views.py
from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def index(request):
    tasks = Task.objects.all().order_by('-id')
    form = TaskForm()

    if request.method == 'POST':
        if 'add' in request.POST:
            form = TaskForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
        elif 'edit' in request.POST:
            task = Task.objects.get(id=request.POST['task_id'])
            task.title = request.POST['title']
            task.save()
            return redirect('/')
        elif 'delete' in request.POST:
            Task.objects.get(id=request.POST['task_id']).delete()
            return redirect('/')
        elif 'complete' in request.POST:
            task = Task.objects.get(id=request.POST['task_id'])
            task.completed = not task.completed
            task.save()
            return redirect('/')

    return render(request, 'todo_app/index.html', {'tasks': tasks, 'form': form})
