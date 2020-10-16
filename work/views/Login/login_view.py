from django.contrib.auth.models import User
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from work.decorators import unauthenticated_user
from work.dto.PasswordDto import ChangePassDto
from django.contrib.auth.models import User


def logout_view(request):
    logout(request)
    return redirect('index')


@unauthenticated_user
def login_page_gt(request):
    context = {

    }
    return render(request, 'login/loginpage.html', context)


@unauthenticated_user
def login_page_post(request):
    context = {

    }
    username = request.POST.get('username', False)
    password = request.POST.get('password')
    user: User = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        if user.groups.filter(name__exact="patients").exists():
            return redirect("patient_home")
        elif user.groups.filter(name__exact="staffs").exists():
            return redirect("staff_home")
        elif user.groups.filter(name__exact="doctor").exists():
            return redirect("doctor_home")
    else:
        context['message'] = 'username or password incorrect'
    return render(request, 'login/loginpage.html', context)


def change_password(request):
    context = {

    }
    __change_if_post(context, request)
    if request.method == 'POST' and context['saved']:
        return redirect("login_get")
    return render(request, 'login/forget_password.html', context)


def __get_attribute_from_request(password_dto, request):
    password_dto.username = request.POST['username']
    password_dto.password = request.POST['password']
    password_dto.confirm_password = request.POST['confirm_password']


def __get_password_dto_from_request(request: HttpRequest):
    password_dto = ChangePassDto()
    password_dto.username = request.POST['username']
    __get_attribute_from_request(password_dto, request)
    return password_dto


def __change_if_post(context, request):
    if request.method == 'POST':
        try:
            user = __get_password_dto_from_request(request)
            username = user.username
            password = user.password
            confirm_password = user.confirm_password
            if password == confirm_password:
                u = User.objects.get(username__exact=username)
                u.set_password(password)
                u.save()
                context['saved'] = True
            else:
                context['saved'] = False
        except Exception as e:
            print(e)
            context['saved'] = False



































