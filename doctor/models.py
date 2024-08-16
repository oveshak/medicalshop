from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify

# class Dr_Social_Media(models.Model):
#     dr_name = models.CharField(max_length=30)
#     social_name = models.CharField(max_length=40)
#     social_icon = models.CharField(max_length=30)
#     social_url=models.URLField()
    
#     def __str__(self):
#         return f"{self.dr_name} ------ {self.social_name}"

class Drs_socaials_medias(models.Model):
    dr_name=models.CharField(max_length=40)
    social_name = models.CharField(max_length=40)
    social_icon = models.CharField(max_length=30)
    social_url=models.URLField()
    def __str__(self):
        return f"{self.dr_name} ------ {self.social_name}"


class Medical_Specialization(models.Model):
    specialization = models.TextField()
    
    def __str__(self):
        return f"{self.specialization}"

class Dr_Medical_Specialization(models.Model):
    dr_name = models.CharField(max_length=39)
    specializations = models.ManyToManyField(Medical_Specialization)
    
    def __str__(self):
        return f"{self.dr_name}"

class Education_Medical_Training(models.Model):
    training = models.TextField()
    
    def __str__(self):
        return f"{self.training}"

class Dr_Education_Medical_Training(models.Model):
    dr_name = models.CharField(max_length=39)
    trainings = models.ManyToManyField(Education_Medical_Training)
    
    def __str__(self):
        return f"{self.dr_name}"

class Training(models.Model):
    training = models.TextField()
    
    def __str__(self):
        return f"{self.training}"

class Dr_Training(models.Model):
    dr_name = models.CharField(max_length=39)
    trainings = models.ManyToManyField(Training)
    
    def __str__(self):
        return f"{self.dr_name}"

class Certification(models.Model):
    certification = models.TextField()
    
    def __str__(self):
        return f"{self.certification}"

class Dr_Certification(models.Model):
    dr_name = models.CharField(max_length=39)
    certifications = models.ManyToManyField(Certification)
    
    def __str__(self):
        return f"{self.dr_name}"

class Percentage(models.Model):
    dr_name = models.CharField(max_length=150, blank=True)
    name_of_percentage = models.CharField(max_length=60, blank=True)
    rate_of_percentage = models.IntegerField(blank=True)
    
    def __str__(self):
        return f"{self.dr_name} ----- {self.name_of_percentage}"




class Opening_Hour(models.Model):
    dr_name = models.CharField(max_length=40, blank=True)
    day_name = models.CharField(max_length=40, blank=True)
    day_opening = models.CharField(max_length=20, blank=True)
    day_closing = models.CharField(max_length=20, blank=True)
    
    def __str__(self):
        return f"{self.dr_name}  -  {self.day_name}"



# class Doctor(models.Model):
#     dr_name = models.CharField(max_length=60)
#     slug = models.SlugField(blank=True, default="", null=False, unique=True)
    
#     def save(self, *args, **kwargs):
#         if not self.slug:
#             # Generate initial slug
#             self.slug = slugify(self.dr_name)
#             unique_slug = self.slug
#             num = 1
#             # Ensure the slug is unique
#             while Doctor.objects.filter(slug=unique_slug).exists():
#                 unique_slug = f'{self.slug}-{num}'
#                 num += 1
#             self.slug = unique_slug
#         super().save(*args, **kwargs)

#     profession_name = models.CharField(max_length=50)
#     img = models.ImageField(upload_to='images/')
#     social_media = models.ManyToManyField('Drs_socaials_medias', blank=True)
#     desc = RichTextField(blank=True)
#     medical_specializations = models.ForeignKey('Dr_Medical_Specialization', on_delete=models.CASCADE, related_name='doctors')
#     education_trainings = models.ForeignKey('Dr_Education_Medical_Training', on_delete=models.CASCADE, related_name='doctors')
#     trainings = models.ForeignKey('Dr_Training', on_delete=models.CASCADE, related_name='doctors')
#     certifications = models.ForeignKey('Dr_Certification', on_delete=models.CASCADE, related_name='doctors')
#     opening_hours = models.ManyToManyField('Opening_Hour',  related_name='doctors')
#     professional_rating = models.ForeignKey('Percentage',  related_name='doctors')
#     phone_number = models.CharField(max_length=18)
#     job_place = models.CharField(max_length=500)
#     fax_number = models.CharField(max_length=16)
#     email = models.EmailField()
#     web_app_link = models.URLField(blank=True)
    
#     def __str__(self):
#         return f"{self.dr_name}"


class Doctors(models.Model):
    dr_name = models.CharField(max_length=60)
    slug = models.SlugField(blank=True, default="", null=False, unique=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            # Generate initial slug
            self.slug = slugify(self.dr_name)
            unique_slug = self.slug
            num = 1
            # Ensure the slug is unique
            while Doctors.objects.filter(slug=unique_slug).exists():
                unique_slug = f'{self.slug}-{num}'
                num += 1
            self.slug = unique_slug
        super().save(*args, **kwargs)

    profession_name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='images/')
    social_media = models.ManyToManyField('Drs_socaials_medias', blank=True)
    desc = RichTextField(blank=True)
    medical_specializations = models.ForeignKey('Dr_Medical_Specialization', on_delete=models.CASCADE, related_name='doctors')
    education_trainings = models.ForeignKey('Dr_Education_Medical_Training', on_delete=models.CASCADE, related_name='doctors')
    trainings = models.ForeignKey('Dr_Training', on_delete=models.CASCADE, related_name='doctors')
    certifications = models.ForeignKey('Dr_Certification', on_delete=models.CASCADE, related_name='doctors')
    opening_hours = models.ManyToManyField('Opening_Hour',  related_name='doctors')
    professional_rating = models.ManyToManyField('Percentage',  related_name='doctors')
    phone_number = models.CharField(max_length=18)
    job_place = models.CharField(max_length=500)
    fax_number = models.CharField(max_length=16)
    email = models.EmailField()
    web_app_link = models.URLField(blank=True)
    
    def __str__(self):
        return f"{self.dr_name}"

