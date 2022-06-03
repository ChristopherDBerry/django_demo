from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset, ButtonHolder, Submit

class CustomSwitch(Field):
    template = 'custom_switch.html'

class ClientAddRequestForm(forms.Form):
    summary = forms.CharField(label="Summary", max_length=100)
    description = forms.CharField(label="Description", widget=forms.Textarea)
    high_priority = forms.BooleanField(
        label="Flag as high priority", required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('summary'),
            Field('description'),
            CustomSwitch('high_priority'),
            Submit('submit', 'Create support request'),
        )
