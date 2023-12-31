from django.shortcuts import render, redirect, get_object_or_404
from projects.models import Project
from django.contrib.auth.decorators import login_required
from projects.forms import ProjectForm
from tasks.models import Task

# Create your views here.


@login_required
def all_projects(request):
    projects = Project.objects.filter(owner=request.user).order_by("due_date")
    for project in projects:
        tasks = Task.objects.filter(is_completed=False, project=project.id)
        project.incompleted_tasks = tasks
    context = {"all_projects": projects}
    return render(request, "projects/projects.html", context)


@login_required
def view_every_project(request):
    if request.user.is_superuser:
        project = Project.objects.all().order_by("due_date")
    context = {"every_project": project}
    return render(request, "projects/every_project.html", context)


@login_required
def all_tasks_in_a_project(request, id):
    tasks = Task.objects.filter(project=id).order_by("due_date")
    a_project = Project.objects.get(id=id)
    context = {"all_tasks_in_project": tasks, "a_project": a_project}
    return render(request, "tasks/all_tasks_in_project.html", context)


def all_incompleted_tasks_in_a_project(request, id):
    tasks = Task.objects.filter(is_completed=False, project=id)
    a_project = Project.objects.get(id=id)
    context = {
        "all_incompleted_tasks_in_a_project": tasks,
        "ain_project": a_project,
    }
    return render(
        request, "tasks/all_incompleted_tasks_in_a_project.html", context
    )


def all_completed_tasks_in_a_project(request, id):
    tasks = Task.objects.filter(is_completed=True, project=id)
    a_project = Project.objects.get(id=id)
    context = {
        "all_completed_tasks_in_a_project": tasks,
        "ac_project": a_project,
    }
    return render(
        request, "tasks/all_completed_tasks_in_a_project.html", context
    )


def redirect_home(request):
    return redirect("list_projects")


@login_required
def view_single_project(request, id):
    project = get_object_or_404(Project, id=id)
    task = Task.objects.filter(project=id).order_by("due_date")
    context = {"single_project": project, "all_t_in_P": task}
    return render(request, "projects/single_project.html", context)


@login_required
def create_new_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid:
            new_project = form.save(False)
            new_project.owner = request.user
            new_project.save()
            return redirect("list_projects")
    else:
        form = ProjectForm()
    context = {"form": form}
    return render(request, "projects/create_project.html", context)


def search_project(request):
    if request.method == "POST":
        searched = request.POST["searched"]
        project = Project.objects.filter(name__contains=searched)
        return render(
            request,
            "projects/search.project.html",
            {"searched": searched, "project": project},
        )
    else:
        return render(request, "projects/search.project.html", {})
