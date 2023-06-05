from django.shortcuts import render
from projects.models import Project

# Create your views here.


def all_projects(request):
    projects = Project.objects.all()
    context = {"all_projects": projects}
    return render(request, "projects/projects.html", context)
