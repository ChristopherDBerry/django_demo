"""supportdesk models"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

STATUSES = (
    ("pending", "Pending"),
    ("in_progress", "In progress"),
    ("completed", "Completed"),
)

class Request(models.Model):
    """supportdesk client request model"""
    summary = models.CharField(default="", max_length=250, blank=True)
    description = models.TextField(blank=True, null=True)
    requested = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=12,
        choices=STATUSES, default='pending')
    high_priority = models.BooleanField(default=False)
    requestor = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'requestor')
    assigned_to = models.ForeignKey(User, blank=True, null=True,
        on_delete=models.SET_NULL, related_name = 'assigned_to')
