import pathlib
from pantry.core.models import Ingredient, Recipe, RecipeIngredient
from django.core.management.base import BaseCommand
from django.db import IntegrityError
from django.contrib.auth.models import User


def insert_ingredients():

    path = pathlib.Path(__file__).parent.absolute()
    with open(f"{path}/ingredients.txt") as f:
        data = f.readlines()

    for line in data:
        i = Ingredient(name=line.strip().lower())
        try:
            i.save()
            print(f"Saving {i.name}")
        except IntegrityError:
            pass


def create_user():
    try:
        User.objects.create_user(
            first_name="Shane",
            last_name="Kennedy",
            username="shane.kennedy9@gmail.com",
            email="shane.kennedy9@gmail.com",
        )
    except IntegrityError:
        pass


def create_recipe():
    name = "porbably something gross"
    instructions = "please never make this"
    ingredients = Ingredient.objects.all()[:5]
    author = User.objects.first()
    recipe = Recipe.objects.create(author=author, name=name, instructions=instructions)
    for ingredient in ingredients:
        RecipeIngredient.objects.create(
            ingredient=ingredient, recipe=recipe, quantity=1, units="G"
        )


class Command(BaseCommand):
    help = "Inserts ingredients to database"

    def handle(self, *args, **options):
        insert_ingredients()
        create_user()
        create_recipe()
