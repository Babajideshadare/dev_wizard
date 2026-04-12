from django.urls import path
from . import views

app_name = "curriculum"

urlpatterns = [
    path("", views.home, name="home"),
    path("category/<slug:slug>/", views.category_detail, name="category-detail"),
    path("topic/<slug:slug>/", views.topic_detail, name="topic-detail"),
    path("checker/<int:checker_id>/toggle/", views.toggle_checker_completion, name="toggle-checker"),
    path("progress/", views.progress_dashboard, name="progress-dashboard"),
]