from django.contrib.auth import views as auth_views
from django.urls import path

from registration import views

app_name = "registration"

urlpatterns = [
    path("login/", views.SigninView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("signup/", views.SignupView.as_view(), name="signup"),
    path(
        "change_password/",
        views.UserPasswordChangeView.as_view(),
        name="change_password",
    ),
    path(
        "reset_password/", views.UserPasswordResetView.as_view(), name="reset_password"
    ),
    path(
        "reset/<uidb64>/<token>/",
        views.UserPasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
]
