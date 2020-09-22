from django.http import HttpRequest, Http404
from work.dto.MedicalRecordsDto import SearchMedicalRecordsDto, MedicalRecordsDetailsDto, ListMedicalRecordsDto, EditMedicalRecordsDto, CreateMedicalRecordsDto
from work.models import MedicalRecords
from work.service_provider import work_service_provider
from django.shortcuts import redirect, render


def list_medical_record(request):
    medical_records = work_service_provider.medical_record_management_service().list_medical_record()
    context = {
        'medical_records': medical_records
    }
    return render(request, '', context)


def create_medical_record(request):
    patients = work_service_provider.patient_management_service().get_all_for_select_list()
    doctors = work_service_provider.doctor_management_service().get_all_for_select_list()
    context = {
        'patients': patients,
        'doctors': doctors
    }
    __create_if_post_method(request, context)
    if request.method == 'POST' and context['saved']:
        return redirect('')
    return render(request, '', context)


def __set_create_attribute_from_request(create_medical_record_dto, request):
    create_medical_record_dto.med_id = request.POST['med_id']
    create_medical_record_dto.med_number = request.POST['med_number']
    create_medical_record_dto.patient_id = request.POST['patient_id']
    create_medical_record_dto.doctor_id = request.POST['doctor_id']
    create_medical_record_dto.treatments = request.POST['treatments']
    create_medical_record_dto.medications = request.POST['medications']
    create_medical_record_dto.test_required = request.POST['test_required']
    create_medical_record_dto.appointment_history = request.POST['appointment_history']
    create_medical_record_dto.updated_date = request.POST['updated_date']


def __get_create_attribute_from_request( request):
    create_medical_record_dto = CreateMedicalRecordsDto()
    create_medical_record_dto.med_id = request.POST['med_id']
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