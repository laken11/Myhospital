from django.urls import path
from work.views.Staff_view import staff_view

urlpatterns = [
    path('register/', staff_view.register_staff, name='register_staff'),
    path('list/', staff_view.list_staff, name='list_staff'),
    path('<id>/', staff_view.staff_details, name='staff details'),
    path('<id>/edit', staff_view.edit_staff, name='edit staff'),
    path('', staff_view.staff_home, name='staff_home')
]