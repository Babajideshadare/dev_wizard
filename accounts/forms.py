from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import DeveloperProfile


class CustomUserCreationForm(UserCreationForm):
    """
    Registration form that includes email in addition to username and password.
    """
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class DeveloperProfileForm(forms.ModelForm):
    """
    Profile edit form for the DeveloperProfile plus the User's email field.
    """
    email = forms.EmailField(required=True)

    class Meta:
        model = DeveloperProfile
        fields = [
            "full_name",
            "headline",
            "location",
            "bio",
            "years_of_experience",
            "current_role",
            "website_url",
            "github_url",
            "linkedin_url",
            "primary_tech_stack",
            "spoken_languages",
            "availability",
            "education_summary",
            "profile_picture",
        ]

    def __init__(self, *args, **kwargs):
        # We expect current user to be passed in from the view.
        self.user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
        if self.user is not None:
            self.fields["email"].initial = self.user.email

    def _normalize_url(self, url):
        """
        If the user enters a URL without http/https, prefix it with https://
        so Django's URLField accepts it.
        """
        if url and not url.startswith(("http://", "https://")):
            url = "https://" + url
        return url

    def clean_website_url(self):
        url = self.cleaned_data.get("website_url")
        return self._normalize_url(url)

    def clean_github_url(self):
        url = self.cleaned_data.get("github_url")
        return self._normalize_url(url)

    def clean_linkedin_url(self):
        url = self.cleaned_data.get("linkedin_url")
        return self._normalize_url(url)

    def save(self, commit=True):
        profile = super().save(commit=False)
        if self.user is not None:
            profile.user = self.user
        if commit:
            profile.save()
            # Also update the User's email
            if self.user is not None:
                self.user.email = self.cleaned_data["email"]
                self.user.save()
        return profile