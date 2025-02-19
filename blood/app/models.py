from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Donor(models.Model):
    name = models.TextField()
    blood_group = models.CharField(max_length=10)
    contact_number = models.CharField(max_length=15)
    city = models.CharField(max_length=50)
    age = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.user.username} ({self.blood_group})"
    

class BloodRequest(models.Model):
    patient_name = models.CharField(max_length=100)
    description = models.TextField()
    place = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=15)
    request_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Blood request for {self.patient_name} at {self.place}"

class BloodDonationRequest(models.Model):
    BLOOD_TYPE_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
    ]
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    place = models.CharField(max_length=255)
    blood_type = models.CharField(max_length=3, choices=BLOOD_TYPE_CHOICES)
    message = models.TextField()
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Request by {self.name} from {self.place}"