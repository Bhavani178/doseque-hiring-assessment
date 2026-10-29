
from django.urls import path

from . import views

urlpatterns = [
    path("appointments/", views.appointment_list_create, name="appointment-list-create"),
    path(
        "appointments/<int:appointment_id>/",
        views.appointment_cancel,
        name="appointment-cancel",
    ),
]
