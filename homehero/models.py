from django.db import models
from solo.models import SingletonModel
from ckeditor.fields import RichTextField
# Create your models here.
class SliderItem(models.Model):
    title= RichTextField(blank=True)
    descriptions = models.CharField(max_length=50)
    image=models.ImageField(upload_to="slider/")
    button_one = models.URLField()
    button_two = models.URLField()
    def __str__(self):
        return self.title
    
class Slider(SingletonModel):
    name = models.CharField(max_length=20)
    slider_item = models.ManyToManyField(SliderItem)


class About_item(models.Model):
    TYPE_CHOICES = [
        ('services', 'services'),
        ('About', 'About'),
    ]
    type = models.CharField(max_length=40, choices=TYPE_CHOICES , blank=True)
    icon=models.CharField(max_length=50)
    title=models.CharField(max_length=50)
    desc=models.TextField()
    buton_url=models.URLField(blank=True)
    def __str__(self) :
        return f"{self.type}"
    
class About(SingletonModel):
    title=models.CharField(max_length=30)
    about_item=models.ManyToManyField(About_item)
class Service(SingletonModel):
    title=models.CharField(max_length=30)
    about_item=models.ManyToManyField(About_item)

class Counter(SingletonModel):
    Heart_Transplants=models.IntegerField(default=0)
    BARIATRIC_SURGERY=models.IntegerField(default=0)
    CRITICAL_CARE=models.IntegerField(default=0)
    EXPERT_Doctor=models.IntegerField(default=0)








class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    image = models.ImageField(upload_to='testimonials/')
    rating = models.IntegerField()
    comment = models.TextField()

    def __str__(self):
        return self.name