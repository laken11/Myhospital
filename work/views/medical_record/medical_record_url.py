from django.urls import path
from work.views.medical_record import medical_record_view

urlpatterns = [
    path('list/', medical_record_view.list_medical_record, name='list_medical_record'),
    path('create/', medical_record_view.create_medical_record, name='create_medical_record')
]