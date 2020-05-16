from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=50, unique=True)

    objects = models.Manager()


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    instructions = models.TextField(blank=True, default='')
    ingredients = models.ManyToManyField(
        Ingredient,
        through='RecipeIngredient'
    )

    objects = models.Manager()


class RecipeIngredient(models.Model):
    MG = "MG"
    G = "G"
    KG = "KG"
    ML = "ML"
    L = "L"

    UNITS = [
        (MG, 'mg'),
        (G, 'g'),
        (KG, 'kg'),
        (ML, 'mL'),
        (L, 'L'),
    ]
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    quantity = models.FloatField()
    units = models.CharField(choices=UNITS, max_length=20)

    class Meta:
        unique_together = ['ingredient', 'recipe']

    objects = models.Manager()
