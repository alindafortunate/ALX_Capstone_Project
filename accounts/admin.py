from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class CustomeUserAdmin(UserAdmin):
    pass


admin.site.register(User, CustomeUserAdmin)
