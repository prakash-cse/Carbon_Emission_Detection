from django import forms
from .models import *

class IndustryForm(forms.ModelForm):
    class Meta:
        model = Industry
        fields = '__all__'

class HouseholdForm(forms.ModelForm):
    class Meta:
        model = Household
        fields = '__all__'