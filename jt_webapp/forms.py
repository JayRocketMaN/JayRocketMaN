from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
 first_name = forms.CharField(max_length=300)
last_name = forms.CharField(max_length=300)
username = forms.CharField(max_length=300)
business_name = forms.CharField(max_length=300)
business_brand = forms.CharField(max_length=300)
mobile_number = forms.CharField(max_length=20)
email = forms.EmailField()
tech_school_you_graduated_from = forms.CharField(max_length=300)
tech_skill = forms.CharField(max_length=300)
certificate_earn = forms.ImageField
why_should_we_onboard_you = forms.CharField(max_length=300)
what_can_we_offer = forms.CharField(max_length=300)

class Meta:
		model = User
		fields = ['__all__']
