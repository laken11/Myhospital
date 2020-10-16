import uuid

from requests import request

from work.decorators import allowed_users
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404, HttpRequest
from django.shortcuts import render, redirect
from work.service_provider import work_service_provider
from work.models import Patient
from work.dto.PatientDto import ListPatientDto, SearchPatientDto, EditPatientDto, CreatePatientDto, PatientDetailsDto
from django.core.exceptions import ValidationError


@login_required(login_url='login_get')
@allowed_users(allowed_user=['staffs'])
def list_patient(request):
    patients = work_service_provider.patient_management_service().list_patient()
    context = {
        "title": 'Patients',
        'patients': patients
    }
    return render(request, 'patient/viewpatient.html', context)


@login_required(login_url='login_get')
@allowed_users(allowed_user=['doctor'])
def list_patient_for_doctor(request):
    patients = work_service_provider.patient_management_service().list_patient()
    context = {
        "title": 'Patients',
        'patients': patients
    }
    return render(request, 'doctor/list_patient_for_doc.html', context)


def register_user_get(request):
    context = {

    }
    return render(request, 'patient/Registerpage.html', context)


def register_user_post(request):
    patient_id = uuid.uuid4()
    patient_number = str(uuid.uuid4()).replace("-", '')[0:10].upper()
    context = {
        'patient_id': patient_id,
        'patient_number': patient_number
    }
    __create_if_post_method(context, request)
    if request.method == 'POST' and context['saved']:
        return redirect("login_get")
    return render(request, 'patient/Registerpage.html', context)


@login_required(login_url='login_get')
@allowed_users(allowed_user=['staffs'])
def register_user_post_staff(request):
    patient_id = uuid.uuid4()
    patient_number = str(uuid.uuid4()).replace("-", '')[0:10].upper()
    context = {
        'patient_id': patient_id,
        'patient_number': patient_number
    }
    __create_if_post_method(context, request)
    if request.method == 'POST' and context['saved']:
        return redirect("aad_patient_for_staff")
    return render(request, 'staff/add_patiant_for_staff.html', context)


@login_required(login_url='login_get')
@allowed_users(allowed_user=['patients'])
def patient_home(request):
    first_name = request.user.first_name
    last_name = request.user.last_name
    email = request.user.email
    gender = request.user.patient.gender
    address = request.user.patient.address
    genotype = request.user.patient.genotype
    marital_status = request.user.patient.marital_status
    patient_number = request.user.patient.patient_number
    blood_group = request.user.patient.blood_group
    date_of_birth = request.user.patient.date_of_birth
    occupation = request.user.patient.occupation
    phone = request.user.patient.phone
    next_of_kin = request.user.patient.next_of_kin
    id = request.user.patient.id
    context = {
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'gender': gender,
        'address': address,
        'genotype': genotype,
        'marital_status': marital_status,
        'patient_number': patient_number,
        'blood_group': blood_group,
        'date_of_birth': date_of_birth,
        'occupation': occupation,
        'phone': phone,
        'next_of_kin': next_of_kin,
        'id': id
    }
    return render(request, 'patient/patientHome.html', context)


@login_required(login_url='login_get')
@allowed_users(allowed_user=['staffs'])
def patient_details(request, patient_id):
    patient = __get_patient_details_dto_or_rise_404(patient_id)
    context = {
        'title': 'Patient Details',
        'patient': patient
    }
    return render(request, 'staff/patient_details.html', context)


@login_required(login_url='login_get')
def edit_patient(request, patient_id):
    patient_details_dto = __get_patient_details_dto_or_rise_404(patient_id)
    context = {
        'title': f'Edit patient {patient_details_dto.user_first_name}',
        'patient_id': patient_id,
        'patient': patient_details_dto,
        'date_of_birth': patient_details_dto.date_of_birth.strftime("%Y-%m-%d %H:%M:%S"),
    }
    new_patient_dto = __edit_if_post_method(context, request, patient_id)
    if new_patient_dto is not None:
        context["patient"] = new_patient_dto
    return render(request, "patient/edit_patient.html", context)


@login_required(login_url='login_get')
@allowed_users(allowed_user=['staffs'])
def search_input(request):
    context = {

    }
    return render(request, 'staff/search_input.html', context)


@login_required(login_url='login_get')
@allowed_users(allowed_user=['staffs'])
def search_patient(request):
    patient = work_service_provider.patient_management_service().search_patient(request.GET.get('patient_number', None))
    context = {
        'patient': patient,
        'patient_number': request.GET['patient_number']
    }
    return render(request, 'staff/search_patient.html', context)


@login_required(login_url='login_get')
@allowed_users(allowed_user=['staffs'])
def edit_patient_for_staff(request, patient_id: int):
    patient_details_dto = __get_patient_details_dto_or_rise_404(patient_id)
    context = {
        'title': f'Edit patient {patient_details_dto.user_first_name}',
        'patient_id': patient_id,
        'patient': patient_details_dto,
        'date_of_birth': patient_details_dto.date_of_birth.strftime("%Y-%m-%d %H:%M:%S"),
    }
    new_patient_dto = __edit_if_post_method(context, request, patient_id)
    if new_patient_dto is not None:
        context["patient"] = new_patient_dto
    return render(request, "staff/edit_patient_for_staff.html", context)


def __set_patient_attributes_form_request_edit(edit_patient_dto, request):
    edit_patient_dto.blood_group = request.POST['blood_group']
    edit_patient_dto.phone = request.POST['phone']
    edit_patient_dto.gender = request.POST['gender']
    edit_patient_dto.address = request.POST['address']
    edit_patient_dto.date_of_birth = request.POST['date_of_birth']
    edit_patient_dto.genotype = request.POST['genotype']
    edit_patient_dto.next_of_kin = request.POST['next_of_kin']
    edit_patient_dto.marital_status = request.POST['marital_status']
    edit_patient_dto.occupation = request.POST['occupation']


def __set_patient_attributes_form_request(create_patient_dto, request):
    create_patient_dto.phone = request.POST['phone']
    create_patient_dto.address = request.POST['address']
    create_patient_dto.gender = request.POST['gender']
    create_patient_dto.blood_group = request.POST['blood_group']
    create_patient_dto.marital_status = request.POST['marital_status']
    create_patient_dto.genotype = request.POST['genotype']
    create_patient_dto.next_of_kin = request.POST['next_of_kin']
    create_patient_dto.occupation = request.POST['occupation']
    create_patient_dto.username = request.POST['username']
    create_patient_dto.first_name = request.POST['first_name']
    create_patient_dto.last_name = request.POST['last_name']
    create_patient_dto.password = request.POST['password']
    create_patient_dto.email = request.POST['email']
    create_patient_dto.date_of_birth = request.POST['date_of_birth']
    create_patient_dto.patient_number = request.POST['patient_number']
    create_patient_dto.patient_id = request.POST['patient_id']
    create_patient_dto.confirm_password = request.POST['confirm_password']


def __get_edit_patient_dto_from_request(request: HttpRequest, patient_id: int) -> EditPatientDto:
    edit_patient_dto = EditPatientDto()
    edit_patient_dto.id = patient_id
    __set_patient_attributes_form_request_edit(edit_patient_dto, request)
    return edit_patient_dto


def __get_create_patient_dto_from_request(request: HttpRequest) -> CreatePatientDto:
    create_patient_dto = CreatePatientDto()
    create_patient_dto.phone = request.POST['phone']
    __set_patient_attributes_form_request(create_patient_dto, request)
    return create_patient_dto


def __create_if_post_method(context, request):
    if request.method == 'POST':
        try:
            patient = __get_create_patient_dto_from_request(request)
            password = patient.password
            confirm_password = patient.confirm_password
            if password == confirm_password:
                work_service_provider.patient_management_service().create_patient(patient)
                context['saved'] = True
            else:
                context['saved'] = False
        except Exception as e:
            context['saved'] = False


def __edit_if_post_method(context, request: HttpRequest, patient_id: int):
    if request.method == 'POST':
        try:
            patient = __get_edit_patient_dto_from_request(request, patient_id)
            work_service_provider.patient_management_service().edit_patient(patient_id, patient)
            context['saved'] = True
            return __get_patient_details_dto_or_rise_404(patient_id)
        except Exception as e:
            print(e)
            context['saved'] = False


def __get_patient_details_dto_or_rise_404(patient_id) -> PatientDetailsDto:
    try:
        patient = work_service_provider.patient_management_service().patient_details(patient_id)
    except Patient.DoesNotExist:
        raise Http404("requested patient dose not exit")
    return patient
