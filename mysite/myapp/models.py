from django.db import models
from django.contrib.auth.models import User as auth_user

# Create your models here.
class SuggestionModel(models.Model):
    suggestion = models.CharField(max_length=240)
    author = models.ForeignKey(
        auth_user,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return "%s"%(
            self.suggestion
        )

class CommentModel(models.Model):
    comment = models.CharField(max_length=240)
    author = models.ForeignKey(
        auth_user,
        on_delete=models.CASCADE
    )
    suggestion = models.ForeignKey(
        SuggestionModel,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return "%s"%(
            self.comment
        )