from django.conf import settings
from django.db import models


class TimeStampedModel(models.Model):
    """Abstract base model to add created_at and updated_at timestamps."""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(TimeStampedModel):
    """
    High-level grouping, e.g. 'Python', 'Data Base', 'Django', 'API', 'Capstone Projects'.
    Global: same for all users.
    """
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True)
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "name"]

    def __str__(self):
        return self.name


class Topic(TimeStampedModel):
    """
    Specific area inside a Category, e.g. 'Functions, Data Structures and Modules'.
    Global: same for all users.
    """
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="topics",
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220)
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "title"]
        unique_together = ("category", "slug")

    def __str__(self):
        return f"{self.category.name} - {self.title}"


class Objective(TimeStampedModel):
    """
    A specific learning objective under a Topic.
    Global: same for all users.
    """
    topic = models.ForeignKey(
        Topic,
        on_delete=models.CASCADE,
        related_name="objectives",
    )
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return self.description[:80]


class Task(TimeStampedModel):
    """
    A concrete activity the learner must perform within a Topic.
    Global: defined by you, the same for all users.
    """
    topic = models.ForeignKey(
        Topic,
        on_delete=models.CASCADE,
        related_name="tasks",
    )
    title = models.CharField(max_length=255)
    instructions = models.TextField()
    order = models.PositiveIntegerField(default=0)
    is_mandatory = models.BooleanField(default=True)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return f"{self.topic.title} - {self.title}"


class Checker(TimeStampedModel):
    """
    A single check/requirement for a Task.
    Example: 'Checks for files exists and not empty'.
    """
    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        related_name="checkers",
    )
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return f"{self.task.title} - {self.description[:50]}"


class UserCheckerProgress(TimeStampedModel):
    """
    Per-user progress for a single Checker.
    One row = one user's status for one Checker.
    """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="checker_progress",
    )
    checker = models.ForeignKey(
        Checker,
        on_delete=models.CASCADE,
        related_name="user_progress",
    )
    is_completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        unique_together = ("user", "checker")
        verbose_name = "User checker progress"
        verbose_name_plural = "User checker progress"

    def __str__(self):
        status = "✓" if self.is_completed else "…"
        return f"{self.user.username} {status} {self.checker.description[:40]}"