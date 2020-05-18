from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from .models import Ingredient


class IngredientsAPITests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.url = reverse('ingredients')

    def test_GET__ReturnAllIngredients(self):
        # Arrange
        expected_num_ingredients = Ingredient.objects.count()

        # Act
        response = self.client.get(self.url)

        # Assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), expected_num_ingredients)

    def test_GET_SearchByName_ReturFiiteredResults(self):
        expected_num_ingredients = Ingredient.objects.filter(
            name="artichoke"
        ).count()
        params = {
            "item": "artichoke",
        }

        response = self.client.get(self.url, params)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), expected_num_ingredients)

    def test_GET_EmptySearch_ShouldReturnAllIngredients(self):
        expected_num_ingredients = Ingredient.objects.count()
        params = {
            "item": "",
        }

        response = self.client.get(self.url, params)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), expected_num_ingredients)
