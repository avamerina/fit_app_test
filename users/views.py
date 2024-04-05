from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from users.models import BaseProfile
from users.serializers import BaseProfileSerializer


class BaseProfileViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = BaseProfileSerializer
    http_method_names = ['get', 'patch']
    queryset = BaseProfile.objects.all()
