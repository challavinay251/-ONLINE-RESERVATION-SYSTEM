# reservation/urls.py

from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('reservation/', views.reservation, name='reservation'),
    path('cancellation/', views.cancellation, name='cancellation'),
]
