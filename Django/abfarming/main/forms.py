from django import forms
from .models import farmer
from django.core.validators import RegexValidator
from django.contrib.auth.forms import UserCreationForm
from location_field.forms.plain import PlainLocationField

class Regform(UserCreationForm):
    phone_regex     = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number    = forms.CharField( validators=[phone_regex], max_length=17, help_text="patient's phone number")
    fname = forms.CharField(widget=forms.TextInput(
      attrs={'placeholder': 'First Name'}))
    lname= forms.CharField(widget=forms.TextInput(
      attrs={'placeholder': 'Last Name'}))
    password1 = forms.CharField(widget=forms.PasswordInput(
      attrs={'placeholder': '********'}))
    password2 = forms.CharField(widget=forms.PasswordInput(
      attrs={'placeholder': '********'}))
    location = location = PlainLocationField(initial='-22.2876834,-49.1607606')
    phone_number= forms.CharField(widget=forms.NumberInput(
      attrs={'placeholder': '+2519857483'}))

    class Meta:
        model = farmer
        fields = ("fname","lname", "phone_number","location","email","password1", "password2")
