from django.conf import settings
from django.db import models


class DeveloperProfile(models.Model):
    """
    Extra profile information for a developer, linked one-to-one with Django's User.
    """

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="profile",
    )
    full_name = models.CharField(max_length=200)

    headline = models.CharField(
        max_length=200,
        blank=True,
        help_text="Short title, e.g. 'Backend Developer'",
    )
    location = models.CharField(
        max_length=200,
        blank=True,
        help_text="City / Country",
    )
    bio = models.TextField(
        blank=True,
        help_text="Short 'About me' paragraph.",
    )
    years_of_experience = models.PositiveIntegerField(
        blank=True,
        null=True,
        help_text="Total years of professional experience.",
    )
    current_role = models.CharField(
        max_length=200,
        blank=True,
        help_text="Your current role / company.",
    )
    website_url = models.URLField(
        blank=True,
        help_text="Personal website or portfolio URL.",
    )
    github_url = models.URLField(
        blank=True,
        help_text="GitHub profile URL.",
    )
    linkedin_url = models.URLField(
        blank=True,
        help_text="LinkedIn profile URL.",
    )
    primary_tech_stack = models.CharField(
        max_length=300,
        blank=True,
        help_text="Primary tech stack, e.g. 'Python, Django, DRF, PostgreSQL'.",
    )
    spoken_languages = models.CharField(
        max_length=200,
        blank=True,
        help_text="Spoken languages, e.g. 'English, French'.",
    )
    availability = models.CharField(
        max_length=200,
        blank=True,
        help_text="Availability, e.g. 'Open to work', 'Full-time only', 'Freelance'.",
    )
    education_summary = models.TextField(
        blank=True,
        help_text="Short education summary (not full list).",
    )

    profile_picture = models.ImageField(
        upload_to="profile_pics/",
        blank=True,
        null=True,
        help_text="Upload a profile picture/avatar.",
    )

    def __str__(self):
        return f"Profile for {self.user.username}"