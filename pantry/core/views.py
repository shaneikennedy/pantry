from .serializers import IngredientSerializer, RecipeSerializer
from .models import Ingredient, Recipe
from rest_framework.views import APIView, Response
from rest_framework import status


class IngredientAPIView(APIView):
    def get(self, request):
        ingredients = Ingredient.objects.all()
        item = self.request.query_params.get("item", "")

        if item != "":
            ingredients = ingredients.filter(name=item)

        serializer = IngredientSerializer(ingredients, many=True)

        return Response(serializer.data)

    def post(self, request):
        ingredients_data = request.data
        serializer = IngredientSerializer(data=ingredients_data)

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(
            status=status.HTTP_400_BAD_REQUEST, data=serializer.errors
        )


ingredients_api = IngredientAPIView.as_view()


class RecipesAPIView(APIView):
    def get(self, request):
        recipes = Recipe.objects.prefetch_related("recipeingredient_set").all()
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data)

    def post(self, request):
        recipe = request.data
        serializer = RecipeSerializer(data=recipe)

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(
            data=serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )


recipes_api = RecipesAPIView.as_view()
