from django.urls import path
from accounts.views import view_login, view_logout, view_signupform


urlpatterns = [
    path("login/", view_login, name="login"),
    path("logout/", view_logout, name="logout"),
    path("signup/", view_signupform, name="signup"),
]
