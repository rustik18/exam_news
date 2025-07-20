from django.urls import path
from .views import *

urlpatterns = [
    path('signup/', sign_up_view, name='sign_up'),
    path('login/', log_in_view, name='log_in'),
    path('logout/', log_out_view, name='log_out'),
    path('', profile_view, name='profile'),
    path('change_pass/', change_pass_view, name='change_pass'),
    path('edit/', edit_profile, name='edit_profile')
]