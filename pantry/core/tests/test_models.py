from django.test import TestCase

from ..models import Ingredient


class IngredientTests(TestCase):
    def test_Save_UppercaseName_ConvertedToLowercase(self):
        # Arrange
        given_name = "LETTUCE"
        ing = Ingredient(name=given_name)

        # Act
        ing.save()

        # Assert
        self.assertEqual(ing.name, given_name.lower())
