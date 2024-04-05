from rest_framework import serializers

from users.models import BaseProfile


class BaseProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseProfile
        fields = '__all__'
