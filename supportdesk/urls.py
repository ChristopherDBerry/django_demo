from django.urls import path
from . import views

urlpatterns = [
    #path(
    #    "", views.ClientHome.as_view(), name="supportdesk_client_home"
    #),
    path('', views.home, name="supportdesk_home"),
    path('add', views.client_request_add, name="supportdesk_client_request_add"),
]
