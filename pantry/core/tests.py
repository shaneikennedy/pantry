from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from .models import Ingredient


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
        [Ingredient.objects.create(name=name) for name in cls.ingredient_names]

        cls.url = reverse("ingredients")

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
