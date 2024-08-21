from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from django.db import models
from .models import Blog, BlogHero, ContactFormSubmission, HeroHeader, Project, Testimonial, Teamwork, About, Service, TopService, Details,  AccordionItem
from django import forms
class BlogAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget()},
    }

# admin.site.register(Blog, BlogAdmin)


class BlogHeroAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

class ContactFormSubmissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'created_at')

class HeroHeaderAdmin(admin.ModelAdmin):
    list_display = ('heading', 'paragraph')

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'link')

class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'profession')

class TeamworkAdmin(admin.ModelAdmin):
    list_display = ('id',)

class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

 
class ServiceAdminForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'
        widgets = {
            'content': CKEditorWidget(),
        }

class AccordionItemInline(admin.TabularInline):
    model = AccordionItem
    extra = 1

class ServiceAdmin(admin.ModelAdmin):
    form = ServiceAdminForm
    inlines = [AccordionItemInline]


class TopServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

class DetailsAdmin(admin.ModelAdmin):
    list_display = ('address', 'phone', 'email')

admin.site.register(Blog, BlogAdmin)
admin.site.register(BlogHero, BlogHeroAdmin)
admin.site.register(ContactFormSubmission, ContactFormSubmissionAdmin)
admin.site.register(HeroHeader, HeroHeaderAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Testimonial, TestimonialAdmin)
admin.site.register(Teamwork, TeamworkAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(TopService, TopServiceAdmin)
admin.site.register(Details, DetailsAdmin)
