from django.contrib import admin
from .models import Post
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["user", "created", "image", "edit_time", "slug", "edited"]
    list_filter = ["created", "edited"]
    search_fields = ["user", "created"]