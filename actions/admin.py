from django.contrib import admin
from .models import Action


@admin.register(Action)
class ActionAdmin(admin.ModelAdmin):
    list_display = ["user", "act", "target_ct", "target_id", "created"]
    list_filter = ["created"]
    search_fields = ["act"]