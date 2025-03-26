from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth import get_user_model
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
)
from .serializers import UserSerializer
from .forms import CustomUserCreationForm

User = get_user_model()


# Create your views here.
def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/accounts/login/")
    else:
        form = CustomUserCreationForm()
    context = {"form": form}

    return render(request, "accounts/register.html", context)


def logout_view(request):
    logout(request)
    return redirect("/accounts/login/")
    


class UserListApiView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserCreateApiView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailApiView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserUpdateApiView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDeleteApiView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
