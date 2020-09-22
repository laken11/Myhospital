from django.http import Http404, HttpRequest
from django.shortcuts import redirect, render
from work.dto.AppointmentDto import SearchAppointmentDto, AppointmentDetailsDto, ListAppointmentDto, CreateAppointmentDto
from work.models import Appointments
from work.service_provider import work_service_provider


def list_appointments(request):
    appointments = work_service_provider.appointment_management_service().list_appointment()
    context = {
        'appointments': appointments
    }
    return render(request, '', context)


def create_appointment(request):
    patients = work_service_provider.patient_management_service().get_all_for_select_list()
    doctors = work_service_provider.doctor_management_service().get_all_for_select_list_doc()
    context = {
        'patients': patients,
        'doctors': doctors
    }
    return render(request, '', context)


def __create_if_post_method(context, request):
    if request.method == 'POST':
        try:
            appointment = __get_create_attribute_from_request(request)
            work_service_provider.appointment_management_service().create_appointment(appointment)
            context['saved'] = True
        except Exception as e:
            print(e)
            context['saved'] = False


def __get_create_attribute_from_request(request):
    create_appointment_dto = CreateAppointmentDto()
    CreateAppointmentDto.appointment_number = request.POST['appointment_number']
    __set_create_attribute_from_request(create_appointment_dto, request)
    return create_appointment_dto


def __set_create_attribute_from_request(create_appointment_dto, request):
    create_appointment_dto.doctor_id = request.POST['doctor_id']
    create_appointment_dto.patient_id = request.POST['patient_id']
    create_appointment_dto.appointment_reference = request.POST['appointment_reference']
    create_appointment_dto.appointment_number = request.POST['appointment_number']
    create_appointment_dto.appointment_datetime = request.POST['appointment_datetime']
