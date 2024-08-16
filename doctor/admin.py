from django.contrib import admin

from doctor.models import Certification, Doctors, Dr_Certification, Dr_Education_Medical_Training, Dr_Medical_Specialization, Dr_Training,Drs_socaials_medias, Education_Medical_Training, Medical_Specialization, Opening_Hour, Percentage, Training

# Register your models here.
admin.site.register(Drs_socaials_medias)
admin.site.register(Medical_Specialization)
admin.site.register(Dr_Medical_Specialization)
admin.site.register(Education_Medical_Training)
admin.site.register(Dr_Education_Medical_Training)
admin.site.register(Training)
admin.site.register(Dr_Training)
admin.site.register(Certification)
admin.site.register(Dr_Certification)
admin.site.register(Percentage)
admin.site.register(Opening_Hour)
admin.site.register(Doctors)
# admin.site.register()
# admin.site.register()
# admin.site.register()