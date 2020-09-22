from abc import ABCMeta, abstractmethod
from typing import List

from work.dto.LabTestDto import *
from work.repositorites.LabTestReoposistory import LabTestRepository


class LabTestManagementService(metaclass=ABCMeta):
    @abstractmethod
    def create_lab_test(self, model: CreateLabTest):
        """Create lab test object"""
        raise NotImplementedError

    @abstractmethod
    def edit_lab_test(self, id:int, model: EditLabTestDto):
        """Edit lab test object"""
        raise NotImplementedError

    @abstractmethod
    def lab_test_details(self, id:int) -> LabTestDetailsDto:
        """Get lab test object"""
        raise NotImplementedError

    @abstractmethod
    def list_lab_test(self) -> List[ListLabTest]:
        """List lab test items"""
        raise NotImplementedError

    @abstractmethod
    def search_lab_test(self, med_ref: str) -> SearchLabTestDto:
        """Returns lab test"""
        raise NotImplementedError


class DefaultLabTestManagementService(LabTestManagementService):
    repository: LabTestRepository

    def __init__(self, repository: LabTestRepository):
        self.repository = repository

    def create_lab_test(self, model: CreateLabTest):
        return self.repository.create_lab_test(model)

    def edit_lab_test(self, id: int, model: EditLabTestDto):
        return self.repository.edit_lab_test(id, model)

    def search_lab_test(self, med_ref: str) -> SearchLabTestDto:
        return self.repository.search_lab_test(med_ref=med_ref)

    def list_lab_test(self) -> List[ListLabTest]:
        return self.repository.list_lab_test()

    def lab_test_details(self, id:int) -> LabTestDetailsDto:
        return self.repository.lab_test_details(id=id)
