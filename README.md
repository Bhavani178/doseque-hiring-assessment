# DoseQue Appointment API

A REST API built with Django and Django REST Framework to create, list, and cancel appointments.

## Features

- Create appointments with patient name, email, and appointment time.
- List appointments, newest first.
- Cancel appointments without deleting their records.
- Validate patient names, email addresses, and future appointment times.
- Return appropriate HTTP status codes for successful and invalid requests.
- Automated tests for appointment creation, validation, and cancellation.

## Requirements

- Python 3.13+
- pip

## Setup

```bash
python -m venv .venv
```

Activate the virtual environment on Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Apply database migrations:

```bash
python manage.py migrate
```

Start the development server:

```bash
python manage.py runserver
```

## API Endpoints

### Create an appointment

`POST /api/appointments/`

Example JSON:

```json
{
  "patient_name": "Alex Kumar",
  "email": "alex@example.com",
  "appointment_time": "2027-01-15T10:00:00+05:30"
}
```

Returns `201 Created` on success and `400 Bad Request` for invalid input.

### List appointments

`GET /api/appointments/`

Returns appointments ordered by creation time, newest first.

### Cancel an appointment

`DELETE /api/appointments/<id>/`

Marks an appointment as cancelled instead of deleting it. Returns `404 Not Found` if the appointment does not exist and `409 Conflict` if it is already cancelled.

## Run Tests

```bash
python manage.py test appointments
```

The test suite covers successful creation, invalid appointment input, and cancellation.
