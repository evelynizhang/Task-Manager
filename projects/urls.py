from django.urls import path
from projects.views import (
    all_projects,
    view_single_project,
    create_new_project,
    all_tasks_in_a_project,
    all_incompleted_tasks_in_a_project,
    all_completed_tasks_in_a_project,
    view_every_project,
)

urlpatterns = [
    path("", all_projects, name="list_projects"),
    path("<int:id>/", view_single_project, name="show_project"),
    path("create/", create_new_project, name="create_project"),
    path(
        "<int:id>/tasks",
        all_tasks_in_a_project,
        name="show_all_tasks_in_a_project",
    ),
    path(
        "<int:id>/incompleted_tasks",
        all_incompleted_tasks_in_a_project,
        name="all_incompleted_tasks_in_a_project",
    ),
    path(
        "<int:id>/completed_tasks",
        all_completed_tasks_in_a_project,
        name="all_completed_tasks_in_a_project",
    ),
    path(
        "all",
        view_every_project,
        name="view_every_project",
    ),
]
