from django.urls import path
from work.views.appointment import appointment_view

urlpatterns =[
    path('search_input/', appointment_view.search_input_for_staff, name='search_in'),
    path('search_output/', appointment_view.search_appointment_staff, name='search_out'),
    path('search_output/', appointment_view.search_appointment, name='appointment_output'),
    path('search_input/', appointment_view.search_input, name='appointment_input'),
    path('lsit_/', appointment_view.list_appointments_doctor, name='list_appointment_for_doctor'),
    path('list/', appointment_view.list_appointments, name='list_appointments'),
    path('make_appointment/', appointment_view.create_appointment, name='Create_appointment'),
    path('make_appointment_staff/', appointment_view.create_appointment_for_staff, name='create_appointment_for_staff')
]