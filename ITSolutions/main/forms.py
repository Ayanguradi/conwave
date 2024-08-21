# forms.py

from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    country_code = forms.CharField(max_length=5, required=True)
    phone = forms.CharField(max_length=15, required=True)
    email = forms.EmailField(required=True)
    subject = forms.CharField(widget=forms.Textarea, required=True)
