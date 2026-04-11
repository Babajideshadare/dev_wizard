from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.shortcuts import redirect, render

from .forms import CustomUserCreationForm, DeveloperProfileForm
from .models import DeveloperProfile


def login_view(request):
    """
    Real login view using Django's AuthenticationForm.
    GET: show form
    POST: validate and log the user in
    """
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("curriculum:home")
    else:
        form = AuthenticationForm(request)

    return render(request, "accounts/login.html", {"form": form})


def register_view(request):
    """
    Registration view using CustomUserCreationForm.
    GET: show form
    POST: validate and create user, then log them in.
    """
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("curriculum:home")
    else:
        form = CustomUserCreationForm()

    return render(request, "accounts/register.html", {"form": form})


@login_required
def profile_view(request):
    """
    Read-only profile summary page, showing DeveloperProfile in a professional layout.
    """
    profile, created = DeveloperProfile.objects.get_or_create(user=request.user)
    # Pass user_email separately for clarity
    context = {
        "profile": profile,
        "user_email": request.user.email,
    }
    return render(request, "accounts/profile.html", context)


@login_required
def profile_edit_view(request):
    """
    Profile edit page (form) for DeveloperProfile + email.
    """
    profile, created = DeveloperProfile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        form = DeveloperProfileForm(request.POST, request.FILES, instance=profile, user=request.user)
        if form.is_valid():
            form.save()
            return redirect("accounts:profile")
    else:
        form = DeveloperProfileForm(instance=profile, user=request.user)

    return render(request, "accounts/profile_edit.html", {"form": form})


@login_required
def logout_view(request):
    """
    Log the user out and redirect to the home page.
    """
    logout(request)
    return redirect("curriculum:home")


@login_required
def password_change_view(request):
    """
    Allow the logged-in user to change their password.
    """
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            # Keep the user logged in after changing password
            update_session_auth_hash(request, user)
            return redirect("accounts:profile")
    else:
        form = PasswordChangeForm(request.user)

    return render(request, "accounts/password_change.html", {"form": form})