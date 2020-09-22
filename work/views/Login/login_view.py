from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
import uuid


def logout_view(request):
    logout(request)
    return redirect('index')


def login_page_post(request):
    context = {

    }
    username = request.POST.get('username', False)
    password = request.POST.get('password')
    user: User = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # return redirect('index')
        if user.groups.filter(name__exact="patients").exists():
            return redirect("patient_home")
        elif user.groups.filter(name__exact="staffs").exists():
            return redirect("staff_home")
        # elif user.groups.filter(name__exact="staff").exists():
        #     redirect("staff_home")
    else:
        context['message'] = 'Username or password invalid'
    return render(request, 'login/loginpage.html', context)































