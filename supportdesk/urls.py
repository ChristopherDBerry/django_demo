from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="supportdesk_home"),
    path(
        'add', views.ClientRequestAddView.as_view(),
        name="supportdesk_client_request_add"
    ),
    path(
        'list', views.ClientRequestListView.as_view(),
        name="supportdesk_client_request_list"
    ),
]
