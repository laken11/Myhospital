from abc import ABCMeta, abstractmethod
from typing import List

from work.dto.AppointmentDto import *
from work.repositorites.AppointmentRepository import AppointmentRepository


class AppointManagementService(metaclass=ABCMeta):
    @abstractmethod
    def create_appointment(self, model: CreateAppointmentDto):
        """Create Appointment Object"""
        raise NotImplementedError

    @abstractmethod
    def appointment_details(self, id: int) -> AppointmentDetailsDto:
        """Get Appointment Object"""
        raise NotImplementedError

    @abstractmethod
    def list_appointment(self) -> List[ListAppointmentDto]:
        """List Appointment Objects"""
        raise NotImplementedError

    @abstractmethod
    def search_appointment(self, appointment_reference: str, appointment_date: date):
        """Returns Appointment Object"""
        raise NotImplementedError


class DefaultAppointmentManagementService(AppointManagementService):
    repository: AppointmentRepository

    def __init__(self, repository: AppointmentRepository):
        self.repository = repository

    def create_appointment(self, model: CreateAppointmentDto):
        return self.repository.create_appointment(model)

    def search_appointment(self, appointment_reference: str, appointment_date: date):
        return self.repository.search_appointment(appointment_date=appointment_date,
                                                  appointment_reference=appointment_reference)

    def appointment_details(self, id: int) -> AppointmentDetailsDto:
        return self.repository.appointment_details(id=id)

    def list_appointment(self) -> List[ListAppointmentDto]:
        return self.repository.list_appointment()

