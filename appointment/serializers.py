from rest_framework import serializers

from appointment.models import Appointment
from utils.validators.appointment_validators import (
    date_validator_by_schedule_days,
    trainer_schedule_conflict_validator,
    future_date_validator,
    client_appointment_conflicts_validator,
    user_role_validator, trainer_availability_validator
)
from utils.validators.schedule_validators import start_end_time_order_conflict


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'


class AppointmentCreateSerializer(serializers.ModelSerializer):
    def validate(self, attrs):
        if future_date_validator(attrs):
            return serializers.ValidationError('Cannot create appointment withing past dates')

        if not user_role_validator(attrs):
            raise serializers.ValidationError('Client or Trainer user roles is not valid ')

        if client_appointment_conflicts_validator(attrs):
            raise serializers.ValidationError('User have already appointment on this time')

        if date_validator_by_schedule_days(attrs):
            raise serializers.ValidationError('Trainer is not available for this date')

        if trainer_availability_validator(attrs):
            raise serializers.ValidationError('Trainer has appointment on this time')

        if trainer_schedule_conflict_validator(attrs):
            raise serializers.ValidationError('Trainer is not available for this time')

        if start_end_time_order_conflict(attrs):
            raise serializers.ValidationError("Start and end time order conflict")

        return attrs

    class Meta:
        model = Appointment
        fields = [
            'id',
            'client',
            'trainer',
            'gym',
            'date',
            'start_time',
            'end_time',
        ]
