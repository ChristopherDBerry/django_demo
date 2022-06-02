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
    path(
        'staff/list', views.StaffRequestListView.as_view(),
        name="supportdesk_staff_request_list"
    ),
    path(
        'staff/view/<int:requestID>/', views.StaffRequestView.as_view(),
        name="supportdesk_staff_request_view"
    ),
    path('staff/assign', views.assign_request,
        name="assign_request"),
    path('staff/complete', views.complete_request,
        name="assign_request"),
]
