from django.shortcuts import render
from .models import Category


def home(request):
    categories = Category.objects.all().order_by("order", "name")
    context = {
        "categories": categories,
    }
    return render(request, "curriculum/category_list.html", context)