

from django.utils import timezone
from rest_framework import serializers

from .models import Appointment


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = [
            "id",
            "patient_name",
            "email",
            "appointment_time",
            "status",
            "created_at",
        ]
        read_only_fields = ["id", "status", "created_at"]

    def validate_patient_name(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError(
                "Patient name cannot be empty."
            )
        return value

    def validate_appointment_time(self, value):
        if timezone.is_naive(value):
            raise serializers.ValidationError(
                "Appointment time must include a timezone."
            )
        if value <= timezone.now():
            raise serializers.ValidationError(
                "Appointment must be in the future."
            )
        return value

