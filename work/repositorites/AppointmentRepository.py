from abc import ABCMeta, abstractmethod
from typing import List
from work.models import Appointments
from work.dto.AppointmentDto import AppointmentDetailsDto, CreateAppointmentDto, ListAppointmentDto, \
    SearchAppointmentDto
from datetime import date


class AppointmentRepository(metaclass=ABCMeta):
    @abstractmethod
    def create_appointment(self, model: CreateAppointmentDto):
        """Create Appointment Object"""
        raise NotImplementedError

    def appointment_details(self, id: int) -> AppointmentDetailsDto:
        """Get Appointment Object"""
        raise NotImplementedError

    def list_appointment(self) -> List[ListAppointmentDto]:
        """List Appointment Objects"""
        raise NotImplementedError

    def search_appointment(self, appointment_reference: str, appointment_date: date):
        """Returns Appointment Object"""
        raise NotImplementedError


class DjangoORMAppointmentRepository(AppointmentRepository):
    def create_appointment(self, model: CreateAppointmentDto):
        appointment = Appointments()
        appointment.doctor_id = model.doctor_id
        appointment.appointment_reference = model.appointment_reference
        appointment.appointment_datetime = model.appointment_datetime
        appointment.patient_id = model.patient_id

    def list_appointment(self) -> List[ListAppointmentDto]:
        appointments = list(Appointments.objects.values('id',
                                                        'patient__user__last_name',
                                                        'patient__user__first_name',
                                                        'doctor__staff__user__first_name',
                                                        'doctor__staff__user__last_name',
                                                        'appointment_reference',
                                                        'appointment_datetime'))
        result: List[ListAppointmentDto] = []
        for appointment in appointments:
            item = ListAppointmentDto()
            item.id = appointment['id']
            item.patient_first_name = appointment['patient__user__last_name']
            item.patient_last_name = appointment['patient__user__first_name']
            item.doctor_first_name = appointment['doctor__staff__user__first_name']
            item.patient_last_name = appointment['doctor__staff__user__first_name']
            item.appointment_reference = appointment['appointment_reference']
            item.appointment_datetime = appointment['appointment_datetime']
            result.append(item)
        return result

    def appointment_details(self, id: int) -> AppointmentDetailsDto:
        try:
            appointment = Appointments.objects.get(id=id)
            result = AppointmentDetailsDto()
            result.id = appointment.id
            result.doctor_last_name = appointment.doctor.staff.user.last_name
            result.doctor_first_name = appointment.doctor.staff.user.first_name
            result.patient_last_name = appointment.patient.user.last_name
            result.patient_first_name = appointment.patient.user.first_name
            result.appointment_datetime = appointment.appointment_datetime
            result.appointment_reference = appointment.appointment_reference
            return result
        except Appointments.DoesNotExist as e:
            message = 'Appointment does not exit'
            print(message)
            raise e

    def search_appointment(self, appointment_reference: str, appointment_date: date):
        try:
            appointment = Appointments.objects
            if appointment is not None:
                appointment = appointment.filter(appointment_reference=appointment_reference)
            if appointment is not None:
                appointment = appointment.filter(appointment_date=appointment_date)

            result = SearchAppointmentDto()
            result.id = appointment.id
            result.doctor_last_name = appointment.doctor.staff.user.last_name
            result.doctor_first_name = appointment.doctor.staff.user.first_name
            result.patient_last_name = appointment.patient.user.last_name
            result.patient_last_name = appointment.patient.user.last_name
            result.appointment_reference = appointment.appointment_reference
            result.appointment_date = appointment.appointment_date
            return result
        except Appointments.DoesNotExist as e:
            message = 'Appointment does not exit'
            print(message)
            raise e