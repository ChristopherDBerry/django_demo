"""Support desk main views """

from django.shortcuts import render
from django.views.generic import TemplateView

from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required

#@login_required
def home(request):
    """ redirect to appropriate dashbpard for user status """
    if request.user.is_staff:
        return client_request_add(request) #XXX
    else:
        return client_request_add(request)

#@login_required
def client_request_add(request):
    context = {}
#   raise Exception((request.user, request.user.is_authenticated,
#       request.user.is_staff))
    return render(request, 'supportdesk/index.html', context)
