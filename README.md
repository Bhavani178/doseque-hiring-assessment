# Appointment API

A simple appointment management API built using Django and Django REST Framework.

## What it does

- Creates an appointment with a patient name, email, and appointment time.
- Returns a list of appointments.
- Cancels an appointment by changing its status to `cancelled`.
- Checks that the patient name is not empty and the appointment time is in the future.

## Setup

Make sure Python is installed, then run these commands from the project directory.

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Set up the database:

```bash
python manage.py migrate
```

Start the server:

```bash
python manage.py runserver
```

The server runs at `http://127.0.0.1:8000/` by default.

## API endpoints

### Create an appointment

`POST /api/appointments/`

Example request:

```json
{
  "patient_name": "Alex Kumar",
  "email": "alex@example.com",
  "appointment_time": "2027-01-15T10:00:00+05:30"
}
```

### List appointments

`GET /api/appointments/`

Returns the appointments, with the newest ones first.

### Cancel an appointment

`DELETE /api/appointments/<id>/`

This changes the appointment status to `cancelled`. It does not delete the appointment from the database.

## Tests

Run the tests with:

```bash
python manage.py test appointments
```

The current test suite checks appointment creation, invalid input, and cancellation.
