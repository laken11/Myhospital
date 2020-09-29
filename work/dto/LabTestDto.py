from datetime import date


class CreateLabTest:
    test_name: str
    test_id: str
    test_result: str
    medical_records_id: int
    date: date
    staff_id: int


class ListLabTest:
    id: int
    test_name: str
    test_id: str
    test_result: str
    medical_records_med_ref: str
    date: date
    staff_last_name: str
    staff_first_name: str


class SearchLabTestDto:
    id: int
    test_name: str
    test_id: str
    test_result: str
    medical_records_med_ref: str
    date: date
    staff_last_name: str
    staff_first_name: str


class EditLabTestDto:
    id: int
    test_name: str
    test_id: str
    test_result: str
    medical_records_med_ref: str
    date: date
    staff_last_name: str
    staff_first_name: str


class LabTestDetailsDto:
    id: int
    test_name: str
    test_id: str
    test_result: str
    medical_records_med_ref: str
    date: date
    staff_last_name: str
    staff_first_name: str
