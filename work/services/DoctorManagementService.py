from abc import ABCMeta, abstractmethod
from typing import List

from work.dto.DoctorDto import *
from work.repositorites.DoctorRepository import DoctorRepository
from work.dto.CommonDto import SelectOptionDto


class DoctorManagementService(metaclass=ABCMeta):
    @abstractmethod
    def create_doctor(self, model: CreateDoctorDto):
        """Create Doctors object"""
        raise NotImplementedError

    @abstractmethod
    def edit_doctor(self,id: int, model: EditDoctorDto):
        """Edit doctors Object"""
        raise NotImplementedError

    @abstractmethod
    def doctor_details(self, id: int) -> DoctorDetailsDto:
        """Get doctors object details"""
        raise NotImplementedError

    @abstractmethod
    def search_doctor(self, specialization: str) -> SearchDoctorDto:
        """Returns Doctors Object"""
        raise NotImplementedError

    @abstractmethod
    def list_doctors(self) -> List[ListDoctorDto]:
        """List doctors object"""
        raise NotImplementedError

    @abstractmethod
    def get_all_for_select_list(self) -> List[SelectOptionDto]:
        """Create a doctor object"""
        raise NotImplementedError

    def get_all_for_select_list_doc(self) -> List[SelectOptionDto]:
        """ Create a doctor object"""
        raise NotImplementedError


class DefaultDoctorManagementService(DoctorManagementService):
    repository: DoctorRepository

    def __init__(self, repository: DoctorRepository):
        self.repository = repository

    def create_doctor(self, model: CreateDoctorDto):
        return self.repository.create_doctor(model)

    def edit_doctor(self,id: int,  model: EditDoctorDto):
        return self.repository.edit_doctor(id, model)

    def list_doctors(self) -> List[ListDoctorDto]:
        return self.repository.list_doctors()

    def search_doctor(self, specialization: str) -> SearchDoctorDto:
        return self.repository.search_doctor(specialization=specialization)

    def doctor_details(self, id: int) -> DoctorDetailsDto:
        return self.repository.doctor_details(id=id)

    def get_all_for_select_list(self) -> List[SelectOptionDto]:
        return self.repository.get_all_for_select_list()

    def get_all_for_select_list_doc(self) -> List[SelectOptionDto]:
        return self.repository.get_all_for_select_list_doc()
