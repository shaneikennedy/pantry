from django.contrib.auth.models import User
from rest_framework import serializers
from pantry.core.serializers import RecipeSerializer
from .models import RecipeLike


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email", "password", "date_joined")
        extra_kwargs = {
            "password": {"write_only": True},
            "date_joined": {"read_only": True},
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
        )
        return user


class RecipeLikesSerializer(serializers.ModelSerializer):

    class Meta:
        model = RecipeLike
        fields = ("id", "user", "recipe")


class UserProfileSerializer(serializers.ModelSerializer):
    recipes = RecipeSerializer(many=True, source="recipe_set.all")
    likes = RecipeLikesSerializer(many=True, source="recipelike_set.all")

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "date_joined",
            "recipes",
            "likes",
            "id",
        )
