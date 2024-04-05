from django.urls import path, include
from rest_framework import routers

from users.views import BaseProfileViewSet

router = routers.DefaultRouter()
router.register(r'base_profiles', BaseProfileViewSet, basename='base_profiles')

urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt'))
]

urlpatterns += router.urls
