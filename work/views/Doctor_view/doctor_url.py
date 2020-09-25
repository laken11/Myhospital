from django.urls import path
from work.views.Doctor_view import doctor_view

urlpatterns = [
    path('home/', doctor_view.doctor_home, name='doctor_home'),
    path('list/', doctor_view.list_doctors, name='list_doctors'),
    path('add_doctor/', doctor_view.create_doctor, name="create_doctors"),
    path('<doctor_id>/', doctor_view.doctor_details, name='details'),
]