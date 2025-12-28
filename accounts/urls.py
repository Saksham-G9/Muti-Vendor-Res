from django.urls import include, path
from . import views

urlpatterns = [
    path("register-user/", views.register_user, name="register_user"),
]
