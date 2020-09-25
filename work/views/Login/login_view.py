from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from work.decorators import unauthenticated_user


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































