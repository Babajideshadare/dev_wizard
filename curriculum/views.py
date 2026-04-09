from django.shortcuts import render, get_object_or_404
from .models import Category, Topic


def home(request):
    categories = Category.objects.all().order_by("order", "name")
    context = {
        "categories": categories,
    }
    return render(request, "curriculum/category_list.html", context)

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    topics = category.topics.all().order_by("order", "title")
    context = {
        "category": category,
        "topics": topics,
    }
    return render(request, "curriculum/category_detail.html", context)

def topic_detail(request, slug):
    topic = get_object_or_404(Topic, slug=slug)
    objectives = topic.objectives.all().order_by("order", "id")
    tasks = topic.tasks.all().order_by("order", "id")
    context = {
        "topic": topic,
        "objectives": objectives,
        "tasks": tasks,
    }
    return render(request, "curriculum/topic_detail.html", context)