from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from .forms import UserCreationForm, UserChangeForm


User = get_user_model()


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ["phone_number", "first_name", "is_admin"]
    list_filter = ["is_admin", "phone_number"]
    readonly_fields = ["last_login"]

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "phone_number",
                    "first_name",
                    "password",
                    "birth_date",
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_admin",
                    "last_login",
                    "joined_data",
                )
            },
        ),
    )

    add_fieldsets = (
        (
            None,
            {
                "fields": (
                    "phone_number",
                    "first_name",
                    "last_name",
                    "birth_date",
                    "password1",
                    "password2",
                )
            },
        ),
    )

    readonly_fields = [
        "joined_data",
    ]
    search_fields = ["phone_number", "first_name", "last_name"]
    ordering = ("joined_data",)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
