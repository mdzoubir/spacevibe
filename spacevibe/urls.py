"""
URL configuration for spacevibe project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from users.views import *
from rooms.views import *
from furniture.views import *

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'houses', HouseViewSet, basename='house')
router.register(r'rooms', RoomViewSet, basename='room')
router.register(r'walls', WallViewSet, basename='wall')
router.register(r'furniture-categories', FurnitureCategoryViewSet, basename='furniture-category')
router.register(r'furniture', FurnitureViewSet, basename='furniture')
router.register(r'furniture-placements', FurniturePlacementViewSet, basename='furniture-placement')

# Swagger configuration for API documentation
schema_view = get_schema_view(
    openapi.Info(
        title="House Design API",
        default_version='v1',
        description="API for managing houses, rooms, walls, and furniture",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/auth/', include('users.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]



