from abc import ABCMeta, abstractmethod
from typing import List
from work.models import Patient
from work.dto.PatientDto import CreatePatientDto, EditPatientDto, ListPatientDto, PatientDetailsDto, SearchPatientDto
from django.contrib.auth.models import User, Group
from work.dto.CommonDto import SelectOptionDto


class PatientRepository(metaclass=ABCMeta):
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


class DjangoORMPatientRepository(PatientRepository):
    def create_patient(self, model: CreatePatientDto):
        patient = Patient()
        patient.phone = model.phone
        patient.address = model.address
        patient.date_of_birth = model.date_of_birth
        patient.gender = model.gender
        patient.blood_group = model.blood_group
        patient.marital_status = model.marital_status
        patient.genotype = model.genotype
        patient.next_of_kin = model.next_of_kin
        patient.occupation = model.occupation
        patient.patient_id = model.patient_id
        patient.patient_number = model.patient_number

        user = User.objects.create_user(model.username, model.email, model.password)
        user.last_name = model.last_name
        user.first_name = model.first_name
        user.save()
        patient.user = user
        patients = Group.objects.get(name='patients')
        user.groups.add(patients)

        patient.save()

    def edit_patient(self, id: int, model: EditPatientDto):
        try:
            patient = Patient.objects.get(id=id)
            patient.occupation = model.occupation
            patient.gender = model.gender
            patient.blood_group = model.blood_group
            patient.marital_status = model.marital_status
            patient.next_of_kin = model.next_of_kin
            patient.phone = model.phone
            patient.genotype = model.genotype
            patient.date_of_birth = model.date_of_birth
            patient.address = model.address
            patient.save()
        except Patient.DoesNotExist as e:
            message = "Patient dose not exist"
            print(message)
            raise e

    def patient_details(self, id: int) -> PatientDetailsDto:
        try:
            patient = Patient.objects.get(id=id)
            result = PatientDetailsDto()
            result.genotype = patient.genotype
            result.phone = patient.phone
            result.gender = patient.gender
            result.marital_status = patient.marital_status
            result.address = patient.address
            result.id = patient.id
            result.user_last_name = patient.user.last_name
            result.user_first_name = patient.user.first_name
            result.user_email = patient.user.email
            result.occupation = patient.occupation
            result.next_of_kin = patient.next_of_kin
            result.date_of_birth = patient.date_of_birth
            result.blood_group = patient.blood_group
            result.patient_number = patient.patient_number
            result.patient_id = patient.patient_id
            return result
        except Patient.DoesNotExist as e:
            message = "Patient dose not exist"
            print(message)
            raise e

    def search_patient(self, patient_number: str) -> SearchPatientDto:
        try:
            patient = Patient.objects.get(patient_number=patient_number)
            result = SearchPatientDto()
            result.id = patient.id
            result.user_last_name = patient.user.first_name
            result.user_first_name = patient.user.last_name
            result.date_of_birth = patient.date_of_birth
            result.gender = patient.gender
            result.marital_status = patient.marital_status
            result.occupation = patient.occupation
            result.genotype = patient.genotype
            result.next_of_kin = patient.next_of_kin
            result.phone = patient.phone
            result.blood_group = patient.blood_group
            result.address = patient.address
            result.email = patient.user.email
            result.patient_number = patient.patient_number
            return result
        except Patient.DoesNotExist as e:
            message = "Patient dose not exist"
            print(message)
            raise e

    def list_patient(self) -> List[ListPatientDto]:
        patients = list(Patient.objects.values('id',
                                               'user__last_name',
                                               'user__first_name',
                                               'user__email',
                                               'phone',
                                               'address',
                                               'blood_group',
                                               'genotype',
                                               'next_of_kin',
                                               'occupation',
                                               'marital_status',
                                               'gender',
                                               'date_of_birth',
                                               'patient_number',
                                               'patient_id'))
        result: List[ListPatientDto] = []
        for patient in patients:
            item = ListPatientDto()
            item.id = patient['id']
            item.user_first_name = patient['user__first_name']
            item.user_last_name = patient['user__last_name']
            item.user_email = patient['user__email']
            item.phone = patient['phone']
            item.address = patient['address']
            item.blood_group = patient['blood_group']
            item.genotype = patient['genotype']
            item.next_of_kin = patient['next_of_kin']
            item.occupation = patient['occupation']
            item.marital_status = patient['marital_status']
            item.gender = patient['gender']
            item.date_of_birth = patient['date_of_birth']
            item.patient_number = patient['patient_number']
            item.patient_id = patient['patient_id']
            result.append(item)
        return result

    def get_all_for_select_list(self) -> List[SelectOptionDto]:
        patient = Patient.objects.values("id", "patient_number")
        return [SelectOptionDto(p["id"], p["patient_number"]) for p in patient]
