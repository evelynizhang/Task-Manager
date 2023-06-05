from django.urls import path
from tasks.views import view_create_task


urlpatterns = [
    path("create/", view_create_task, name="create_task"),
]
