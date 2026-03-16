from django.conf import settings
from django.db import models

# Create your models here.
class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True

class category(TimeStampedModel):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True)
    description = models.TimeField(blank=True)
    order = models.PositiveBigIntegerField(default=0)

    class Meta:
        ordering = ["order", "name"]

    def __str__(self):
        return self.name
    
class Topic(TimeStampedModel):
    category = models.ForeignKey(
        category,
        on_delete=models.CASCADE,
        related_name="topics",
    )

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220)
    description = models.TextField(blank=True)
    order= models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", 'title']
        unique_together = ("category", "slug")

    def __str__(self):
        return f"(self.category.name) - {self.title}"
    
class Objective(TimeStampedModel):
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
        return f"{self.topic.title}" - "{self.title}"