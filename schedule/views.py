from rest_framework import viewsets, status
from rest_framework.response import Response

from schedule.models import ScheduleUnit
from schedule.serializers import ScheduleUnitSerializer, ScheduleUnitCreateSerializer


class ScheduleUnitViewSet(viewsets.ModelViewSet):
    queryset = ScheduleUnit.objects.all()
    serializer_class = ScheduleUnitSerializer
    http_method_names = ['get', 'post', 'patch']

    def perform_create(self, serializer):
        return serializer.save()

    def create(self, request, *args, **kwargs):
        serializer = ScheduleUnitCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
