from rest_framework import serializers

from users.models import BaseProfile


class BaseProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseProfile
        fields = [
            'id',
            'role',
            'username',
            'first_name',
            'last_name',
            'email',
            'birth_date',
            'gender',
            'archived',
        ]


class BaseProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseProfile
        fields = [
            'id',
            'role',
            'first_name',
            'last_name',
            'email',
            'birth_date',
            'gender',
        ]
