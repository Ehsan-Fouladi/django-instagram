from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserChangeForm, UserCreationForm
from .models import User


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ["email", "username", "phone", "first_name", "last_name", "is_staff", "is_admin"]
    list_filter = ["is_admin", "is_staff"]

    fieldsets = [
        (None, {"fields": ["email", "username", "password"]}),
        ("Personal info", {"fields": ["phone", "first_name", "last_name"]}),
        ("Permissions", {"fields": ["is_admin", "is_staff", "is_active", "is_superuser"]}),
    ]
    search_fields = ["email", "username"]
    ordering = ["username", "phone"]
    filter_horizontal = []

admin.site.register(User, UserAdmin)
admin.site.unregister(Group)