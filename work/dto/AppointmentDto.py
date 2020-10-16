from datetime import date


class CreateAppointmentDto:
    appointment_datetime: date
    appointment_reference: str
    patient_id: int
    doctor_id: int
    appointment_number: str


class ListAppointmentDto:
    id: int
    appointment_datetime: date
    appointment_reference: str
    patient_last_name: str
    patient_first_name: str
    doctor_last_name: str
    doctor_first_name: str
    appointment_number: str


class SearchAppointmentDto:
    id: int
    appointment_datetime: date
    appointment_reference: str
    patient_last_name: str
    patient_first_name: str
    doctor_last_name: str
    doctor_first_name: str
    appointment_number: str


class AppointmentDetailsDto:
    id: int
    appointment_datetime: date
    appointment_reference: str
    patient_last_name: str
    patient_first_name: str
    doctor_last_name: str
    doctor_first_name: str
    appointment_number: str


class GetAppointmentForDoctor:
    id: int
    appointment_number: str
    patient_last_name: str
    patient_first_name: str



