from dependency_injector import containers, providers

from work.repositorites.AppointmentRepository import AppointmentRepository, DjangoORMAppointmentRepository
from work.repositorites.LabTestReoposistory import LabTestRepository, DjangoORMLabTestRepository
from work.repositorites.MedicalRecordsRepository import MedicalRecordsRepository, DjangoORMMedicalRecordRepository
from work.repositorites.DoctorRepository import DoctorRepository, DjangoORMDoctorRepository
from work.repositorites.StaffRepository import StaffRepository, DjangoOMStaffRepository
from work.repositorites.PatientRepository import PatientRepository, DjangoORMPatientRepository

from work.services.LabTestManagementService import LabTestManagementService, DefaultLabTestManagementService
from work.services.MedicalRecordsManagementService import MedicalRecordsManagementService, \
    DefaultMedicalRecordManagementService
from work.services.DoctorManagementService import DoctorManagementService, DefaultDoctorManagementService
from work.services.StaffManagementService import StaffManagementService, DefaultStaffManagementService
from work.services.PatientManagementService import PatientManagementService, DefaultPatientManagementService
from work.services.AppointmentManagementService import AppointManagementService, DefaultAppointmentManagementService

from typing import Callable


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    appointment_repository: Callable[[], AppointmentRepository] = providers.Factory(
        DjangoORMAppointmentRepository
    )

    lab_test_repository: Callable[[], LabTestRepository] = providers.Factory(
        DjangoORMLabTestRepository
    )

    medical_record_repository: Callable[[], MedicalRecordsRepository] = providers.Factory(
        DjangoORMMedicalRecordRepository
    )

    doctor_repository: Callable[[], DoctorRepository] = providers.Factory(
        DjangoORMDoctorRepository
    )

    staff_repository: Callable[[], StaffRepository] = providers.Factory(
        DjangoOMStaffRepository
    )

    patient_repository: Callable[[], PatientRepository] = providers.Factory(
        DjangoORMPatientRepository
    )

    appointment_management_service: Callable[[], AppointManagementService] = providers.Factory(
        DefaultAppointmentManagementService,
        repository=appointment_repository
    )

    lab_test_management_service: Callable[[], LabTestManagementService] = providers.Factory(
        DefaultLabTestManagementService,
        repository=lab_test_repository
    )

    medical_record_management_service: Callable[[], MedicalRecordsManagementService] = providers.Factory(
        DefaultMedicalRecordManagementService,
        repository=medical_record_repository
    )

    doctor_management_service: Callable[[], DoctorManagementService] = providers.Factory(
        DefaultDoctorManagementService,
        repository=doctor_repository
    )

    staff_management_service: Callable[[], StaffManagementService] = providers.Factory(
        DefaultStaffManagementService,
        repository=staff_repository
    )

    patient_management_service: Callable[[], PatientManagementService] = providers.Factory(
        DefaultPatientManagementService,
        repository=patient_repository
    )


work_service_provider = Container()