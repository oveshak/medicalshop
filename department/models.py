from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Opening_Hour(models.Model):
    dept_name = models.CharField(max_length=40, blank=True)
    day_name = models.CharField(max_length=40, blank=True)
    day_opening = models.CharField(max_length=20, blank=True)
    day_closing = models.CharField(max_length=20, blank=True)
    
    def __str__(self):
        return f"{self.dept_name}  -  {self.day_name}"
class Treatments_fee(models.Model):
    dept_name = models.CharField(max_length=40, blank=True)
    treatments_name = models.CharField(max_length=40, blank=True)
    treatments_fee = models.IntegerField(default=0)
    
    
    def __str__(self):
        return f"{self.dept_name}  -  {self.treatments_name}"
    
class Investigations_fee(models.Model):
    dept_name = models.CharField(max_length=40, blank=True)
    investigations_name = models.CharField(max_length=40, blank=True)
    investigations_fee = models.IntegerField(default=0)
    def __str__(self):
        return f"{self.dept_name}  -  {self.investigations_name}"


class Department(models.Model):
    DEPT_CHOICES = (
        ("Cardiologists", "Cardiologists"),
        ("Orthopaedics", "Orthopaedics"),
        ("Gastroenterology", "Gastroenterology"),
        ("Neurosciences", "Neurosciences"),
        ("Spine", "Spine"),
        ("Cancer", "Cancer"),
        ("Colorectal", "Colorectal"),
        ("Bariatric", "Bariatric")
    )
    dept_img = models.ImageField(upload_to="deptImg/")
    dept_name = models.CharField(max_length=100, choices=DEPT_CHOICES) 
    dept_desc = RichTextField(blank=True)
    opening_hour = models.ManyToManyField('Opening_Hour')
    treatments_fee = models.ManyToManyField('Treatments_fee')
    investigations_fee = models.ManyToManyField('Investigations_fee')

    def __str__(self):
        return f"{self.dept_name}"