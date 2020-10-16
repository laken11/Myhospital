from django.urls import path
from work.views.PatientViews import patient_view

urlpatterns = [
    path("register_get/", patient_view.register_user_get, name='register_get'),
    path('search/', patient_view.search_patient, name='search_patient'),
    path('list_for_doctor/', patient_view.list_patient_for_doctor, name='list_for_doctor'),
    path('searhinput', patient_view.search_input, name='searchInput'),
    path('register/', patient_view.register_user_post, name="register"),
    path('register_staff/', patient_view.register_user_post_staff, name='add_patient_for_staff'),
    path('view_patients/', patient_view.list_patient, name='list_patients'),
    path('<patient_id>/', patient_view.patient_details, name='patient_details'),
    path('<patient_id>/edit_for_staff', patient_view.edit_patient_for_staff, name="edit_patient_for_staff"),
    path('patient_home', patient_view.patient_home, name='patient_home'),
    path('<patient_id>/edit', patient_view.edit_patient, name='edit_patient'),
]