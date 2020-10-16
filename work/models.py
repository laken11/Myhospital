from django.db import models
import uuid
from django.contrib.auth.models import User


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.RESTRICT)
    patient_id = models.UUIDField(default=uuid.uuid4, editable=False)
    patient_number = models.CharField(max_length=10)
    phone = models.CharField(max_length=20, null=True)
    address = models.CharField(max_length=150)
    date_of_birth = models.DateField()
    occupation = models.CharField(max_length=50, null=True)
    marital_status = models.CharField(max_length=50, null=True)
    gender = models.CharField(max_length=10)
    blood_group = models.CharField(max_length=10, null=True)
    genotype = models.CharField(max_length=5, null=True)
    next_of_kin = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.user.username}\t{self.patient_number}\t{self.user.first_name}\t{self.user.last_name}'


class Staff(models.Model):
    staff_id = models.UUIDField(default=uuid.uuid4, editable=False)
    staff_number = models.CharField(max_length=10)
    address = models.CharField(max_length=150)
    user = models.OneToOneField(User, on_delete=models.RESTRICT)
    date_of_birth = models.DateField()
    job_title = models.CharField(max_length=50)
    year_of_employment = models.DateField()
    level = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.user.username}\t{self.staff_number}\t{self.user.first_name}\t{self.user.last_name}'


class Doctor(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.RESTRICT)
    specialization = models.CharField(max_length=50)
    appointment_schedules = models.IntegerField(default=0)
    doctor_number = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.staff.user.username}\t{self.staff.staff_number}\t{self.doctor_number}\t{self.specialization}\t{self.appointment_schedules}'


class MedicalRecords(models.Model):
    med_id = models.UUIDField(default=uuid.uuid4, editable=False)
    med_number = models.CharField(max_length=10)
    patient = models.ForeignKey(Patient, on_delete=models.RESTRICT)
    diagnosis = models.CharField(max_length=500)
    treatments = models.CharField(max_length=500)
    medications = models.CharField(max_length=500)
    test_required = models.CharField(max_length=150, null=True)
    appointment_history = models.CharField(max_length=50)
    updated_date = models.DateField()
    doctor = models.ForeignKey(Doctor, on_delete=models.RESTRICT)

    def __str__(self):
        return f'{self.med_number}\t{self.patient.user.username}'

class Appointments(models.Model):
    appointment_datetime = models.DateField()
    appointment_reference = models.UUIDField(default=uuid.uuid4, editable=False)
    appointment_number = models.CharField(max_length=10)
    patient = models.ForeignKey(Patient, on_delete=models.RESTRICT)
    doctor = models.ForeignKey(Doctor, on_delete=models.RESTRICT)

    def __str__(self):
        return f'{self.appointment_number}'

class LabTest(models.Model):
    test_name = models.CharField(max_length=150)
    test_number = models.CharField(max_length=10)
    test_reference = models.UUIDField(default=uuid.uuid4, editable=False)
    test_result = models.CharField(max_length=500)
    medical_records = models.ForeignKey(MedicalRecords, on_delete=models.RESTRICT)
    date = models.DateField()
    staff = models.ForeignKey(Staff, on_delete=models.RESTRICT)

    def __str__(self):
        return f'{self.test_name}\t{self.test_number}\t{self.test_result}\t{self.medical_records}\t{self.date}\t{self.staff}'
