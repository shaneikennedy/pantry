from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse


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
        self.assertEqual(response.data['email'], 'melissa@mail.com')
        self.assertEqual(response.data['username'], 'melissa')

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
