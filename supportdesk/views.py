"""Support desk main views """

from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy

from django.contrib.auth.mixins import (LoginRequiredMixin,
    PermissionRequiredMixin)
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required

from . import forms
from .models import Request

@login_required
def home(request):
    """ redirect to appropriate dashbpard for user status """
    if request.user.is_staff:
        return redirect("supportdesk_client_request_add") #XXX
    else:
        return redirect("supportdesk_client_request_add")


class ClientRequestAddView(LoginRequiredMixin, FormView):
    """ Form view for client to add request """
    template_name = "supportdesk/add.html"
    form_class = forms.ClientAddRequestForm
    success_url = reverse_lazy("supportdesk_client_request_list")

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        reqs = Request.objects.filter(requestor=self.request.user)
        context['request_count'] = reqs.count()
        return context

    def form_valid(self, form):
        data = form.cleaned_data
        req = Request(summary=data["summary"],
            description=data["description"],
            high_priority=data["high_priority"],
            requestor=self.request.user)
        req.save()
        return redirect(self.success_url)


class ClientRequestListView(LoginRequiredMixin, TemplateView):
    """ Form view for client to view all requests """
    template_name = 'supportdesk/list.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        reqs = Request.objects.filter(requestor=self.request.user)
        context['request_count'] = reqs.count()
        return context


class StaffRequestListView(PermissionRequiredMixin, FormView):
    permission_required = 'is_staff'
