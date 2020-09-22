from django.urls import path
from work.views.PatientViews import patient_view

urlpatterns = [
    path('register/', patient_view.register_user_post, name="register"),
    path('view_patients/', patient_view.list_patient, name='list_patients'),
    path('<patient_id>/', patient_view.patient_details, name='details'),
    path('patient_home', patient_view.patient_home, name='patient_home'),
    path('<patient_id>/edit', patient_view.edit_patient, name='edit_patient'),
    path('search/', patient_view.search_patient, name='search'),
    path('searhinput', patient_view.search_input, name='searchInput')
]