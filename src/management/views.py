from django.shortcuts import render

from .models import Task

from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def main_dashboard(request):
    if 'delete_task' in request.POST:
        task_to_delete = Task.objects.get(id=request.POST['delete_task'])
        task_to_delete.delete()
    elif 'title' in request.POST:
        
        title = request.POST.get('title')
        minutes = request.POST.get('minutes')
        description = request.POST.get('description')
        if title == "" or minutes == "":
            messages.error(request, 'Enter a proper title and/or minutes')
        else:
            Task.objects.create(user=request.user, title=title, minutes=minutes, description=description)
    tasks = Task.objects.filter(user=request.user)
    completed_tasks = tasks.filter(approved=True)
    total_minutes = 0
    for task in completed_tasks:
        total_minutes += task.minutes
    context = {
        'tasks': tasks,
        'total_minutes': total_minutes,
    }
    return render(request, 'team/dashboard.html', context)