from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser


class SignUpView(View):
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, "signup.html", context={"form": form})

    def post(self, request):
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("login")
        return render(request, "signup.html", context={"form": form})


class LoginView(View):
    def get(self, request):
        form = AuthenticationForm(request=request)
        return render(request, "login.html", {"form": form})

    def post(self, request):
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("index")
        return render(
            request,
            "login.html",
            {
                "error": "Login yoki parol xato",
                "form": form,
            },
        )


class LogOutView(View):
    def post(self, request):
        logout(request)
        return redirect("index")


class ProfileView(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        user_p = get_object_or_404(CustomUser, pk=self.kwargs.get("pk"))
        return user_p == self.request.user

    def get(self, request, pk):
        user_p = get_object_or_404(CustomUser, pk=pk)
        return render(request, "profile.html", {"profile_user": user_p})


class EditProfileView(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        user_p = get_object_or_404(CustomUser, pk=self.kwargs.get("pk"))
        return user_p == self.request.user

    def get(self, request, pk):
        form = CustomUserChangeForm(instance=request.user)
        return render(request, "update_profile.html", {"form": form})

    def post(self, request, pk):
        form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("profile", pk=request.user.pk)
        return render(request, "update_profile.html", {"form": form})


class PasswordChange(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        user_data = get_object_or_404(CustomUser, pk=self.kwargs.get("pk"))

        return user_data == self.request.user

    def get(self, request, pk):
        form = PasswordChangeForm(user=request.user)
        return render(request, "password_change.html", {"form": form})

    def post(self, request, pk):
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect("profile", pk=user.pk)

        return render(request, "password_change.html", {"form": form})