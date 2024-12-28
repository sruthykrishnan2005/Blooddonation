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