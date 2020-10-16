from abc import ABCMeta, abstractmethod
from typing import List
from work.models import Doctor
from django.contrib.auth.models import Group
from work.dto.DoctorDto import CreateDoctorDto, DoctorDetailsDto, ListDoctorDto, EditDoctorDto, SearchDoctorDto, GetSchedule
from work.dto.CommonDto import SelectOptionDto
import datetime

class DoctorRepository(metaclass=ABCMeta):
    @abstractmethod
    def create_doctor(self, model: CreateDoctorDto):
        """Create Doctors object"""
        raise NotImplementedError

    @abstractmethod
    def edit_doctor(self, id: int, model: EditDoctorDto):
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
    @abstractmethod
    def get_all_for_select_list_doc(self) -> List[SelectOptionDto]:
        """ Create a doctor object"""
        raise NotImplementedError

    @abstractmethod
    def get_schedule(self, doctor_number: int) -> GetSchedule:
        """Return doctor object"""
        raise NotImplementedError

    @abstractmethod
    def get_doctor_number(self, doctor_id: int):
        """Return doctor number"""
        raise NotImplementedError


class DjangoORMDoctorRepository(DoctorRepository):
    def create_doctor(self, model: CreateDoctorDto):
        doctor = Doctor()
        doctor.staff_id = model.staff_id
        doctor.specialization = model.specialization
        doctor.appointment_schedules = model.appointment_schedule
        doctor.doctor_number = model.doctor_number

        user = doctor.staff.user
        doctors = Group.objects.get(name="doctor")
        user.groups.add(doctors)

        doctor.save()

    def edit_doctor(self, id: int, model: EditDoctorDto):
        doctor = Doctor.objects.get(id=id)
        doctor.specialization = model.specialization
        doctor.appointment_schedules = model.appointment_schedule

    def list_doctors(self) -> List[ListDoctorDto]:
        doctors = list(Doctor.objects.values('id',
                                             'staff__user__first_name',
                                             'staff__user__last_name',
                                             'appointment_schedules',
                                             'specialization',
                                             ))
        result: List[ListDoctorDto] = []
        for doctor in doctors:
            item = ListDoctorDto()
            item.id = doctor['id']
            item.staff_first_name = doctor["staff__user__first_name"]
            item.staff_last_name = doctor['staff__user__last_name']
            item.appointment_schedule = doctor['appointment_schedules']
            item.specialization = doctor['specialization']
            result.append(item)
        return result

    def doctor_details(self, id: int) -> DoctorDetailsDto:
        try:
            doctor = Doctor.objects.get(staff_id=id)
            result = DoctorDetailsDto()
            result.id = doctor.id
            result.staff_first_name = doctor.staff.user.first_name
            result.staff_last_name = doctor.staff.user.last_name
            result.appointment_schedule = doctor.appointment_schedules
            result.specialization = doctor.specialization
            result.doctor_number = doctor.doctor_number
            return result
        except Doctor.DoesNotExist as e:
            message = 'Doctor dose not exit'
            print(message)
            raise e

    def search_doctor(self, specialization: str) -> SearchDoctorDto:
        try:
            doctor = Doctor.objects.get(specialization=specialization)
            result = SearchDoctorDto()
            result.id = doctor.id
            result.staff_first_name = doctor.staff.user.first_name
            result.staff_last_name = doctor.staff.user.last_name
            result.specialization = doctor.specialization
            result.appointment_schedule = doctor.appointment_schedules
            result.doctor_number = doctor.doctor_number
            return result
        except Doctor.DoesNotExist as e:
            message = 'Doctor does not exit'
            print(message)
            raise e

    def get_all_for_select_list(self) -> List[SelectOptionDto]:
        doctor = Doctor.objects.values("id", "doctor_number")
        return [SelectOptionDto(d["id"], d["doctor_number"]) for d in doctor]

    def get_all_for_select_list_doc(self) -> List[SelectOptionDto]:
        doctor = Doctor.objects.values('id', 'specialization')
        return [SelectOptionDto(d['id'], d['specialization'])for d in doctor]

    def get_schedule(self, doctor_number: int):
        doctor = Doctor.objects.get(doctor_number=doctor_number)
        result = GetSchedule
        result.id = doctor.id
        result.appointment_schedule = doctor.appointment_schedules
        return result

    def get_doctor_number(self, doctor_id):
        doctor = Doctor.objects.get(id=doctor_id)
        result = DoctorDetailsDto()
        result.doctor_number = doctor.doctor_number
        return result


