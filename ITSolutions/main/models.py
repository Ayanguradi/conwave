from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from django.utils.html import mark_safe
from django.core.validators import MaxLengthValidator
# from ckeditor.fields import CKEditor5Field
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
class HeroHeader(models.Model):
    image = models.ImageField(upload_to='hero_images/')
    heading = models.CharField(max_length=255)
    paragraph = models.TextField()

    def __str__(self):
        return self.heading


class TopService(models.Model):
    name = models.CharField(max_length=470)
    # description = models.TextField()
    # description = models.TextField(validators=[MaxLengthValidator(475)])
    description= RichTextField(validators=[MaxLengthValidator(475)])
    image = models.ImageField(upload_to='services/')

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ImageField(upload_to='service_icons/')
    hero_heading = models.CharField(max_length=255)
    hero_description = models.TextField( )
    hero_image = models.ImageField(upload_to='hero_images/')
    mission_title = models.CharField(max_length=255)
    # mission_description = models.TextField( null=True, blank=True)
    mission_description =  RichTextField(validators=[MaxLengthValidator(475)])
    mission_image = models.ImageField(upload_to='mission_images/')
    content = RichTextField()

    def __str__(self):
        return self.name

class AccordionItem(models.Model):
    service = models.ForeignKey(Service, related_name='accordion_items', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    # description = models.TextField()
    description = RichTextField()
    def __str__(self):
        return f"{self.title} - {self.service.name}"


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='project_images/')
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

class Testimonial(models.Model):
    content = models.TextField()  # Corresponds to <p>
    client_name = models.CharField(max_length=200)  # Corresponds to <h5>
    profession = models.CharField(max_length=200)  # Corresponds to <span>
    image = models.ImageField(upload_to='testimonial_images/')  # Corresponds to <img>

    def __str__(self):
        return self.client_name

class Teamwork(models.Model):
    image = models.ImageField(upload_to='teamwork_images/')  # Corresponds to the image

    def __str__(self):
        return f"Teamwork Image {self.id}"

class Details(models.Model):
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    twitter = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.address

class BlogHero(models.Model):
    background_image = models.ImageField(upload_to='blog_hero/')
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return "Blog Hero Section"

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextUploadingField()
    date_posted = models.DateField()
    thumbnail = models.ImageField(upload_to='blog_thumbnails/')

    def __str__(self):
        return self.title

    @property
    def short_content(self):
        return ' '.join(self.content.split()[:30]) + '...'

    def get_absolute_url(self):
        return reverse('blog_detail', args=[str(self.pk)])

class ContactFormSubmission(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class About(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    skills = models.TextField()  # Stores a list of skill dictionaries with 'name' and 'percentage'
    image = models.ImageField(upload_to='about_images/')
    
    def __str__(self):
        return self.title





