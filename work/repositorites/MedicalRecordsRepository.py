from abc import ABCMeta, abstractmethod
from typing import List
from work.models import MedicalRecords
from work.dto.MedicalRecordsDto import CreateMedicalRecordsDto, EditMedicalRecordsDto, ListMedicalRecordsDto, \
    MedicalRecordsDetailsDto, SearchMedicalRecordsDto


class MedicalRecordsRepository(metaclass=ABCMeta):
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



class DjangoORMMedicalRecordRepository(MedicalRecordsRepository):
    def create_medical_record(self, model: CreateMedicalRecordsDto):
        medical_record = MedicalRecords()
        medical_record.diagnosis = model.diagnosis
        medical_record.patient_id = model.patient_id
        medical_record.med_id = model.med_id
        medical_record.doctor_id = model.doctor_id
        medical_record.updated_date = model.updated_date
        medical_record.test_required = model.test_required
        medical_record.treatments = model.treatments
        medical_record.appointment_history = model.appointment_history
        medical_record.med_number = model.med_number
        medical_record.medications = model.medications
        medical_record.save()

    def edit_medical_record(self, id: int, model: EditMedicalRecordsDto):
        try:
            medical_record = MedicalRecords.objects.get(id=id)
            medical_record.diagnosis = model.diagnosis
            medical_record.updated_date = model.updated_date
            medical_record.test_required = model.test_required
            medical_record.treatments = model.treatments
            medical_record.appointment_history = model.appointment_history
            medical_record.save()
        except MedicalRecords.DoesNotExist as e:
            message = 'Medical Record does not exist'
            print(message)
            raise e

    def list_medical_record(self) -> List[ListMedicalRecordsDto]:
        medical_records = list(MedicalRecords.objects.values('id',
                                                             'doctor__staff__user__last_name',
                                                             'doctor__staff__user__first_name',
                                                             'patient__user__first_name',
                                                             'patient__user__last_name',
                                                             'test_required',
                                                             'treatments',
                                                             'appointment_history',
                                                             'updated_date',
                                                             'med_number',
                                                             'diagnosis',
                                                             'medications'))
        result: List[ListMedicalRecordsDto] = []
        for medical_record in medical_records:
            item = ListMedicalRecordsDto()
            item.diagnosis = medical_record['diagnosis']
            item.med_number = medical_record['med_number']
            item.updated_date = medical_record['updated_date']
            item.test_required = medical_record['test_required']
            item.appointment_history = medical_record['appointment_history']
            item.doctor_user_first_name = medical_record['doctor__staff__user__first_name']
            item.doctor_user_last_name = medical_record['doctor__staff__user__last_name']
            item.Patient_user_first_name = medical_record['patient__user__first_name']
            item.Patient_user_last_name = medical_record['patient__user__last_name']
            item.medications = medical_record['medications']
            item.treatment = medical_record['treatments']
            item.id = medical_record['id']
            result.append(item)
        return result

    def medical_record_details(self, id: int) -> MedicalRecordsDetailsDto:
        try:
            medical_record = MedicalRecords.objects.get(id=id)
            result = MedicalRecordsDetailsDto()
            result.patient_user_first_name = medical_record.patient.user.first_name
            result.patient_user_last_name = medical_record.patient.user.last_name
            result.doctor_user_last_name = medical_record.doctor.staff.user.last_name
            result.doctor_user_first_name = medical_record.doctor.staff.user.first_name
            result.appointment_history = medical_record.appointment_history
            result.updated_date = medical_record.updated_date
            result.test_required = medical_record.test_required
            result.med_id = medical_record.med_id
            result.treatment = medical_record.treatments
            result.test_required = medical_record.test_required
            result.diagnosis = medical_record.diagnosis
            result.medication = medical_record.medications
            result.med_number = medical_record.med_number
            return result
        except MedicalRecords.DoesNotExist as e:
            message = 'Medical record does not exit'
            print(message)
            raise e

    def search_medical_record(self, patient_number: str) -> List[SearchMedicalRecordsDto]:
        medical_records = MedicalRecords.objects.filter(patient__patient_number=patient_number)
        medical_records = list(medical_records)
        results = []
        for medical_record in medical_records:
            result = SearchMedicalRecordsDto()
            result.test_required = medical_record.test_required
            result.med_id = medical_record.med_id
            result.med_number = medical_record.med_number
            result.diagnosis = medical_record.diagnosis
            result.medication = medical_record.medications
            result.treatment = medical_record.treatments
            result.doctor_user_last_name = medical_record.doctor.staff.user.last_name
            result.doctor_user_first_name = medical_record.doctor.staff.user.first_name
            result.patient_number = medical_record.patient.patient_number
            result.updated_date = medical_record.updated_date
            result.appointment_history = medical_record.appointment_history
            result.id = medical_record.id
            results.append(result)
        return results
