from django.db.utils import IntegrityError
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import viewsets, status

from trainer.models import Trainer
from trainer.serializers import TrainerDetailSerializer, TrainerCreateSerializer, TrainerUpdateSerializer


class TrainerViewSet(viewsets.ModelViewSet):
    queryset = Trainer.objects.filter(base_profile__archived=False)
    http_method_names = ['get', 'post', 'patch']
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['specialization', 'gyms', 'base_profile__last_name']

    def get_serializer_class(self):
        if hasattr(self.request, 'method'):
            if self.request.method == 'GET':
                return TrainerDetailSerializer
            elif self.request.method == 'POST':
                return TrainerCreateSerializer
            elif self.request.method == 'PATCH':
                return TrainerUpdateSerializer
        else:
            return TrainerDetailSerializer

    def create(self, request, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            data = serializer.data
        except IntegrityError as e:
            data = {"error": f"{e}"}

        return Response(data=data, status=status.HTTP_201_CREATED)
