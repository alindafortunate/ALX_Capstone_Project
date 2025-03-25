from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm, CustomUserChangeForm

User = get_user_model()


class CustomeUserAdmin(UserAdmin):
    list_display = ["email", "username", "is_staff", "active_status"]
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    model = User

    fieldsets = (
        (None, {"fields": ["email", "username", "active_status", "password"]}),
    )
    add_fieldsets = (
        (
            None,
            {
                "fields": [
                    "email",
                    "username",
                    "active_status",
                    "password1",
                    "password2",
                ]
            },
        ),
    )


admin.site.register(User, CustomeUserAdmin)
