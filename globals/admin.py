from django.contrib import admin
from globals.models import BusiNess_hours, Company_socaial_media, Email, FooterImg, Global
from solo.admin import SingletonModelAdmin
# Register your models here.

admin.site.register(Company_socaial_media)
admin.site.register(Email)
admin.site.register(FooterImg)
admin.site.register(BusiNess_hours)
admin.site.register(Global,SingletonModelAdmin)