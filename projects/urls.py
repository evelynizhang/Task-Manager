from django.urls import path
from projects.views import all_projects

urlpatterns = [
    path("", all_projects, name="list_projects"),
]
