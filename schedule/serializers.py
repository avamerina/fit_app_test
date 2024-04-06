from rest_framework import serializers

from schedule.models import ScheduleUnit
from utils.validators.schedule_validators import conflicting_trainer_schedule_units, conflicting_gym_schedule_units


class ScheduleUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScheduleUnit
        fields = '__all__'


class ScheduleUnitCreateSerializer(serializers.ModelSerializer):
    def validate(self, attrs):
        if conflicting_gym_schedule_units(attrs):
            raise serializers.ValidationError("Пересечение расписаний тренеров в одном зале")

        if conflicting_trainer_schedule_units(attrs):
            raise serializers.ValidationError("Пересечение в расписании тренера")

        return attrs

    class Meta:
        model = ScheduleUnit
        fields = [
            'trainer',
            'gym',
            'week_day',
            'start_time',
            'end_time'
        ]
