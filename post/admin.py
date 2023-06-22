from django.contrib import admin
from .models import Post, Comments


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["user", "created", "image", "edit_time", "slug", "edited"]
    list_filter = ["created", "edited"]
    search_fields = ["user", "created"]

@admin.register(Comments)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["post", "user", "id"]