from django import forms
from django.forms import fields
from .models import *

class ReportForm(forms.ModelForm):
    class Meta:
        model = customers
        fields = ('Company_name', 'Contact_person', 'Mobile_number')