from django.urls import path
from projects.views import (
    all_projects,
    view_single_project,
    create_new_project,
)

urlpatterns = [
    path("", all_projects, name="list_projects"),
    path("<int:id>/", view_single_project, name="show_project"),
    path("create/", create_new_project, name="create_project"),
]
