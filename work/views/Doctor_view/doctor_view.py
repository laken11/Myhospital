import uuid

from work.dto.DoctorDto import SearchDoctorDto, DoctorDetailsDto, ListDoctorDto, EditDoctorDto, CreateDoctorDto
from work.service_provider import work_service_provider
from work.models import Doctor
from django.shortcuts import render, redirect
from django.http import Http404, HttpRequest, HttpResponse


def list_doctors(request):
    doctors = work_service_provider.doctor_management_service().list_doctors()
    context = {
        'title': 'Doctor',
        'doctors': doctors,
        'doctor_number': str(uuid.uuid4()).replace("-", '')[0:10].upper()
    }
    return render(request, '', context)


def doctor_details(request, doctor_id):
    doctor = __get_doctor_details_or_raise_404(doctor_id)
    context = {
        'title': "Doctor's details",
        'doctor': doctor
    }
    return render(request, '', context)


def create_doctor(request):
    staff = work_service_provider.staff_management_service().get_all_for_select_list()
    context = {
        'staff': staff
    }
    __create_if_post_method(request, context)
    if request.method == 'POST' and context['saved']:
        return redirect('')
    return render(request, '', context)


def __set_create_attribute_from_request(create_doctor_dto, request):
    create_doctor_dto.specialization = request.POST['specialization']
    create_doctor_dto.appointment_schedule = request.POST['appointment_schedule']
    create_doctor_dto.staff_id = request.POST['staff_id']


def __get_create_attribute_from_request(request: HttpRequest):
    create_doctor_dto = CreateDoctorDto()
    create_doctor_dto.specialization = request.POST['specialization']
    __set_create_attribute_from_request(create_doctor_dto, request)
    return create_doctor_dto


def __create_if_post_method(request, context):
    if request.method == 'POST':
        try:
            doctor = __get_create_attribute_from_request(request)
            work_service_provider.doctor_management_service().create_doctor(doctor)
            context['saved'] = True
        except Exception as e:
            print(e)
            context['saved'] = False


def __get_doctor_details_or_raise_404(doctor_id):
    try:
        doctor = work_service_provider.doctor_management_service().doctor_details(doctor_id)
    except Doctor.DoesNotExist:
        raise Http404('Appointment does not exits')
    return doctor
