from datetime import date


class CreateStaffDto:
    staff_id: str
    address: str
    date_of_birth: date
    job_title: str
    year_of_employment: date
    level: str
    username: str
    last_name: str
    first_name: str
    email: str
    password: str
    phone: str
    staff_number: str


class ListStaffDto:
    id: int
    staff_id: str
    address: str
    date_of_birth: date
    job_title: str
    year_of_employment: date
    level: str
    username: str
    last_name: str
    first_name: str
    email: str
    password: str
    phone: str
    staff_number: str


class EditStaffDto:
    id: int
    address: str
    date_of_birth: date
    job_title: str
    year_of_employment: date
    level: str
    phone: str


class StaffDetailsDto:
    id: int
    staff_id: str
    address: str
    date_of_birth: date
    job_title: str
    year_of_employment: date
    level: str
    user_last_name: str
    user_first_name: str
    phone: str
    user_email: str
    staff_number: str


class SearchStaffDto:
    id: int
    staff_id: str
    address: str
    date_of_birth: date
    job_title: str
    year_of_employment: date
    level: str
    user_last_name: str
    user_first_name: str
    phone: str
    user_email: str
    staff_number: str
