from django.db import models

from django.contrib.auth.models import User


class Ingredient(models.Model):
    name = models.CharField(max_length=50, unique=True)

    objects = models.Manager()

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Recipe(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    instructions = models.TextField(blank=True, default="")
    ingredients = models.ManyToManyField(
        Ingredient, through="RecipeIngredient"
    )

    objects = models.Manager()

    def __str__(self):
        return self.name


class RecipeIngredient(models.Model):
    MG = "MG"
    G = "G"
    KG = "KG"
    ML = "ML"
    L = "L"

    UNITS = [
        (MG, "mg"),
        (G, "g"),
        (KG, "kg"),
        (ML, "mL"),
        (L, "L"),
    ]
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    quantity = models.FloatField()
    units = models.CharField(choices=UNITS, max_length=20)

    class Meta:
        unique_together = ["ingredient", "recipe"]

    objects = models.Manager()

    def __str__(self):
        return (
            f"{self.quantity} {self.units} "
            f"of {self.ingredient} for {self.recipe}"
        )
