from django.db import models

# Create your models here.

class Appointments(models.Model):
    fname= models.CharField(max_length=20)
    lname=models.CharField(max_length=30)
    subject=models.CharField(max_length=60)
    email=models.EmailField()
    phone=models.CharField(max_length=15)
    data= models.DateField()
    message=models.TextField()

    def __str__(self):
        return f"{self.fname}    --   {self.email}"
    
class Contacts(models.Model):
    name= models.CharField(max_length=20)
    subject=models.TextField()
    email=models.EmailField()
    
    message=models.TextField()

    def __str__(self):
        return f"{self.name}    --   {self.email}"