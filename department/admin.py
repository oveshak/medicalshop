from django.contrib import admin

from department.models import Department, Investigations_fee, Opening_Hour, Treatments_fee

# Register your models here.
admin.site.register(Department)
admin.site.register(Investigations_fee)
admin.site.register(Treatments_fee)
admin.site.register(Opening_Hour)
