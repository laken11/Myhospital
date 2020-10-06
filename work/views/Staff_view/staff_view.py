from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404, HttpRequest
from django.shortcuts import render, redirect
from work.service_provider import work_service_provider
from work.models import Staff
from work.dto.StaffDto import StaffDetailsDto, SearchStaffDto, ListStaffDto, EditStaffDto, CreateStaffDto
import uuid
from work.decorators import allowed_users


@login_required(login_url='login_get')
@allowed_users(allowed_user=['staffs'])
def staff_home(request):
    first_name = request.user.first_name
    last_name = request.user.last_name
    email = request.user.email
    phone = request.user.staff.phone
    job_title = request.user.staff.job_title
    year_of_employment = request.user.staff.year_of_employment
    staff_number = request.user.staff.staff_number
    level = request.user.staff.level
    date_of_birth = request.user.staff.date_of_birth
    id = request.user.staff.id
    context = {
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'phone': phone,
        'job_title': job_title,
        'year_of_employment': year_of_employment,
        'staff_number': staff_number,
        'level': level,
        'date_of_birth': date_of_birth,
        'id': id
    }
    return render(request, 'staff/staff_home.html', context)


@login_required(login_url='login_get')
@allowed_users(allowed_user=['staffs'])
def register_staff(request):
    staff_id = uuid.uuid4()
    context = {
        'staff_id': staff_id,
        'staff_number': str(uuid.uuid4()).replace("-", '')[0:10].upper()
    }
    __create_if_post_method(context, request)
    if request.method == 'POST' and context['saved']:
        return redirect("login")
    return render(request, 'staff/register_staff.html', context)


@login_required(login_url='login_get')
@allowed_users(allowed_user=['staffs'])
def list_staff(request):
    staffs = work_service_provider.staff_management_service().list_staff()
    context = {
        'staffs': staffs,
        'title': 'Staffs'
    }
    return render(request, 'staff/staff_list.html', context)


@login_required(login_url='login_get')
@allowed_users(allowed_user=['staffs'])
def staff_details(request, id):
    staff = __get_staff_details_or_raise_404(id)
    context = {
        'title': 'Staff details',
        'staff': staff
    }
    return render(request, 'staff/staff_details.html', context)


@login_required(login_url='login_get')
@allowed_users(allowed_user=['staffs'])
def edit_staff(request, id: int):
    staff_detail_dto = __get_staff_details_or_raise_404(id)
    context = {
        'staff': staff_detail_dto,
        'date_of_birth': staff_detail_dto.date_of_birth.strftime("%Y-%m-%d %H:%M:%S"),
        'year_of_employment': staff_detail_dto.year_of_employment.strftime("%Y-%m-%d %H:%M:%S"),
        'id': id,
        'title': 'Edit flight',
    }
    new_staff_dto = __edit_if_post_method(context, request, id)
    if new_staff_dto is not None:
        context['staff'] = new_staff_dto
    return render(request, 'staff/edit_staff.html', context)


@login_required(login_url='login_get')
@allowed_users(allowed_user=['staffs'])
def search_input(request):
    context = {

    }
    return render(request, 'staff/search.html', context)


@login_required(login_url='login_get')
@allowed_users(allowed_user=['staffs'])
def search_staff(request):
    staff = work_service_provider.staff_management_service().search_staff(request.GET.get("staff_number", None))
    context = {
        'staff': staff,
        'staff_number': request.GET['staff_number']
    }
    return render(request, 'staff/search_result.html', context)


def __get_staff_details_or_raise_404(id):
    try:
        staff = work_service_provider.staff_management_service().staff_details(id)
    except Staff.DoesNotExist:
        raise Http404('Staff dose not exit')
    return staff


def __set_staff_attribute_from_request_for_edit(edit_staff_dto, request):
    edit_staff_dto.phone = request.POST['phone']
    edit_staff_dto.address = request.POST['address']
    edit_staff_dto.date_of_birth = request.POST['date_of_birth']
    edit_staff_dto.year_of_employment = request.POST['year_of_employment']
    edit_staff_dto.job_title = request.POST['job_title']
    edit_staff_dto.level = request.POST['level']


def __get_staff_attribute_from_request_edit(request, id: int):
    edit_staff_dto = EditStaffDto()
    edit_staff_dto.id = id
    __set_staff_attribute_from_request_for_edit(edit_staff_dto, request)
    return edit_staff_dto


def __edit_if_post_method(context, request: HttpRequest, id: int):
    if request.method == 'POST':
        try:
            staff = __get_staff_attribute_from_request_edit(request, id)
            work_service_provider.staff_management_service().edit_staff(staff, id)
            context['saved'] = True
            return __get_staff_details_or_raise_404(id)
        except Exception as e:
            print(e)
            context['saved'] = False


def __set_staff_attribute_from_request(create_staff_dto, request):
    create_staff_dto.username = request.POST['username']
    create_staff_dto.password = request.POST['password']
    create_staff_dto.email = request.POST['email']
    create_staff_dto.phone = request.POST['phone']
    create_staff_dto.staff_id = request.POST['staff_id']
    create_staff_dto.address = request.POST['address']
    create_staff_dto.date_of_birth = request.POST['date_of_birth']
    create_staff_dto.job_title = request.POST['job_title']
    create_staff_dto.year_of_employment = request.POST['year_of_employment']
    create_staff_dto.level = request.POST['level']
    create_staff_dto.first_name = request.POST['first_name']
    create_staff_dto.last_name = request.POST['last_name']
    create_staff_dto.staff_number = request.POST['staff_number']


def __get_create_staff_dto_from_request(request: HttpRequest):
    create_staff_dto = CreateStaffDto()
    create_staff_dto.phone = request.POST['phone']
    __set_staff_attribute_from_request(create_staff_dto, request)
    return create_staff_dto


def __create_if_post_method(context, request):
    if request.method == 'POST':
        try:
            staff = __get_create_staff_dto_from_request(request)
            work_service_provider.staff_management_service().create_staff(staff)
            context['saved'] = True
        except Exception as e:
            print(e)
            context['saved'] = False







