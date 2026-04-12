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
    Includes per-user checker completion status and a topic-level progress summary.
    """
    topic = get_object_or_404(Topic, slug=slug)
    objectives = topic.objectives.all().order_by("order", "id")
    tasks = topic.tasks.all().prefetch_related("checkers").order_by("order", "id")

    # Completed checkers for this user on this topic
    progress_qs = UserCheckerProgress.objects.filter(
        user=request.user,
        checker__task__topic=topic,
        is_completed=True,
    )
    completed_checker_ids = list(
        progress_qs.values_list("checker_id", flat=True)
    )
    completed_checkers = len(completed_checker_ids)

    # Total checkers in this topic
    total_checkers = Checker.objects.filter(task__topic=topic).count()

    if total_checkers > 0:
        progress_percent = int((completed_checkers / total_checkers) * 100)
    else:
        progress_percent = 0

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
        "total_checkers": total_checkers,
        "completed_checkers": completed_checkers,
        "progress_percent": progress_percent,
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


@login_required
def progress_dashboard(request):
    """
    Dashboard page showing overall and per-topic progress for the logged-in user.
    """
    # Overall progress (all checkers in the system)
    total_checkers = Checker.objects.count()
    completed_overall = UserCheckerProgress.objects.filter(
        user=request.user,
        is_completed=True,
    ).count()

    if total_checkers > 0:
        overall_percent = int((completed_overall / total_checkers) * 100)
    else:
        overall_percent = 0

    # Per-topic progress grouped by Category
    topics = Topic.objects.select_related("category").order_by(
        "category__order",
        "order",
        "title",
    )

    from collections import OrderedDict
    categories_progress = OrderedDict()  # preserve order

    for topic in topics:
        topic_total = Checker.objects.filter(task__topic=topic).count()
        topic_completed = UserCheckerProgress.objects.filter(
            user=request.user,
            checker__task__topic=topic,
            is_completed=True,
        ).count()

        if topic_total > 0:
            topic_percent = int((topic_completed / topic_total) * 100)
        else:
            topic_percent = 0

        cat = topic.category
        if cat.id not in categories_progress:
            categories_progress[cat.id] = {
                "category": cat,
                "topics": [],
            }
        categories_progress[cat.id]["topics"].append(
            {
                "topic": topic,
                "total": topic_total,
                "completed": topic_completed,
                "percent": topic_percent,
            }
        )

    context = {
        "overall_total": total_checkers,
        "overall_completed": completed_overall,
        "overall_percent": overall_percent,
        "categories_progress": list(categories_progress.values()),
    }
    return render(request, "curriculum/progress_dashboard.html", context)