from django.urls import path
from work.views.Login import login_view

urlpatterns = [
    path('login/', login_view.login_page_post, name='login'),
    path('change_password/', login_view.change_password, name='change password'),
    path('', login_view.logout_view, name='logout'),
    path('login_get/', login_view.login_page_gt, name='login_get')
]