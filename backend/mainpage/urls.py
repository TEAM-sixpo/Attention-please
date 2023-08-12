from django.urls import path
from . import views

urlpatterns = [
    path("check_login_status/", views.check_login_status, name="check_login_status"),
]
