from django.contrib import admin
from .models import *


# Register your models here.
admin.site.register(Donor)
admin.site.register(BloodRequest)
admin.site.register(BloodDonationRequest)
admin.site.register(Contact)
