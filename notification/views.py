from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from notification.models import Notification
from notification.serializers import NotificationSerializer


class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    http_method_names = ['get', 'post']
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ['receiver', 'notification_type']

