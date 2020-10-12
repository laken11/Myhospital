from datetime import date


class CreateMedicalRecordsDto:
    patient_id: int
    diagnosis: str
    medications: str
    test_required: str
    appointment_history: str
    updated_date: date
    doctor_id: int
    treatments: str
    med_id: str
    med_number: str


class EditMedicalRecordsDto:
    id: int
    diagnosis: str
    medications: str
    treatments: str
    appointment_history: str
    updated_date: date
    test_required: str


class MedicalRecordsDetailsDto:
    id: int
    doctor_user_last_name: str
    test_required: str
    appointment_history: str
    updated_date: date
    patient_user_last_name: str
    diagnosis: str
    medication: str
    med_id: str
    Patient_user_first_name: str
    doctor_user_first_name: str
    med_number: str
    treatment: str



class SearchMedicalRecordsDto:
    id: int
    doctor_user_last_name: str
    test_required: str
    appointment_history: str
    updated_date: date
    patient_number: str
    diagnosis: str
    medication: str
    med_id: str
    doctor_user_first_name: str
    med_number: str
    treatment: str


class ListMedicalRecordsDto:
    id: int
    Patient_user_last_name: str
    diagnosis: str
    medications: str
    test_required: int
    appointment_history: str
    updated_date: date
    doctor_user_last_name: str
    med_id: str
    doctor_user_first_name: str
    Patient_user_first_name: str
    med_number: str

