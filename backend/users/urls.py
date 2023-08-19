from django.urls import path
from django.contrib.auth import views as auth_views
from .views import RegisterView, LoginView, logout_view

app_name = "users"

urlpatterns = [
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="users/login.html"),
        name="login",
    ),
    path(
        "register/",
        RegisterView.as_view(),
        name="register",
    ),
    path("logout/", logout_view, name="user_logout"),
]
