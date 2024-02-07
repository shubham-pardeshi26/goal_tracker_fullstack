# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserRegistrationViewSet

router = DefaultRouter()
router.register(r"register", UserRegistrationViewSet, basename="user-registration")

urlpatterns = [
    path("", include(router.urls)),
    # Add other URLs as needed
]
