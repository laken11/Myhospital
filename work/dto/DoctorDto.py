class CreateDoctorDto:
    staff_id: int
    specialization: str
    appointment_schedule: int
    doctor_number: str


class ListDoctorDto:
    id: int
    staff_last_name: str
    staff_first_name: str
    specialization: str
    appointment_schedule: int


class EditDoctorDto:
    id: int
    staff_last_name: str
    staff_first_name: str
    specialization: str
    appointment_schedule: int


class DoctorDetailsDto:
    id: int
    staff_last_name: str
    staff_first_name: str
    specialization: str
    appointment_schedule: int
    doctor_number: str


class SearchDoctorDto:
    id: int
    staff_last_name: str
    staff_first_name: str
    specialization: str
    appointment_schedule: str
    doctor_number: str


class GetSchedule:
    id: int
    appointment_schedule: str
