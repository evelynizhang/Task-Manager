from django.shortcuts import render, redirect, get_object_or_404
from projects.models import Project
from django.contrib.auth.decorators import login_required


# Create your views here.


@login_required
def all_projects(request):
    projects = Project.objects.filter(owner=request.user)
    context = {"all_projects": projects}
    return render(request, "projects/projects.html", context)


def redirect_home(request):
    return redirect("list_projects")


@login_required
def view_single_project(request, id):
    project = get_object_or_404(Project, id=id)
    context = {"single_project": project}
    return render(request, "projects/single_project.html", context)
