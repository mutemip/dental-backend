from django.contrib import admin
from .models import (
    Clinic,
    Doctor,
    Affiliation,
    Visit,
    Patient,
    Appointment
)

admin.site.register(Clinic)
admin.site.register(Doctor)
admin.site.register(Affiliation)
admin.site.register(Visit)
admin.site.register(Patient)
admin.site.register(Appointment)