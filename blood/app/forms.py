from django import forms
from .models import Donor
from .models import BloodDonationRequest


class DonorRegistrationForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = ['name', 'blood_group', 'contact_number', 'city', 'age']

class BloodDonationRequestForm(forms.Form):
    full_name = forms.CharField(label="Full Name", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your full name'}))
    email = forms.EmailField(label="Email Address", widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email address'}))
    phone = forms.CharField(label="Phone Number", max_length=15, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your phone number'}))
    message = forms.CharField(label="Message", widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Describe your blood request', 'rows': 4}))