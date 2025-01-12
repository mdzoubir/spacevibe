from django.contrib.auth import get_user_model
from django.db import transaction
from rest_framework import viewsets
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

from users.serializers import UserSerializer

# Dynamically get the user model
User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing users
    """
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'put', 'patch', 'delete']

    def get_queryset(self):
        # Only allow users to access their own data
        return User.objects.filter(id=self.request.user.id)

    def get_object(self):
        # Ensure the requested object belongs to the current user
        obj = super().get_object()
        if obj.id != self.request.user.id:
            raise PermissionDenied("You don't have permission to access this user's data")
        return obj

    @transaction.atomic
    def update(self, request, *args, **kwargs):
        # Ensure the user is trying to update their own profile
        if str(self.request.user.id) != kwargs.get('pk'):
            raise PermissionDenied("You can only update your own profile")
        return super().update(request, *args, **kwargs)

    @transaction.atomic
    def destroy(self, request, *args, **kwargs):
        # Ensure the user is trying to delete their own profile
        if str(self.request.user.id) != kwargs.get('pk'):
            raise PermissionDenied("You can only delete your own profile")
        return super().destroy(request, *args, **kwargs)


class EmailTokenObtainPairView(TokenObtainPairView):
    username_field = 'email'

class RegisterView(APIView):
    """
    API endpoint for user registration. Open to anyone.
    """
    permission_classes = [AllowAny]

    @transaction.atomic
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response(
                    {
                        "message": "User registered successfully",
                        "user": serializer.data
                    },
                    status=status.HTTP_201_CREATED
                )
            except Exception as e:
                return Response(
                    {
                        "detail": "Registration failed",
                        "error": str(e)
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
        return Response(
            {
                "detail": "Invalid data",
                "errors": serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST
        )