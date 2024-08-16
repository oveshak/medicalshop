from django.db import models
from solo.models import SingletonModel
# Create your models here.
class Company_socaial_media(models.Model):
    social_name = models.CharField(max_length=40)
    social_icon = models.CharField(max_length=30)
    social_url=models.URLField()
    def __str__(self):
        return f"{self.social_name}"
class Email(models.Model):
    email=models.EmailField()
    def __str__(self) :
        return f"{self.email}"
class FooterImg(models.Model):
    img=models.ImageField(upload_to="footer_image/")
    def __str__(self) :
        return f"{self.img}"

class BusiNess_hours(models.Model):
    day_name=models.CharField(max_length=50)
    day_openging=models.CharField(max_length=10)
    day_ending=models.CharField(max_length=10)
    def __str__(self) :
        return f"{self.day_name}"

class Global(SingletonModel):
    logo_img=models.ImageField(upload_to="globalLogo/")
    company_socaial_medias=models.ManyToManyField(Company_socaial_media)
    email=models.ManyToManyField(Email)
    phone_Number=models.CharField(max_length=14)
    adress=models.TextField()
    footerImg=models.ManyToManyField(FooterImg)
    footertext=models.TextField()
    google_map_url=models.URLField()
    busiNess_hours=models.ManyToManyField(BusiNess_hours)
    def __str__(self):
        return "Global Settings"