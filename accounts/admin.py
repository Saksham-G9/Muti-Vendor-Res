from django.contrib import admin
from .models import CustomUser, UserProfile
from django.contrib.auth.admin import UserAdmin

# Register your models here.


class CustomUserAdmin(UserAdmin):
    list_display = ("email", "username", "first_name", "last_name", "role", "is_staff")
    search_fields = ("email", "username", "first_name", "last_name")
    readonly_fields = ("date_joined",)
    filter_horizontal = ()
    list_filter = ()

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            "Personal info",
            {"fields": ("first_name", "last_name", "username", "phone_number", "role")},
        ),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser")}),
        ("Important dates", {"fields": ("date_joined",)}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "username",
                    "first_name",
                    "last_name",
                    "phone_number",
                    "role",
                    "password1",
                    "password2",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                ),
            },
        ),
    )


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(UserProfile)
