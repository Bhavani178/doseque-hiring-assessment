

from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Appointment
from .serializers import AppointmentSerializer


@api_view(["GET", "POST"])
def appointment_list_create(request):
    if request.method == "GET":
        appointments = Appointment.objects.all().order_by("-created_at")
        serializer = AppointmentSerializer(appointments, many=True)
        return Response(serializer.data)

    serializer = AppointmentSerializer(data=request.data)
    if serializer.is_valid():
        appointment = serializer.save()
        return Response(
            AppointmentSerializer(appointment).data,
            status=status.HTTP_201_CREATED,
        )

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def appointment_cancel(request, appointment_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id)

    if appointment.status == "cancelled":
        return Response(
            {"detail": "Appointment is already cancelled."},
            status=status.HTTP_409_CONFLICT,
        )

    appointment.status = "cancelled"
    appointment.save(update_fields=["status"])

    return Response(
        AppointmentSerializer(appointment).data,
        status=status.HTTP_200_OK,
    )

