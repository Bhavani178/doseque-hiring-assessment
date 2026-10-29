
from datetime import timedelta

from django.utils import timezone
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Appointment


class AppointmentAPITests(APITestCase):
    def setUp(self):
        self.url = "/api/appointments/"
        self.valid_data = {
            "patient_name": "Alex Kumar",
            "email": "alex@example.com",
            "appointment_time": (
                timezone.now() + timedelta(days=2)
            ).isoformat(),
        }

    def test_create_appointment(self):
        response = self.client.post(
            self.url, self.valid_data, format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Appointment.objects.count(), 1)
        self.assertEqual(response.data["status"], "scheduled")

    def test_reject_invalid_appointment(self):
        invalid_data = {
            **self.valid_data,
            "patient_name": "   ",
            "email": "not-an-email",
            "appointment_time": (
                timezone.now() - timedelta(days=1)
            ).isoformat(),
        }

        response = self.client.post(
            self.url, invalid_data, format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Appointment.objects.count(), 0)

    def test_cancel_appointment(self):
        appointment = Appointment.objects.create(
            patient_name="Alex Kumar",
            email="alex@example.com",
            appointment_time=timezone.now() + timedelta(days=2),
        )

        response = self.client.delete(
            f"{self.url}{appointment.id}/"
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        appointment.refresh_from_db()
        self.assertEqual(appointment.status, "cancelled")
