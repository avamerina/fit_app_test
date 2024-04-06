from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from schedule.models import ScheduleUnit
from schedule.serializers import ScheduleUnitSerializer, ScheduleUnitCreateSerializer
from schedule import services


class ScheduleUnitViewSet(viewsets.ModelViewSet):
    queryset = ScheduleUnit.objects.all()
    serializer_class = ScheduleUnitSerializer
    http_method_names = ['get', 'post', 'patch']
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('trainer', 'gym', 'week_day', 'start_time', 'end_time')

    def create(self, request, *args, **kwargs):
        serializer = ScheduleUnitCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(methods=['get'], detail=False)
    def get_trainer_schedule(self, request, *args, **kwargs):
        trainer = request.GET['trainer']
        self.queryset = services.get_all_schedule_units_by_trainer(trainer)
        serializer = ScheduleUnitSerializer(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(methods=['get'], detail=False)
    def get_gym_schedule(self, request, *args, **kwargs):
        gym = request.GET['gym']
        self.queryset = services.get_schedule_units_by_gym(gym)
        serializer = ScheduleUnitSerializer(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(methods=['get'], detail=False)
    def get_training_class_schedule(self, request, *args, **kwargs):
        spec = request.GET['specialization']
        self.queryset = services.get_schedule_units_by_trainer_specification(spec)
        serializer = ScheduleUnitSerializer(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

