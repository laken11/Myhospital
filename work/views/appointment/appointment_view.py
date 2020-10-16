import datetime
import uuid
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpRequest
from django.shortcuts import redirect, render
from work.dto.AppointmentDto import SearchAppointmentDto, AppointmentDetailsDto, ListAppointmentDto, \
    CreateAppointmentDto
from work.models import Appointments
from work.service_provider import work_service_provider
from work.decorators import allowed_users


@login_required(login_url='login_get')
def list_appointments(request):
    appointments = work_service_provider.appointment_management_service().list_appointment()
    context = {
        'appointments': appointments
    }
    return render(request, 'appointment/list_appointment.html', context)


@login_required(login_url='login_get')
def list_appointments_doctor(request):
    appointments = work_service_provider.appointment_management_service().list_appointment()
    context = {
        'appointments': appointments
    }
    return render(request, 'doctor/appointment_for_doctor.html', context)


@login_required(login_url='login_get')
def search_appointment(request):
    appointment = work_service_provider.appointment_management_service().search_appointment(
        request.GET.get("appointment_number", None))
    context = {
        'appointment_number': request.GET['appointment_number'],
        'appointment': appointment
    }
    return render(request, 'appointment/appointment_output.html', context)


def search_input_for_staff(request):
    context = {

    }
    return render(request, 'staff/appointment_search.html', context)


def search_appointment_staff(request):
    appointment = work_service_provider.appointment_management_service().search_appointment(
        request.GET.get("appointment_number", None))
    context = {
        'appointment_number': request.GET['appointment_number'],
        'appointment': appointment
    }
    return render(request, 'staff/appointment_output.html', context)


@login_required(login_url='login_get')
def search_input(request):
    context = {

    }
    return render(request, 'appointment/appointment_input.html', context)


@login_required(login_url='login_get')
def create_appointment(request):
    doctors = work_service_provider.doctor_management_service().get_all_for_select_list_doc()
    patient_id = request.user.patient.id
    patient_number = request.user.patient.patient_number
    context = {
        'appointment_number': str(uuid.uuid4()).replace("-", '')[0:10].upper(),
        'appointment_reference': uuid.uuid4(),
        'doctors': doctors,
        'patient_id': patient_id,
        'patient_number': patient_number
    }
    __create_if_post_method(request, context)
    if request.method == ['POST'] and context['saved']:
        return redirect('patient_home')
    return render(request, 'appointment/create_appointment.html', context)


@login_required(login_url='login_get')
@allowed_users(allowed_user=['staffs'])
def create_appointment_for_staff(request):
    patients = work_service_provider.patient_management_service().get_all_for_select_list()
    doctors = work_service_provider.doctor_management_service().get_all_for_select_list_doc()
    context = {
        'appointment_number': str(uuid.uuid4()).replace("-", '')[0:10].upper(),
        'appointment_reference': uuid.uuid4(),
        'patients': patients,
        'doctors': doctors,
    }
    __create_if_post_method(request, context)
    if request.method == ['POST'] and context['saved']:
        return redirect('patient_home')
    return render(request, 'staff/appointment_for staff.html', context)


def __create_if_post_method(request, context):
    if request.method == 'POST':
        try:
            appointment = __get_create_attribute_from_request(request)
            doctor_id = appointment.doctor_id
            doctor = work_service_provider.doctor_management_service().get_doctor_number(doctor_id)
            doctor_number = doctor.doctor_number
            appointment_date = appointment.appointment_datetime
            appointment_schedule = work_service_provider.doctor_management_service().get_schedule(
                doctor_number=doctor_number)
            appointment_schedules = appointment_schedule.appointment_schedule
            appointments = work_service_provider.appointment_management_service().get_appointment_by_date(
                appointment_date, doctor_id)
            number_of_appointments = len(appointments)
            if number_of_appointments < appointment_schedules:
                work_service_provider.appointment_management_service().create_appointment(appointment)
                context['saved'] = True
            else:
                context['saved'] = False
        except Exception as e:
            print(e)
            context['saved'] = False


def __get_create_attribute_from_request(request: HttpRequest):
    create_appointment_dto = CreateAppointmentDto()
    CreateAppointmentDto.appointment_reference = request.POST['appointment_reference']
    __set_create_attribute_from_request(create_appointment_dto, request)
    return create_appointment_dto


def __set_create_attribute_from_request(create_appointment_dto, request):
    create_appointment_dto.doctor_id = request.POST['doctor_id']
    create_appointment_dto.patient_id = request.POST['patient_id']
    create_appointment_dto.appointment_reference = request.POST['appointment_reference']
    create_appointment_dto.appointment_number = request.POST['appointment_number']
    create_appointment_dto.appointment_datetime = request.POST['appointment_datetime']
