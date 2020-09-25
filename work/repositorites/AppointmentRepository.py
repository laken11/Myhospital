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

    def search_appointment(self, appointment_number: str):
        """Returns Appointment Object"""
        raise NotImplementedError


class DjangoORMAppointmentRepository(AppointmentRepository):
    def create_appointment(self, model: CreateAppointmentDto):
        appointment = Appointments()
        appointment.doctor_id = model.doctor_id
        appointment.appointment_reference = model.appointment_reference
        appointment.appointment_datetime = model.appointment_datetime
        appointment.patient_id = model.patient_id
        appointment.appointment_number = model.appointment_number
        appointment.save()

    def list_appointment(self) -> List[ListAppointmentDto]:
        appointments = list(Appointments.objects.values('id',
                                                        'patient__user__last_name',
                                                        'patient__user__first_name',
                                                        'doctor__staff__user__first_name',
                                                        'doctor__staff__user__last_name',
                                                        'appointment_number',
                                                        'appointment_datetime'))
        result: List[ListAppointmentDto] = []
        for appointment in appointments:
            item = ListAppointmentDto()
            item.id = appointment['id']
            item.patient_first_name = appointment['patient__user__last_name']
            item.patient_last_name = appointment['patient__user__first_name']
            item.doctor_first_name = appointment['doctor__staff__user__first_name']
            item.doctor_last_name = appointment['doctor__staff__user__last_name']
            item.appointment_number = appointment['appointment_number']
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

    def search_appointment(self, appointment_number: str):
        try:
            appointment = Appointments.objects.get(appointment_number=appointment_number)
            result = SearchAppointmentDto()
            result.id = appointment.id
            result.doctor_last_name = appointment.doctor.staff.user.last_name
            result.doctor_first_name = appointment.doctor.staff.user.first_name
            result.patient_last_name = appointment.patient.user.last_name
            result.patient_first_name = appointment.patient.user.first_name
            result.appointment_reference = appointment.appointment_reference
            result.appointment_datetime = appointment.appointment_datetime
            result.appointment_number = appointment.appointment_number
            return result
        except Appointments.DoesNotExist as e:
            message = 'Appointment does not exit'
            print(message)
            raise e
