from .serializers import UserSerializer
from rest_framework.views import APIView, Response
from rest_framework import status


class RegisterAPIView(APIView):
    def post(self, request):
        user_data = request.data
        serializer = UserSerializer(data=user_data)

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(
            data=serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )


register_api = RegisterAPIView.as_view()
