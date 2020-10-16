"""myhospital URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import django
from django.contrib import admin
from django.urls import path, include
from work.views import Home

urlpatterns = [
    path('', Home.index, name='index'),
    path('about/', Home.aboutus, name='about'),
    path('admin/', admin.site.urls),
    path('Login/', include('work.views.Login.login_url')),
    path('patients/', include('work.views.PatientViews.patient_url')),
    path('staff/', include('work.views.Staff_view.staff_url')),
    path('doctor/', include('work.views.Doctor_view.doctor_url')),
    path('medical_record/', include('work.views.medical_record.medical_record_url')),
    path("appointments/", include('work.views.appointment.appointment_url'))
]
