from .models import Ingredient, Recipe, RecipeIngredient

from rest_framework import serializers


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ("id", "name")


class RecipeIngredientSerializer(serializers.ModelSerializer):
    name = serializers.StringRelatedField(source="ingredient", read_only=True)

    class Meta:
        model = RecipeIngredient
        fields = ("name", "quantity", "units", "ingredient")


class RecipeSerializer(serializers.ModelSerializer):
    ingredients = RecipeIngredientSerializer(
        source="recipeingredient_set", many=True, required=False
    )
    author_username = serializers.CharField(
        read_only=True, source='author.username'
    )

    class Meta:
        model = Recipe
        fields = (
            "name",
            "author",
            "author_username",
            "instructions",
            "ingredients",
            "id",
        )

    def create(self, validated_data):
        recipe_ingredients = []
        if "recipeingredient_set" in validated_data:
            recipe_ingredients = validated_data.pop("recipeingredient_set")

        recipe = Recipe.objects.create(**validated_data)
        for recipe_ingredient in recipe_ingredients:
            RecipeIngredient.objects.create(recipe=recipe, **recipe_ingredient)
        return recipe
