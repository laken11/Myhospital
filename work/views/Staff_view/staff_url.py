from django.urls import path
from work.views.Staff_view import staff_view

urlpatterns = [
    path('searchresult/', staff_view.search_staff, name='search_staff'),
    path('search/', staff_view.search_input, name='staff_search_input'),
    path('register/', staff_view.register_staff, name='register_staff'),
    path('list/', staff_view.list_staff, name='list_staff'),
    path('<id>/', staff_view.staff_details, name='staff_details'),
    path('<id>/edit', staff_view.edit_staff, name='edit staff'),
    path('<id>/details', staff_view.staff_details, name='staff details'),
    path('', staff_view.staff_home, name='staff_home'),
]