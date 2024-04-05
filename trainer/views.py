from rest_framework.response import Response
from rest_framework import viewsets, status

from trainer.models import Trainer
from trainer.serializers import TrainerDetailSerializer, TrainerCreateSerializer


class TrainerViewSet(viewsets.ModelViewSet):
    queryset = Trainer.objects.all()
    serializer_class = TrainerDetailSerializer
    http_method_names = ['get', 'post', 'patch']

    def perform_create(self, serializer):
        return serializer.save()

    def create(self, request, *args, **kwargs):
        serializer = TrainerCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

