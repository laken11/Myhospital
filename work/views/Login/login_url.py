from django.urls import path
from work.views.Login import login_view


urlpatterns = [
    path('login/', login_view.login_page_post, name='login'),
    path('', login_view.logout_view, name='logout'),
]