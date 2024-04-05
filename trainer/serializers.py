from rest_framework import serializers

from trainer.models import Trainer
from users.models import BaseProfile


class TrainerDetailSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    birthday = serializers.SerializerMethodField()
    gender = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()

    def get_name(self, obj):
        return obj.base_profile.get_full_name()

    def get_birthday(self, obj):
        return obj.base_profile.birth_date

    def get_gender(self, obj):
        return obj.base_profile.gender

    def get_email(self, obj):
        return obj.base_profile.email

    class Meta:
        model = Trainer
        fields = [
            'base_profile',
            'name',
            'birthday',
            'gender',
            'email',
            'specialization',
            'gyms'
        ]


class TrainerCreateSerializer(serializers.ModelSerializer):
    base_profile = serializers.PrimaryKeyRelatedField(
        queryset=BaseProfile.objects.all(),
        required=True
    )

    def validate(self, attrs):
        base_profile = attrs.get('base_profile')
        if base_profile and base_profile.role == 'trainer':
            return attrs
        else:
            raise serializers.ValidationError('Not a valid profile')

    class Meta:
        model = Trainer
        fields = '__all__'


