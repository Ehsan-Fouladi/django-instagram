from django.shortcuts import render
from post.models import Post
from actions.models import Action
from account.models import User

def home(request):
    user = request.user
    posts = Post.objects.filter(user=user).order_by("-created")
    if user.following.all():
        for friend in user.following.all():
            friend_post = Post.objects.filter(user=friend)
            posts = (posts | friend_post)
    actions = Action.objects.exclude(user=user).order_by("-created")
    following_ids = user.following.values_list("id", flat=True)
    if following_ids:
        actions = actions.filter(user_id__in=following_ids)[:10]
    user_following = User.objects.filter(id__in=following_ids)
    suggest_list = User.objects.none()
    for follow in user_following.all():
        for suggest_user in follow.following.all():
            if not suggest_user.id in following_ids and suggest_user != user:
                suggest_user = User.objects.filter(id=suggest_user.id)
                suggest_list |= suggest_user
    suggest_list = suggest_list[:10]
    return render(request, "pages/home.html", {"post": posts, "action": actions, "suggest": suggest_list})

def explore(request):
    posts = Post.objects.order_by("-total_likes")
    context = {"posts" : posts}
    return render(request, template_name="pages/explore.html", context=context)