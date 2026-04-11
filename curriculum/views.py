from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from .models import Category, Topic


@login_required
def home(request):
    """
    Home page: list all Categories (Python, Django, API, Capstone, etc.).
    User must be logged in to access this page.
    """
    categories = Category.objects.all().order_by("order", "name")
    context = {
        "categories": categories,
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
    """
    topic = get_object_or_404(Topic, slug=slug)
    objectives = topic.objectives.all().order_by("order", "id")
    tasks = topic.tasks.all().order_by("order", "id")

    context = {
        "topic": topic,
        "objectives": objectives,
        "tasks": tasks,
    }
    return render(request, "curriculum/topic_detail.html", context)