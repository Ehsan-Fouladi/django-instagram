from . import views
from django.urls import path
from django.contrib.auth import views as auth_view

app_name = "account"
urlpatterns = [
    # path("login/", views.LoginUser, name="login"),
    path("login/", auth_view.LoginView.as_view(), name="login"),
    path("profile/", views.Profile, name="profile"),
    path("logout/", auth_view.LogoutView.as_view(), name="logout"),
]
