from django.db import models
from django.conf import settings
from django.utils.text import slugify
from datetime import datetime
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_post")
    caption = models.TextField(blank=True)
    image = models.ImageField(upload_to="post/image/%Y/%m/%d")
    video = models.FileField(upload_to="post/video/%Y/%m/%d", blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.BooleanField(default=False)
    edit_time = models.DateTimeField(auto_now=True)
    slug = models.SlugField(blank=True, max_length=300)
    user_like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="post_like", blank=True)
    total_likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.user) + " " + str(datetime.now())

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(str(self.user) + str(datetime.now()))
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("post:detail", kwargs={"id": self.id, "slug": self.slug})

class Comments(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_comments")
    text = models.TextField()
    release_date = models.DateTimeField(auto_now_add=True)
    edited = models.BooleanField(default=False)
    edit_date = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="comments_like", blank=True)

    def __str__(self):
        return f"{self.post.id} {self.user}"