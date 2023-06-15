from . import views
from django.urls import path
from django.contrib.auth import views as auth_view

# app_name = "account"
urlpatterns = [
    path("login/", views.LoginUser, name="login"),
    path("register/", views.Register, name="register"),
    # path("login/", auth_view.LoginView.as_view(), name="login"),
    path("verify/", views.Verify_Register, name="verify_register"),
    path("<str:username>/", views.Profile, name="profile"),
    path("profile/edit/", views.ProfileEdit, name="profile_edit"),
    path("logout/", auth_view.LogoutView.as_view(), name="logout"),
    # Password Change
    path("password_change/", auth_view.PasswordChangeView.as_view(), name="password_change"),
    path("password_change/done/", auth_view.PasswordChangeDoneView.as_view(), name="password_change_done"),
    # Password RESET
    path("password_reset/", auth_view.PasswordResetView.as_view(), name="password_reset"),
    path("password_reset/done/", auth_view.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path("reset/<uidb64>/<token>/", auth_view.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path("reset/done/", auth_view.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]
