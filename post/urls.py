from . import views
from django.urls import path

app_name = "post"
urlpatterns = [
    path("create/", views.post_create, name="create"),
    path("detail/<int:id>/<slug:slug>", views.post_detail, name="detail"),
    path("like/", views.post_like, name="like")
]