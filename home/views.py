from django.shortcuts import render
from post.models import Post


def home(request):
    user = request.user
    post = Post.objects.filter(user=user).order_by("-created")
    return render(request, "pages/home.html", {"post":post})