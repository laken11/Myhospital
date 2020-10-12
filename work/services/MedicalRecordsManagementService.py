from abc import ABCMeta, abstractmethod
from typing import List

from work.dto.MedicalRecordsDto import *
from work.repositorites.MedicalRecordsRepository import MedicalRecordsRepository


class MedicalRecordsManagementService(metaclass=ABCMeta):
    @abstractmethod
    def create_medical_record(self, model: CreateMedicalRecordsDto):
        """Create a medical record object"""
        raise NotImplementedError

    @abstractmethod
    def edit_medical_record(self, id: int, model: EditMedicalRecordsDto):
        """Edit a medical record object"""
        raise NotImplementedError

    @abstractmethod
    def list_medical_record(self) -> List[ListMedicalRecordsDto]:
        """List medical record object"""
        raise NotImplementedError

    @abstractmethod
    def medical_record_details(self, id: int) -> MedicalRecordsDetailsDto:
        """Get a medical record object"""
        raise NotImplementedError

    @abstractmethod
    def search_medical_record(self, patient_number: str) -> SearchMedicalRecordsDto:
        """Return medical record object"""
        raise NotImplementedError


class DefaultMedicalRecordManagementService(MedicalRecordsManagementService):
    repository: MedicalRecordsRepository

    def __init__(self, repository: MedicalRecordsRepository):
        self.repository = repository

    def create_medical_record(self, model: CreateMedicalRecordsDto):
        return self.repository.create_medical_record(model)

    def edit_medical_record(self, id: int, model: EditMedicalRecordsDto):
        return self.repository.edit_medical_record(id, model)

    def list_medical_record(self) -> List[ListMedicalRecordsDto]:
        return self.repository.list_medical_record()

    def medical_record_details(self, id: int) -> MedicalRecordsDetailsDto:
        return self.repository.medical_record_details(id=id)

    def search_medical_record(self, patient_number: str) -> SearchMedicalRecordsDto:
        return self.repository.search_medical_record(patient_number=patient_number)
