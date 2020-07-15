from django.db import models
from django.contrib.auth.models import User
from pantry.core.models import Recipe


class RecipeLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    class Meta:
        unique_together = ["user", "recipe"]
