from django.urls import path
from tasks.views import (
    view_create_task,
    view_my_task,
    edit_my_task,
    delete_my_task,
    view_each_task,
)


urlpatterns = [
    path("create/", view_create_task, name="create_task"),
    path("mine/", view_my_task, name="show_my_tasks"),
    path("<int:id>/edit/", edit_my_task, name="edit_my_task"),
    path("<int:id>/delete/", delete_my_task, name="delete_my_task"),
    path("<int:id>/", view_each_task, name="view_each_task"),
]
