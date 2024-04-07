from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from users.models import BaseProfile
from users.serializers import BaseProfileSerializer, BaseProfileUpdateSerializer


class BaseProfileViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = BaseProfileSerializer
    http_method_names = ['get', 'patch', 'delete']
    queryset = BaseProfile.objects.filter(archived=False)
    filter_backends = (DjangoFilterBackend, )
    filterset_fields = ('role', )

    def update(self, request, *args, **kwargs) -> Response:
        instance = self.get_object()
        serializer = BaseProfileUpdateSerializer(
            instance,
            data=request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs) -> Response:
        instance = self.get_object()
        instance.archived = True
        instance.save(update_fields=['archived'])
        return Response(data={"status": "success"}, status=status.HTTP_200_OK)

