from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from pantry.core.models import Ingredient, Recipe, RecipeIngredient


class RegisterAPITests(APITestCase):
    def test_POST_ValidData_UserCreated(self):

        # Arrange
        user_data = {
            "username": "melissa",
            "email": "melissa@mail.com",
            "password": "123",
        }
        url = reverse("register")

        # Act
        response = self.client.post(url, user_data)

        # Assert
        user = User.objects.get(username="melissa")
        self.assertEqual("melissa@mail.com", user.email)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_POST_ValidData_UserDataReturned(self):

        # Arrange
        user_data = {
            "username": "melissa",
            "email": "melissa@mail.com",
            "password": "123",
        }
        url = reverse("register")

        # Act
        response = self.client.post(url, user_data)

        # Assert
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["email"], "melissa@mail.com")
        self.assertEqual(response.data["username"], "melissa")

    def test_POST_InvalidData_UserFailedToCreate(self):

        # Arrange
        user_data = {
            "username": "melissa",
            "email": "melissamail.com",
            "password": "123",
        }
        url = reverse("register")

        # Act
        response = self.client.post(url, user_data)

        # Assert
        with self.assertRaises(User.DoesNotExist):
            User.objects.get(username="melissa")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UserAPITests(APITestCase):
    def test_GET_IsAuthenticated_Return200(self):

        # Arrange
        url = reverse("user")
        user = User.objects.create_user(
            email="test@123.com", username="test123", password="123456",
        )
        self.client.force_authenticate(user=user)

        # Act
        response = self.client.get(url)

        # Assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_GET_NotAuthenicated_Return401(self):

        # Arrange
        url = reverse("user")

        # Act
        response = self.client.get(url)

        # Assert
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_GET__ReturnUserInfo(self):

        # Arrange
        url = reverse("user")
        user = User.objects.create_user(
            email="test@123.com", username="test123", password="123456",
        )
        recipe_name = "Pasta"
        recipe_instructions = "Make the pasta"
        ingredient1 = Ingredient.objects.create(name="tomato")
        ingredient2 = Ingredient.objects.create(name="basil")
        recipe = Recipe.objects.create(
            name=recipe_name, instructions=recipe_instructions, author=user
        )
        RecipeIngredient.objects.create(
            recipe=recipe, ingredient=ingredient1, quantity=300, units="G",
        )
        RecipeIngredient.objects.create(
            recipe=recipe, ingredient=ingredient2, quantity=10, units="G",
        )
        self.client.force_authenticate(user=user)

        # Act
        response = self.client.get(url)

        # Assert
        self.assertEqual(response.data["username"], "test123")
        self.assertEqual(response.data["email"], "test@123.com")
        self.assertIsNotNone(response.data["date_joined"])
        self.assertEqual(len(response.data["recipes"]), 1)
        self.assertEqual(response.data["recipes"][0]["name"], recipe_name)
        self.assertEqual(response.data["recipes"][0]["author"], user.id)
