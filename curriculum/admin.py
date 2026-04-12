from django.contrib import admin
from .models import Category, Topic, Objective, Task, Checker, UserCheckerProgress

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "order", "created_at")
    list_editable = ("order",)
    search_fields = ("name", "description")
    prepopulated_fields = {"slug": ("name",)}
    ordering = ("order", "name")

class ObjectiveInline(admin.TabularInline):
    model = Objective
    extra = 1

class TaskInline(admin.TabularInline):
    model = Task
    extra = 1

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "order")
    list_filter = ("category",)
    list_editable = ("order",)
    search_fields = ("title", "description")
    prepopulated_fields = {"slug": ("title",)}
    inlines = [ObjectiveInline, TaskInline]
    ordering = ("category", "order", "title")

@admin.register(Objective)
class ObjetiveAdmin(admin.ModelAdmin):
    list_display = ("short_description", "topic", "order")
    list_filter = ("topic__category", "topic")
    list_editable = ("order",)
    search_fields = ("description",)
    ordering = ("topic__category", "topic", "order")

    def short_description(self, obj):
        return (obj.description[:60] + "...") if len(obj.description) > 60 else obj.description
    short_description.short_description = "Objective"

class CheckerInline(admin.TabularInline):
    model = Checker
    extra = 1

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "topic", "is_mandatory", "order", "created_at")
    list_filter = ("topic__category", "topic", "is_mandatory")
    list_editable = ("order", "is_mandatory")
    search_fields = ("title", "instructions")
    inlines = [CheckerInline]
    ordering = ("topic__category", "topic", "order")

@admin.register(Checker)
class CheckerAdmin(admin.ModelAdmin):
    list_display = ("short_description", "task", "order")
    list_filter = ("task__topic__category", "task__topic")
    list_editable = ("order",)
    search_fields = ("description",)
    ordering = ("task__topic__category", "task__topic", "task", "order")

    def short_description(self, obj):
        return (obj.description[:60] + "...") if len(obj.description) > 60 else obj.description
    short_description.short_description = "Checker"

@admin.register(UserCheckerProgress)
class UserCheckerProgressAdmin(admin.ModelAdmin):
    list_display = ("user", "checker", "is_completed", "completed_at", "created_at")
    list_filter = ("is_completed", "checker__task__topic__category", "checker__task__topic")
    search_fields = ("user__username", "checker__description", "checker__task__title")
    autocomplete_fields = ("user", "checker")
    ordering = ("-updated_at",)
