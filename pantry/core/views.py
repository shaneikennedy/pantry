from .serializers import IngredientSerializer
from .models import Ingredient
from rest_framework.views import APIView, Response


class IngredientAPIView(APIView):

    def get(self, request):
        ingredients = Ingredient.objects.all()
        item = self.request.query_params.get("item", "")

        if item != "":
            ingredients = ingredients.filter(name=item)

        serializer = IngredientSerializer(ingredients, many=True)

        return Response(serializer.data)


ingredients_api = IngredientAPIView.as_view()
