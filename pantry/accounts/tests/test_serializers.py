from django.test import TestCase
from ..serializers import UserSerializer
from django.contrib.auth.models import User


class UserSerializerTests(TestCase):

    def test_Create_ValidData_CreateUser(self):
        # Arrange
        data = {
            'username': 'teste1234',
            'email': 'test@test.com',
            'password': '123456',
        }
        serializer = UserSerializer(data=data)

        # Act
        serializer.is_valid()
        serializer.save()

        # Assert
        user = User.objects.get(username=data['username'])
        self.assertEqual(user.email, data['email'])
        self.assertEqual(user.username, data['username'])

    def test_Create_InvalidEmail_DoNotCreateUser(self):
        # Arrange
        data = {
            'username': 'teste1234',
            'email': 'testtest.com',
            'password': '123456',
        }
        serializer = UserSerializer(data=data)

        # Act
        serializer.is_valid()

        # Assert
        user = User.objects.filter(username=data['username']).first()
        self.assertIsNone(user)
        self.assertIsNotNone(serializer.errors['email'])
