from django import forms
from .models import Donor
from .models import BloodDonationRequest


class DonorRegistrationForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = ['name', 'blood_group', 'contact_number', 'city', 'age']

class BloodDonationRequestForm(forms.ModelForm):
    class Meta:
        model = BloodDonationRequest
        fields = ['name', 'phone', 'place', 'message']