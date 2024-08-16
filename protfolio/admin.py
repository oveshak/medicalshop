from django.contrib import admin

from protfolio.models import Protfolios, Protfolio_Category

# Register your models here.
admin.site.register(Protfolio_Category)
admin.site.register(Protfolios)