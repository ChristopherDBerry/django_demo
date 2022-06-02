from django import template
import datetime
from django.utils.html import format_html

register = template.Library()

@register.filter
def request_created_text(req):
    t = datetime.datetime.now()
    #XXX handle pluralize
    return "Created %d days ago" % (t - req.replace(tzinfo=None)).days

@register.filter
def request_priority_tag(priority):
    if not priority:
        return ""
    return format_html("""\
<span class="alert alert-danger alert-tag">High priority</span>""")

@register.filter
def request_status_tag(status):
    if status == "pending":
        return format_html("""\
<span class="alert alert-primary alert-tag">Pending</span>""")
    if status == "in_progress":
        return format_html("""\
<span class="alert alert-info alert-tag">In progress</span>""")
    if status == "completed":
        return format_html("""\
<span class="alert alert-success alert-tag">Completed</span>""")

