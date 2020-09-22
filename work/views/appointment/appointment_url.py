from django.urls import path
from work.views.appointment import appointment_view

urlpatterns =[
    path('list/', appointment_view.list_appointments, name='list_appointments'),
    path('make_appointment/', appointment_view.create_appointment, name='Create_appointment')
]