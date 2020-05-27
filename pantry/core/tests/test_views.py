from rest_framework import status
from ..models import Ingredient, Recipe, RecipeIngredient
from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth.models import User


class IngredientsAPITests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.ingredient_names = [
            "apple",
            "cucumber",
            "artichoke",
            "banana",
            "pepper",
        ]
        cls.user = User.objects.create_user(
            email="test@123.com", username="test123", password="123456",
        )
        [Ingredient.objects.create(name=name) for name in cls.ingredient_names]

        cls.url = reverse("ingredients")

    def setUp(self):
        self.client.force_authenticate(user=self.user)

    def test_GET__ReturnAllIngredients(self):
        # Act
        response = self.client.get(self.url)

        # Assert
        expected_num_ingredients = Ingredient.objects.count()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), expected_num_ingredients)

        response_names = [item["name"] for item in response.data]

        for name in response_names:
            self.assertIn(name, self.ingredient_names)

    def test_GET_SearchByName_ReturFiiteredResults(self):
        params = {
            "item": "artichoke",
        }

        response = self.client.get(self.url, params)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual("artichoke", response.data[0]["name"])

    def test_GET_EmptySearch_ShouldReturnAllIngredients(self):
        expected_num_ingredients = Ingredient.objects.count()
        params = {
            "item": "",
        }

        response = self.client.get(self.url, params)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), expected_num_ingredients)

    def test_POST_IngredientAlreadyExists_IngredientNotCreated(self):
        # Arrange
        Ingredient.objects.create(name="Kiwi")
        new_ingredient_data = {"name": "Kiwi"}

        # Act
        response = self.client.post(self.url, new_ingredient_data)

        # Assert
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_POST_VaildData_CreateNewIngredient(self):
        # Arrange
        ingredient_data = {"name": "Pear"}

        # Act
        response = self.client.post(self.url, ingredient_data)

        # Assert
        pear_ingredient = Ingredient.objects.filter(name="Pear").first()
        self.assertIsNotNone(pear_ingredient)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class RecipesAPITests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            email="test@123.com", username="test123", password="123456",
        )

    def setUp(self):
        self.client.force_authenticate(user=self.user)

    def test_GET__ReturnAllRecipes(self):
        # Arrange
        recipe_name = "Pasta"
        recipe_instructions = "Make the pasta"
        ingredient1 = Ingredient.objects.create(name="tomato")
        ingredient2 = Ingredient.objects.create(name="basil")
        recipe = Recipe.objects.create(
            name=recipe_name, instructions=recipe_instructions
        )
        RecipeIngredient.objects.create(
            recipe=recipe, ingredient=ingredient1, quantity=300, units="G",
        )
        RecipeIngredient.objects.create(
            recipe=recipe, ingredient=ingredient2, quantity=10, units="G",
        )
        url = reverse("recipes")

        # Act
        response = self.client.get(url)

        # Assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["name"], "Pasta")
        self.assertEqual(response.data[0]["instructions"], "Make the pasta")
        self.assertEqual(response.data[0]["ingredients"][0]["name"], "tomato")
        self.assertEqual(response.data[0]["ingredients"][0]["quantity"], 300)
        self.assertEqual(response.data[0]["ingredients"][0]["units"], "G")
        self.assertEqual(response.data[0]["ingredients"][1]["name"], "basil")
        self.assertEqual(response.data[0]["ingredients"][1]["quantity"], 10)
        self.assertEqual(response.data[0]["ingredients"][1]["units"], "G")

    def test_POST_ValidData_CreateRecipe(self):
        # Arrange
        i = Ingredient.objects.create(name="cheese")
        recipe = {
            "name": "Pasta",
            "instructions": "Make pasta",
            "ingredients": [
                {"ingredient": i.id, "quantity": 5, "units": "G"},
            ],
        }
        url = reverse("recipes")

        # Act
        response = self.client.post(url, recipe)

        # Assert
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        recipe_object = Recipe.objects.filter(
            name="Pasta", instructions="Make pasta"
        ).first()
        self.assertIsNotNone(recipe_object)
        recipe_ingredients = recipe_object.recipeingredient_set.all()
        self.assertEqual(1, recipe_ingredients.count())
        self.assertEqual(i.id, recipe_ingredients[0].ingredient.id)

    def test_POST_InvalidData_RecipeNotCreated(self):
        # Arrange
        i = Ingredient.objects.create(name="cheese")
        recipe = {
            "name": "",
            "instructions": "Make pasta",
            "ingredients": [
                {"ingredient": i.id, "quantity": 5, "units": "G"},
            ],
        }
        url = reverse("recipes")

        # Act
        response = self.client.post(url, recipe)

        # Assert
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        recipe_objects = Recipe.objects.filter(
            name="", instructions="Make pasta"
        )
        self.assertEqual(0, recipe_objects.count())
