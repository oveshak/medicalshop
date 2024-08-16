from django.contrib import admin

from appointment.models import Appointments, Contacts

# Register your models here.
admin.site.register(Appointments)

admin.site.register(Contacts)