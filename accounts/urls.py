from django.urls import path
from accounts.views import view_login


urlpatterns = [
    path("login/", view_login, name="login"),
]
