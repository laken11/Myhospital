from django.urls import path
from work.views.medical_record import medical_record_view

urlpatterns = [
    path('search_med_input/', medical_record_view.search_medical_record_input, name='search_med_input'),
    path('sesrch_med_output/', medical_record_view.search_medical_record_post_output, name='search_med_output'),
    path('list/', medical_record_view.list_medical_record, name='list_medical_record'),
    path('create/', medical_record_view.create_medical_record, name='create_medical_record'),
    path('<id>/', medical_record_view.medical_record_details, name='medical_record_details')
]
