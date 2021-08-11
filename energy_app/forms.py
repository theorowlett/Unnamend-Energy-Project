from django import forms
from django.forms import widgets
from .models import Data

class DataForm(forms.ModelForm):
    class Meta:
        model = Data
        fields =['state']