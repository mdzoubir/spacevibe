from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

from users.serializers import UserSerializer

# Dynamically get the user model
User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing users. Requires authentication for all actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class EmailTokenObtainPairView(TokenObtainPairView):
    username_field = 'email'

class RegisterView(APIView):
    """
    API endpoint for user registration. Open to anyone.
    """
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(
            {
                "detail": "Invalid data",
                "errors": serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST
        )