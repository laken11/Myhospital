import uuid
from work.decorators import allowed_users
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, Http404
from work.dto.MedicalRecordsDto import SearchMedicalRecordsDto, MedicalRecordsDetailsDto, ListMedicalRecordsDto, EditMedicalRecordsDto, CreateMedicalRecordsDto
from work.models import MedicalRecords
from work.service_provider import work_service_provider
from django.shortcuts import redirect, render


@login_required(login_url='login_get')
# @allowed_users(['doctor'])
def list_medical_record(request):
    medical_records = work_service_provider.medical_record_management_service().list_medical_record()
    context = {
        'medical_records': medical_records
    }
    return render(request, 'medical_record/list_doctor.html', context)


@login_required(login_url='login_get')
# @allowed_users(['doctor'])
def create_medical_record(request):
    patient = work_service_provider.patient_management_service().get_all_for_select_list()
    doctor = work_service_provider.doctor_management_service().get_all_for_select_list()
    med_id = uuid.uuid4()
    med_number = str(uuid.uuid4()).replace("-", '')[0:10].upper()
    context = {
        'patient': patient,
        'doctor': doctor,
        'med_id': med_id,
        'med_number': med_number
    }
    __create_if_post_method(request, context)
    if request.method == 'POST' and context['saved']:
        return redirect('doctor_home')
    return render(request, 'medical_record/create_med_red.html', context)


def __set_create_attribute_from_request(create_medical_record_dto, request):
    create_medical_record_dto.med_number = request.POST['med_number']
    create_medical_record_dto.patient_id = request.POST['patient_id']
    create_medical_record_dto.doctor_id = request.POST['doctor_id']
    create_medical_record_dto.treatments = request.POST['treatments']
    create_medical_record_dto.medications = request.POST['medications']
    create_medical_record_dto.test_required = request.POST['test_required']
    create_medical_record_dto.appointment_history = request.POST['appointment_history']
    create_medical_record_dto.updated_date = request.POST['updated_date']
    create_medical_record_dto.diagnosis = request.POST['diagnosis']
    create_medical_record_dto.med_id = request.POST['med_id']


def __get_create_attribute_from_request( request):
    create_medical_record_dto = CreateMedicalRecordsDto()
    create_medical_record_dto.med_number = request.POST['med_number']
    __set_create_attribute_from_request(create_medical_record_dto, request)
    return create_medical_record_dto


def __create_if_post_method(request, context):
    if request.method == 'POST':
        try:
            medical_record = __get_create_attribute_from_request(request)
            work_service_provider.medical_record_management_service().create_medical_record(medical_record)
            context['saved'] = True
        except Exception as e:
            print(e)
            context['saved'] = False
