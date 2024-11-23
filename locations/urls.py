from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LocationDataViewSet

router = DefaultRouter()
router.register(r'locations', LocationDataViewSet)

urlpatterns = [
    path('', include(router.urls)),
] 