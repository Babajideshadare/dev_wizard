from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.urls import reverse

from accounts.models import DeveloperProfile
from .models import Category, Topic, Checker, UserCheckerProgress


@login_required
def home(request):
    """
    Home page: list all Categories (Python, Django, API, Capstone, etc.).
    Also shows a sidebar profile summary card for the logged-in user.
    """
    categories = Category.objects.all().order_by("order", "name")
    profile, _ = DeveloperProfile.objects.get_or_create(user=request.user)

    context = {
        "categories": categories,
        "profile": profile,
        "user_email": request.user.email,
    }
    return render(request, "curriculum/category_list.html", context)


@login_required
def category_detail(request, slug):
    """
    Category detail page: show one Category and its Topics.
    User must be logged in to access this page.
    """
    category = get_object_or_404(Category, slug=slug)
    topics = category.topics.all().order_by("order", "title")
    context = {
        "category": category,
        "topics": topics,
    }
    return render(request, "curriculum/category_detail.html", context)


@login_required
def topic_detail(request, slug):
    """
    Topic detail page: show one Topic, its Objectives, and its Tasks (with Checkers).
    User must be logged in to access this page.
    Also includes per-user checker completion status, and can keep a specific
    task/checker section open based on query params.
    """
    topic = get_object_or_404(Topic, slug=slug)
    objectives = topic.objectives.all().order_by("order", "id")
    tasks = topic.tasks.all().prefetch_related("checkers").order_by("order", "id")

    # Load this user's progress for all checkers under this topic
    progress_qs = UserCheckerProgress.objects.filter(
        user=request.user,
        checker__task__topic=topic,
        is_completed=True,
    )
    completed_checker_ids = list(
        progress_qs.values_list("checker_id", flat=True)
    )

    # Determine which task (and its checker section) should be open
    open_task_id = request.GET.get("open_task")
    if open_task_id:
        try:
            open_task_id = int(open_task_id)
        except ValueError:
            open_task_id = None
    else:
        open_task_id = None

    context = {
        "topic": topic,
        "objectives": objectives,
        "tasks": tasks,
        "completed_checker_ids": completed_checker_ids,
        "open_task_id": open_task_id,
    }
    return render(request, "curriculum/topic_detail.html", context)


@login_required
def toggle_checker_completion(request, checker_id):
    """
    Toggle completion status for a single Checker for the current user.
    Redirects back to the topic detail page, keeping the relevant task/checkers
    open and scrolling to that checker.
    """
    checker = get_object_or_404(Checker, id=checker_id)
    topic_slug = checker.task.topic.slug

    if request.method == "POST":
        progress, _ = UserCheckerProgress.objects.get_or_create(
            user=request.user,
            checker=checker,
        )
        if progress.is_completed:
            progress.is_completed = False
            progress.completed_at = None
        else:
            progress.is_completed = True
            progress.completed_at = timezone.now()
        progress.save()

    # Build URL back to topic detail, with query param + anchor
    base_url = reverse("curriculum:topic-detail", kwargs={"slug": topic_slug})
    redirect_url = f"{base_url}?open_task={checker.task_id}#checker-{checker.id}"
    return redirect(redirect_url)