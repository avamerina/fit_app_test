from rest_framework import serializers

from schedule.models import ScheduleUnit
from utils.validators.schedule_validators import (
    conflicting_trainer_schedule_units,
    conflicting_gym_schedule_units,
    start_end_time_order_conflict
)


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

        if start_end_time_order_conflict(attrs):
            raise serializers.ValidationError("Start and end time order conflict")
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
