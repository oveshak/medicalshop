from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from solo.models import SingletonModel
# Create your models here.
class Blogss(models.Model):
    blog_title=models.CharField(max_length=400)

    slug = models.SlugField(blank=True, default="", null=False, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            # Generate initial slug
            self.slug = slugify(self.blog_title)
            unique_slug = self.slug
            num = 1
            # Ensure the slug is unique
            while Blogss.objects.filter(slug=unique_slug).exists():
                unique_slug = f'{self.slug}-{num}'
                num += 1
            self.slug = unique_slug
        super().save(*args, **kwargs)
    blog_desc=models.TextField()
    blog_img=models.ImageField(upload_to="blog/")
    poyam_text=RichTextField(blank=True)
    blog_Writer_name=models.CharField(max_length=50)
    blog_Writer_desc=models.TextField()
    blog_Writer_img=models.ImageField(upload_to="writer_img/")
    date = models.DateField(auto_now_add=True)
    blog_Writer_fb_url=models.URLField( blank=True)
    blog_Writer_twiter_url=models.URLField(blank=True)
    blog_Writer_linkdin_url=models.URLField(blank=True)
    def __str__(self):
        return f"{self.blog_title}"
    
class AllBlog(SingletonModel):
    name=models.CharField(max_length=40)
    blog_item=models.ManyToManyField(Blogss)
