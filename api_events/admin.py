from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Appointment)
admin.site.register(AppointmentReason)
admin.site.register(AppointmentStatus)
admin.site.register(AppointmentType)