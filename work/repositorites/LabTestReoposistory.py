from abc import ABCMeta, abstractmethod
from typing import List
from work.dto.LabTestDto import CreateLabTest, EditLabTestDto, LabTestDetailsDto, ListLabTest, SearchLabTestDto
from work.models import LabTest


class LabTestRepository(metaclass=ABCMeta):
    @abstractmethod
    def create_lab_test(self, model: CreateLabTest):
        """Create lab test object"""
        raise NotImplementedError

    @abstractmethod
    def edit_lab_test(self, id: int, model: EditLabTestDto):
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


class DjangoORMLabTestRepository(LabTestRepository):
    def create_lab_test(self, model: CreateLabTest):
        lab_test = LabTest()
        lab_test.medical_records_id = model.medical_records_id
        lab_test.staff_id = model.staff_id
        lab_test.test_result = model.test_result
        lab_test.date = model.date
        lab_test.test_name = model.test_name
        lab_test.test_id = model.test_id
        lab_test.save()

    def edit_lab_test(self, id:int, model: EditLabTestDto):
        try:
            lab_test = LabTest.objects.get(id=id)
            lab_test.test_name = model.test_name
            lab_test.id = model.id
            lab_test.test_result = model.test_result
            lab_test.date = model.date
            lab_test.test_id = model.test_id
        except LabTest.DoesNotExist as e:
            message = 'Result record dost not exit'
            print(message)
            raise e

    def list_lab_test(self) -> List[ListLabTest]:
        lab_tests = list(LabTest.objects.values('id',
                                                'test_id',
                                                'date',
                                                'test_result',
                                                'test_name',
                                                'staff__user__last_name',
                                                'medical_records__med_ref'
                                                'staff__user__first_name',
                                                'staff__user__last_name'))
        result: List[ListLabTest] = []
        for lab_test in lab_tests:
            item = ListLabTest()
            item.date = lab_test['date']
            item.test_id = lab_test['test_id']
            item.test_result = lab_test['test_result']
            item.medical_records_med_ref = lab_test['medical__records__med_ref']
            item.staff_last_name = lab_test['staff__user__last_name']
            item.staff_first_name = lab_test['staff__user__first_name']
            result.append(item)
        return result

    def lab_test_details(self, id:int) -> LabTestDetailsDto:
        try:
            lab_test = LabTest.objects.get(id=id)
            result = LabTestDetailsDto()
            result.test_name = lab_test.test_name
            result.test_id = lab_test.test_id
            result.test_result = lab_test.test_result
            result.medical_records_med_ref = lab_test.medical_records.med_ref
            result.staff_first_name = lab_test.staff.user.first_name
            result.staff_last_name = lab_test.staff.user.last_name
            result.date = lab_test.date
            return result
        except LabTest.DoesNotExist as e:
            message = 'Record dose not exit'
            print(message)
            raise e

    def search_lab_test(self, med_ref: str) -> SearchLabTestDto:
        try:
            lab_test = LabTest.objects.get(med_ref=med_ref)
            result = SearchLabTestDto()
            result.test_name = lab_test.test_name
            result.test_id = lab_test.test_id
            result.test_result = lab_test.test_result
            result.medical_records_med_ref = lab_test.medical_records.med_ref
            result.staff_first_name = lab_test.staff.user.first_name
            result.staff_last_name = lab_test.staff.user.last_name
            result.date = lab_test.date
            return result
        except LabTest.DoesNotExist as e:
            message = 'Record dose not exit'
            print(message)
            raise e

