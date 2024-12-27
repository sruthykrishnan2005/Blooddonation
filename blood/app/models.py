from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Donor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    blood_group = models.CharField(max_length=10)
    contact_number = models.CharField(max_length=15)
    city = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.user.username} ({self.blood_group})"