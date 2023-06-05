from django.shortcuts import render, redirect
from tasks.forms import TaskForm
from tasks.models import Task
from django.contrib.auth.decorators import login_required


@login_required
def view_create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_projects")
    else:
        form = TaskForm()
    context = {"form": form}
    return render(request, "tasks/create_task.html", context)


@login_required
def view_my_task(request):
    my_task = Task.objects.filter(assignee=request.user)
    context = {"my_task": my_task}
    return render(request, "tasks/my_task.html", context)
