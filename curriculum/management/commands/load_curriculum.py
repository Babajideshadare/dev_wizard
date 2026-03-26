from django.core.management.base import BaseCommand
from django.db import transaction

from curriculum.models import Category, Topic, Objective, Task, Checker
from curriculum.seed_data import CURRICULUM


class Command(BaseCommand):
    help = "Load initial curriculum data (Categories, Topics, Objectives, Tasks, Checkers) into the database."

    @transaction.atomic
    def handle(self, *args, **options):
        """
        Read the CURRICULUM structure from seed_data.py and create/update
        Category, Topic, Objective, Task, and Checker records.

        This command is idempotent: running it multiple times will not create duplicates.
        """
        categories_data = CURRICULUM.get("categories", [])

        created_counts = {
            "categories": 0,
            "topics": 0,
            "objectives": 0,
            "tasks": 0,
            "checkers": 0,
        }

        for cat_data in categories_data:
            category, cat_created = Category.objects.get_or_create(
                slug=cat_data["slug"],
                defaults={
                    "name": cat_data["name"],
                    "description": cat_data.get("description", ""),
                    "order": cat_data.get("order", 0),
                },
            )
            if not cat_created:
                # Update fields if they changed in seed_data
                category.name = cat_data["name"]
                category.description = cat_data.get("description", "")
                category.order = cat_data.get("order", 0)
                category.save()
            else:
                created_counts["categories"] += 1

            for topic_data in cat_data.get("topics", []):
                topic, topic_created = Topic.objects.get_or_create(
                    category=category,
                    slug=topic_data["slug"],
                    defaults={
                        "title": topic_data["title"],
                        "description": topic_data.get("description", ""),
                        "order": topic_data.get("order", 0),
                    },
                )
                if not topic_created:
                    topic.title = topic_data["title"]
                    topic.description = topic_data.get("description", "")
                    topic.order = topic_data.get("order", 0)
                    topic.save()
                else:
                    created_counts["topics"] += 1

                # Objectives
                for index, obj_desc in enumerate(topic_data.get("objectives", []), start=1):
                    objective, obj_created = Objective.objects.get_or_create(
                        topic=topic,
                        description=obj_desc,
                        defaults={"order": index},
                    )
                    if not obj_created:
                        objective.order = index
                        objective.save()
                    else:
                        created_counts["objectives"] += 1

                # Tasks
                for task_data in topic_data.get("tasks", []):
                    task, task_created = Task.objects.get_or_create(
                        topic=topic,
                        title=task_data["title"],
                        defaults={
                            "instructions": task_data.get("instructions", ""),
                            "order": task_data.get("order", 0),
                            "is_mandatory": task_data.get("is_mandatory", True),
                        },
                    )
                    if not task_created:
                        task.instructions = task_data.get("instructions", "")
                        task.order = task_data.get("order", 0)
                        task.is_mandatory = task_data.get("is_mandatory", True)
                        task.save()
                    else:
                        created_counts["tasks"] += 1

                    # Checkers
                    for index, checker_desc in enumerate(task_data.get("checkers", []), start=1):
                        checker, checker_created = Checker.objects.get_or_create(
                            task=task,
                            description=checker_desc,
                            defaults={"order": index},
                        )
                        if not checker_created:
                            checker.order = index
                            checker.save()
                        else:
                            created_counts["checkers"] += 1

        # Print summary
        self.stdout.write(self.style.SUCCESS("Curriculum load complete."))
        self.stdout.write(
            self.style.SUCCESS(
                f"Created: "
                f"{created_counts['categories']} categories, "
                f"{created_counts['topics']} topics, "
                f"{created_counts['objectives']} objectives, "
                f"{created_counts['tasks']} tasks, "
                f"{created_counts['checkers']} checkers."
            )
        )