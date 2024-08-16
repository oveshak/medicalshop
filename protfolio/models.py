from django.db import models
from django.utils.text import slugify
# Create your models here.


class Protfolio_Category(models.Model):
    name=models.CharField(max_length=30)
    slug = models.SlugField(blank=True, default="", null=False, unique=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            # Generate initial slug
            self.slug = slugify(self.name)
            unique_slug = self.slug
            num = 1
            # Ensure the slug is unique
            while Protfolio_Category.objects.filter(slug=unique_slug).exists():
                unique_slug = f'{self.slug}-{num}'
                num += 1
            self.slug = unique_slug
        super().save(*args, **kwargs)
      
    def __str__(self):
            return self.name
        

class Protfolios(models.Model):
    category=models.ForeignKey(Protfolio_Category, on_delete=models.CASCADE)
    image=models.ImageField(upload_to="portfolio/")
    title=models.CharField(max_length=300)
    subtitle=models.TextField()
    def __str__(self):
        return self.title