from abc import ABCMeta, abstractmethod
from typing import List
from work.dto.CommonDto import SelectOptionDto
from work.dto.StaffDto import *
from work.repositorites.StaffRepository import StaffRepository


class StaffManagementService(metaclass=ABCMeta):
    @abstractmethod
    def create_staff(self, model: CreateStaffDto):
        """Create a staff object"""
        raise NotImplementedError

    @abstractmethod
    def edit_staff(self, model: EditStaffDto, id):
        """Edit a staff object"""
        raise NotImplementedError

    @abstractmethod
    def list_staff(self) -> List[ListStaffDto]:
        """List staff objects"""
        raise NotImplementedError

    @abstractmethod
    def staff_details(self, id: int) -> StaffDetailsDto:
        """Get staff details"""
        raise NotImplementedError

    @abstractmethod
    def search_staff(self, staff_number: str) -> SearchStaffDto:
        """Return staff object"""
        raise NotImplementedError

    @abstractmethod
    def get_all_for_select_list(self) -> List[SelectOptionDto]:
        """Create a staff object"""
        raise NotImplementedError


class DefaultStaffManagementService(StaffManagementService):
    repository: StaffRepository

    def __init__(self, repository: StaffRepository):
        self.repository = repository

    def create_staff(self, model: CreateStaffDto):
        return self.repository.create_staff(model)

    def edit_staff(self, model: EditStaffDto, id):
        return self.repository.edit_staff(model, id=id)

    def staff_details(self, id: int) -> StaffDetailsDto:
        return self.repository.staff_details(id=id)

    def search_staff(self, staff_number: str) -> SearchStaffDto:
        return self.repository.search_staff(staff_number)

    def list_staff(self) -> List[ListStaffDto]:
        return self.repository.list_staff()

    def get_all_for_select_list(self) -> List[SelectOptionDto]:
        return self.repository.get_all_for_select_list()
