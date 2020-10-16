from datetime import date


class CreatePatientDto:
    username: str
    last_name: str
    first_name: str
    email: str
    password: str
    phone: str
    address: str
    date_of_birth: date
    occupation: str
    marital_status: str
    gender: str
    blood_group: str
    genotype: str
    next_of_kin: str
    patient_id: str
    patient_number: str
    confirm_password: str


class EditPatientDto:
    id: int
    user_id: int
    phone: str
    address: str
    date_of_birth: date
    occupation: str
    marital_status: str
    gender: str
    blood_group: str
    genotype: str
    next_of_kin: str


class PatientDetailsDto:
    id: int
    phone: str
    address: str
    date_of_birth: date
    occupation: str
    marital_status: str
    gender: str
    blood_group: str
    genotype: str
    next_of_kin: str
    user_last_name: str
    user_first_name: str
    user_email: str
    patient_id: str
    patient_number: str


class SearchPatientDto:
    id: int
    user_id: int
    phone: str
    address: str
    date_of_birth: date
    occupation: str
    marital_status: str
    gender: str
    blood_group: str
    genotype: str
    next_of_kin: str
    user_last_name: str
    user_first_name: str
    user_email: str
    patient_number: str


class ListPatientDto:
    id: int
    phone: str
    address: str
    date_of_birth: date
    occupation: str
    marital_status: str
    gender: str
    blood_group: str
    genotype: str
    next_of_kin: str
    user_last_name: str
    user_first_name: str
    user_email: str
    patient_number: str
    patient_id: str


