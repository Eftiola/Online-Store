from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin


class UserAdminConfig(UserAdmin):
    model = User
    search_fields = (
        "email",
        "username",
    )
    list_filter = ("email", "username", "first_name", "is_active", "is_staff")
    ordering = ("-start_date",)
    list_display = ("email", "username", "first_name", "is_active", "is_staff")
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "username",
                )
            },
        ),
        ("Permissions", {"fields": ("is_staff", "is_active")}),
        ("Personal", {"fields": ("about",)}),
    )


admin.site.register(User, UserAdminConfig)
# admin.site.register(User)
