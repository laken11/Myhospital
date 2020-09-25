from abc import ABCMeta, abstractmethod
from typing import List

from work.dto.PatientDto import *
from work.repositorites.PatientRepository import PatientRepository
from work.dto.CommonDto import SelectOptionDto


class PatientManagementService(metaclass=ABCMeta):
    @abstractmethod
    def create_patient(self, model: CreatePatientDto):
        """Create patient object"""
        raise NotImplementedError

    @abstractmethod
    def edit_patient(self, id: int, model: EditPatientDto):
        """Edit patient object"""
        raise NotImplementedError

    @abstractmethod
    def list_patient(self) -> List[ListPatientDto]:
        """List patients object"""
        raise NotImplementedError

    @abstractmethod
    def patient_details(self, id: int) -> PatientDetailsDto:
        """Return patient details"""
        raise NotImplementedError

    @abstractmethod
    def search_patient(self, patient_number: str) -> SearchPatientDto:
        """Return an patient object"""
        raise NotImplementedError

    @abstractmethod
    def get_all_for_select_list(self) -> List[SelectOptionDto]:
        """Create a staff object"""
        raise NotImplementedError


class DefaultPatientManagementService(PatientManagementService):
    repository: PatientRepository

    def __init__(self, repository: PatientRepository):
        self.repository = repository

    def create_patient(self, model: CreatePatientDto):
        return self.repository.create_patient(model)

    def edit_patient(self, id: int, model: EditPatientDto):
        return self.repository.edit_patient(id, model)

    def search_patient(self, patient_number: str) -> SearchPatientDto:
        return self.repository.search_patient(patient_number)

    def patient_details(self, id: int) -> PatientDetailsDto:
        return self.repository.patient_details(id=id)

    def list_patient(self) -> List[ListPatientDto]:
        return self.repository.list_patient()

    def get_all_for_select_list(self) -> List[SelectOptionDto]:
        return self.repository.get_all_for_select_list()
