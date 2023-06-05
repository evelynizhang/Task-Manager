from django.urls import path
from tasks.views import view_create_task, view_my_task


urlpatterns = [
    path("create/", view_create_task, name="create_task"),
    path("mine/", view_my_task, name="show_my_tasks"),
]
