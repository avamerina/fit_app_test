from rest_framework import viewsets

from gym.models import Gym
from gym.serializers import GymSerializer


class GymViewSet(viewsets.ModelViewSet):
    queryset = Gym.objects.all()
    serializer_class = GymSerializer
    http_method_names = ['get', 'post', 'patch']
