"""Support desk main views """

from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required

from . import forms
from .models import Request

@login_required
def home(request):
    """ redirect to appropriate dashbpard for user status """
    if request.user.is_staff:
        return redirect("supportdesk_staff_request_list")
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
        context['requests'] = reqs
        return context


@staff_member_required
def assign_request(request):
    requestID = request.POST["requestID"]
    req = Request.objects.get(pk=requestID)
    req.assigned_to = request.user
    req.status = "in_progress"
    req.save()
    return redirect("supportdesk_home")


@staff_member_required
def complete_request(request):
    requestID = request.POST["requestID"]
    req = Request.objects.get(pk=requestID)
    req.status = "completed"
    req.save()
    return redirect("supportdesk_home")


@method_decorator(staff_member_required, name='dispatch')
class StaffRequestListView(TemplateView):
    template_name = 'supportdesk/staff/list.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        reqs = Request.objects.filter(assigned_to=self.request.user
            ).exclude(status="completed")
        context['requests'] = reqs
        #XXX adding this so staff can assign themselves
        #unassigned requests
        other_reqs = Request.objects.exclude(assigned_to=self.request.user
            ).exclude(status="completed")
        context['other_requests'] = other_reqs
        #XXX adding this to review completed requests
        complete_reqs = Request.objects.filter(status="completed")
        context['complete_requests'] = complete_reqs
        return context


@method_decorator(staff_member_required, name='dispatch')
class StaffRequestView(TemplateView):
    template_name = 'supportdesk/staff/view.html'

    def get(self, request, requestID):
        context = {}
        context['request'] = Request.objects.get(pk=requestID)
        return render(request, self.template_name, context)
