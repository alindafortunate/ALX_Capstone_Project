from django.urls import path
from .views import (
    UserListApiView,
    UserCreateApiView,
    UserDetailApiView,
    UserUpdateApiView,
    UserDeleteApiView,
)

urlpatterns = [
    path("users/", UserListApiView.as_view(), name="users"),
    path("user/create/", UserCreateApiView.as_view(), name="create-user"),
    path("user/<int:pk>/", UserDetailApiView.as_view(), name="user-detail"),
    path("user/<int:pk>/update/", UserUpdateApiView.as_view(), name="update-user"),
    path("user/<int:pk>/delete/", UserDeleteApiView.as_view(), name="delete-user"),
]
