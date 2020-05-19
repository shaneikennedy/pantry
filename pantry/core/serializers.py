from .models import Ingredient, Recipe, RecipeIngredient

from rest_framework import serializers


class IngredientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingredient
        fields = ('id', 'name')


class RecipeIngredientSerializer(serializers.ModelSerializer):
    name = serializers.StringRelatedField(source='ingredient')

    class Meta:
        model = RecipeIngredient
        fields = (
            'name',
            'quantity',
            'units',
        )


class RecipeSerializer(serializers.ModelSerializer):
    ingredients = RecipeIngredientSerializer(
        source='recipeingredient_set',
        many=True,
    )

    class Meta:
        model = Recipe
        fields = (
            'name',
            'instructions',
            'ingredients',
        )
