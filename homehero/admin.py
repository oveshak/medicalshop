from django.contrib import admin

# Register your models here.
from homehero.models import About, About_item, Counter, Service, Slider, SliderItem, Testimonial
from solo.admin import SingletonModelAdmin

admin.site.register(SliderItem)
admin.site.register(Slider,SingletonModelAdmin)
admin.site.register(About_item)
admin.site.register(About,SingletonModelAdmin)
admin.site.register(Service,SingletonModelAdmin)
admin.site.register(Counter,SingletonModelAdmin)
admin.site.register(Testimonial)