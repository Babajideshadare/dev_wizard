from django.http import HttpResponse


def login_view(request):
    """
    Placeholder login view.
    Step 6 Checker 1: just prove URL wiring; real auth comes later.
    """
    return HttpResponse("Login page (placeholder)")


def register_view(request):
    """
    Placeholder registration view.
    """
    return HttpResponse("Register page (placeholder)")


def profile_view(request):
    """
    Placeholder profile view.
    Later this will show user info and progress.
    """
    return HttpResponse("Profile page (placeholder)")