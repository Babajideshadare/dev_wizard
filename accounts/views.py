from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from django.http import HttpResponse


def login_view(request):
    """
    Real login view using Django's AuthenticationForm.
    GET: show form
    POST: validate and log the user in
    """
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # AuthenticationForm already checked username/password
            user = form.get_user()
            login(request, user)
            # Redirect to home for now; later we can use 'next' param
            return redirect("curriculum:home")
    else:
        form = AuthenticationForm(request)

    return render(request, "accounts/login.html", {"form": form})


def register_view(request):
    """
    Placeholder registration view.
    We'll implement real registration in Step 6 Checker 3.
    """
    return HttpResponse("Register page (placeholder)")


@login_required
def profile_view(request):
    """
    Simple profile page to test login status.
    Later we'll expand this with real profile info and progress.
    """
    return HttpResponse(f"Profile page - logged in as {request.user.username}")


@login_required
def logout_view(request):
    """
    Log the user out and redirect to the home page.
    """
    logout(request)
    return redirect("curriculum:home")