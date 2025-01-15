from django import forms
from .models import Donor

class DonorRegistrationForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = ['name', 'blood_group', 'contact_number', 'city', 'age']
