from django.shortcuts import render, redirect, get_object_or_404
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
    my_task = Task.objects.filter(assignee=request.user).order_by("due_date")
    print(my_task)
    context = {"my_task": my_task}
    return render(request, "tasks/my_task.html", context)


@login_required
def edit_my_task(request, id):
    my_task = get_object_or_404(Task, id=id)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=my_task)
        if form.is_valid():
            form.save()
            return redirect("show_my_tasks")
    else:
        form = TaskForm(instance=my_task)
    context = {
        "my_task_object": my_task,
        "my_task_form": form,
    }
    return render(request, "tasks/edit.html", context)


def delete_my_task(request, id):
    model_instance = Task.objects.get(id=id)
    if request.method == "POST":
        model_instance.delete()
        return redirect("show_my_tasks")
    return render(request, "tasks/delete.html")


def view_each_task(request, id):
    each_task = get_object_or_404(Task, id=id)
    context = {"each_task": each_task}
    return render(request, "tasks/each_task.html", context)
