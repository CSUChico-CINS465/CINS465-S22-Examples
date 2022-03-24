from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User as auth_user

from . import models

def must_be_caps(value):
    if not value.isupper():
        raise forms.ValidationError("Not all upper case")
    # Always return the cleaned data
    return value

def must_be_bob(value):
    if not str(value).startswith("BOB"):
        raise forms.ValidationError("Needs to start with BOB")
    # Always return the cleaned data
    return value

def must_be_ten(value):
    if not len(value) > 10:
        raise forms.ValidationError("Needs to be more than 10 chars")
    # Always return the cleaned data
    return value

def must_be_unique(value):
    users = auth_user.objects.filter(email=value)
    if len(users) >= 1:
        raise forms.ValidationError("User with that email already exists")
    return value

class CommentForm(forms.Form):
    comment_field = forms.CharField(
        label='Comment',
        max_length=240,
    )

    def save(self, request, sugg_id):
        suggestion_instance = models.SuggestionModel.objects.get(id=sugg_id)
        comment_instance = models.CommentModel()
        comment_instance.comment = self.cleaned_data["comment_field"]
        comment_instance.author = request.user
        comment_instance.suggestion = suggestion_instance
        comment_instance.save()


class SuggestionForm(forms.Form):
    suggestion_field = forms.CharField(
        label='Suggestion',
        max_length=240,
    )
    image_field = forms.ImageField(
        label='Image',
        max_length=144,
        required=False
    )
    image_desc_field = forms.CharField(
        label='Image Description',
        max_length=240,
        required=False
    )

    def save(self, request):
        suggestion_instance = models.SuggestionModel()
        suggestion_instance.suggestion = self.cleaned_data["suggestion_field"]
        suggestion_instance.author = request.user
        suggestion_instance.image = self.cleaned_data["image_field"]
        suggestion_instance.image_description = self.cleaned_data["image_desc_field"]
        suggestion_instance.save()

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        label="Email",
        required=True,
        validators=[must_be_unique]
    )

    class Meta:
        model = auth_user
        fields = (
            "username",
            "email",
            "password1",
            "password2"
        )

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
