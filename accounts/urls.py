from django.urls import path
from .views import (
    EditProfileView,
    LogOutView,
    LoginView,
    PasswordChange,
    ProfileView,
    SignUpView,
)

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogOutView.as_view(), name="logout"),
    path("profile/<int:pk>/", ProfileView.as_view(), name="profile"),
    path("profile/<int:pk>/edit/", EditProfileView.as_view(), name="edit-profile"),
    path(
        "profile/<int:pk>/password/",
        PasswordChange.as_view(),
        name="password-change",
    ),
    path("signup", SignUpView.as_view(), name="signup-legacy"),
    path("login", LoginView.as_view(), name="login-legacy"),
    path("logout", LogOutView.as_view(), name="logout-legacy"),
    path("profile/<int:pk>", ProfileView.as_view(), name="profile-legacy"),
    path("profile/<int:pk>/edit", EditProfileView.as_view(), name="edit-profile-legacy"),
    path(
        "profile/<int:pk>/password",
        PasswordChange.as_view(),
        name="password-change-legacy",
    ),
]