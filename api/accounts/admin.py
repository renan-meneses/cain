from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


class UserAdminConfig(UserAdmin):
    search_fields = ("email", "user_name")
    ordering = ("start_date",)

    list_display = ("email", "id", "user_name", "is_active", "is_staff")

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "user_name",
                )
            },
        ),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser")}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "user_name",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                ),
            },
        ),
    )


admin.site.register(User, UserAdminConfig)
