from django.test import TestCase
from ..models import Ingredient
from ..serializers import RecipeSerializer


class RecipeIngredientSerializerTests(TestCase):

    def test_Create_ValidData_ShowuldPerformCreate(self):
        # Arrange
        i = Ingredient.objects.create(name="cheese")
        recipe = {
            "name": "Pasta",
            "instructions": "Make pasta",
            "ingredients": [
                {"ingredient": i.id, "quantity": 5, "units": "G"},
            ],
        }
        serializer = RecipeSerializer(data=recipe)

        # Act
        serializer.is_valid()
        recipe = serializer.save()

        # Assert
        self.assertIsNotNone(recipe)
        recipe_ingredients = recipe.recipeingredient_set.all()
        self.assertEqual(1, recipe_ingredients.count())
        self.assertEqual(i.id, recipe_ingredients.first().ingredient_id)
        self.assertEqual(recipe.id, recipe_ingredients.first().recipe_id)
        self.assertEqual(5, recipe_ingredients.first().quantity)
        self.assertEqual("G", recipe_ingredients.first().units)

    def test_Create_NoName_DontCreateRecipe(self):
        # Arrange
        i = Ingredient.objects.create(name="cheese")
        recipe = {
            "name": "",
            "instructions": "Make pasta",
            "ingredients": [
                {"ingredient": i.id, "quantity": 5, "units": "G"},
            ],
        }
        serializer = RecipeSerializer(data=recipe)

        # Act
        serializer.is_valid()
        errors = serializer.errors

        # Assert
        self.assertIsNotNone(errors["name"])

    def test_Create_NoIngredientId_DontCreateRecipe(self):
        # Arrange
        recipe = {
            "name": "Pasta",
            "instructions": "Make pasta",
            "ingredients": [
                {"quantity": 5, "units": "G"},
            ],
        }
        serializer = RecipeSerializer(data=recipe)

        # Act
        serializer.is_valid()
        errors = serializer.errors

        # Assert
        self.assertIsNotNone(errors["ingredients"])
