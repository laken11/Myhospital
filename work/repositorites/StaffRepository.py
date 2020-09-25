from abc import ABCMeta, abstractmethod
from typing import List
from work.models import Staff
from work.dto.StaffDto import EditStaffDto, ListStaffDto, CreateStaffDto, SearchStaffDto, StaffDetailsDto
from work.dto.CommonDto import SelectOptionDto
from django.contrib.auth.models import User, Group


class StaffRepository(metaclass=ABCMeta):
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
        """List satff objects"""
        raise NotImplementedError

    @abstractmethod
    def staff_details(self,id:int) -> StaffDetailsDto:
        """Get staff details"""
        raise NotImplementedError

    @abstractmethod
    def search_staff(self, staff_number: str) -> SearchStaffDto :
        """Return staff object"""
        raise NotImplementedError

    @abstractmethod
    def get_all_for_select_list(self) -> List[SelectOptionDto]:
        """Create a staff object"""
        raise NotImplementedError


class DjangoOMStaffRepository(StaffRepository):
    def create_staff(self, model: CreateStaffDto):
        staff = Staff()
        staff.phone = model.phone
        staff.staff_id = model.staff_id
        staff.date_of_birth = model.date_of_birth
        staff.address = model.address
        staff.level = model.level
        staff.year_of_employment = model.year_of_employment
        staff.job_title = model.job_title
        staff.staff_number = model.staff_number
        user = User.objects.create_user(model.username, model.email, model.password)
        user.last_name = model.last_name
        user.first_name = model.first_name
        user.save()
        staff.user = user
        staff.save()

    def edit_staff(self, model: EditStaffDto, id):
        try:
            staff = Staff.objects.get(id= id)
            staff.phone = model.phone
            staff.id = model.id
            staff.level = model.level
            staff.year_of_employment = model.year_of_employment
            staff.job_title = model.job_title
            staff.address = model.address
            staff.date_of_birth = model.date_of_birth
            staff.save()
        except Staff.DoesNotExist as e:
            message = 'Staff dose not exit'
            print(message)
            raise e

    def list_staff(self) -> List[ListStaffDto]:
        staffs = list(Staff.objects.values('id',
                                           'user__first_name',
                                           'user__last_name',
                                           'user__email',
                                           'job_title',
                                           'year_of_employment',
                                           'address',
                                           'level',
                                           'phone',
                                           'staff_id',
                                           'date_of_birth',
                                           'staff_number'))
        result: List[ListStaffDto] = []
        for staff in staffs:
            item = ListStaffDto()
            item.id = staff['id']
            item.user_first_name = staff['user__first_name']
            item.user_last_name = staff['user__last_name']
            item.user_email = staff['user__email']
            item.job_title = staff['job_title']
            item.year_of_employment = staff['year_of_employment']
            item.address = staff['address']
            item.level = staff['level']
            item.phone = staff['phone']
            item.staff_id = staff['staff_id']
            item.date_of_birth = staff['date_of_birth']
            item.staff_number = staff['staff_number']
            result.append(item)
        return result

    def search_staff(self, staff_number: str) -> SearchStaffDto:
        try:
            staff = Staff.objects.get(staff_number=staff_number)
            result = SearchStaffDto()
            result.staff_id = staff.staff_id
            result.date_of_birth = staff.date_of_birth
            result.phone = staff.phone
            result.address = staff.address
            result.level = staff.level
            result.year_of_employment = staff.year_of_employment
            result.job_title = staff.job_title
            result.user_first_name = staff.user.first_name
            result.user_last_name = staff.user.last_name
            result.user_email = staff.user.email
            result.id = staff.id
            result.staff_number = staff.staff_number
            return result
        except Staff.DoesNotExist as e:
            message = 'Staff dose not exit'
            print(message)
            raise e

    def staff_details(self,id:int) -> StaffDetailsDto:
        try:
            staff = Staff.objects.get(id=id)
            result = StaffDetailsDto()
            result.id = staff.id
            result.level = staff.level
            result.year_of_employment = staff.year_of_employment
            result.job_title = staff.job_title
            result.user_first_name = staff.user.first_name
            result.user_last_name = staff.user.last_name
            result.user_email = staff.user.email
            result.date_of_birth = staff.date_of_birth
            result.address = staff.address
            result.phone = staff.phone
            result.staff_id = staff.staff_id
            result.staff_number = staff.staff_number
            return result
        except Staff.DoesNotExist as e:
            message = 'Staff dose not exit'
            print(message)
            raise e

    def get_all_for_select_list(self) -> List[SelectOptionDto]:
        staff = Staff.objects.values("id", "staff_number")
        return [SelectOptionDto(s["id"], s["staff_number"]) for s in staff]
