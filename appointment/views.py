from rest_framework import viewsets, status
from rest_framework.response import Response

from appointment.models import Appointment
from appointment.serializers import AppointmentSerializer, AppointmentCreateSerializer
from notification.tasks import create_trainer_notification


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    http_method_names = ['get', 'post']

    def create(self, request, *args, **kwargs):
        serializer = AppointmentCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        create_trainer_notification(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
