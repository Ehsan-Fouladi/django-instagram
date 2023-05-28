from . import views
from django.urls import path
from django.contrib.auth import views as auth_view

app_name = "account"
urlpatterns = [
    # path("login/", views.LoginUser, name="login"),
    path("login/", auth_view.LoginView.as_view(), name="login"),
    path("profile/", views.Profile, name="profile"),
    path("password_change/", auth_view.PasswordChangeView.as_view(), name="password_change"),
    path("password_change/done/", auth_view.PasswordChangeDoneView.as_view(), name="password_done"),
    path("logout/", auth_view.LogoutView.as_view(), name="logout"),
]
