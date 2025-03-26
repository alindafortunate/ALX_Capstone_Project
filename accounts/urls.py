from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import (
    register,
    logout_view,
    UserListApiView,
    UserCreateApiView,
    UserDetailApiView,
    UserUpdateApiView,
    UserDeleteApiView,
)

urlpatterns = [
    path("users/", UserListApiView.as_view(), name="users"),
    path(
        "login/",
        LoginView.as_view(template_name="registration/login.html"),
        name="login",
    ),
    path("register/", register, name="register"),
    path("logout/", logout_view, name="logout"),
    path("user/create/", UserCreateApiView.as_view(), name="create-user"),
    path("user/<int:pk>/", UserDetailApiView.as_view(), name="user-detail"),
    path("user/<int:pk>/update/", UserUpdateApiView.as_view(), name="update-user"),
    path("user/<int:pk>/delete/", UserDeleteApiView.as_view(), name="delete-user"),
]
