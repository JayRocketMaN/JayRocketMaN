from django.db import models
import os
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class User(models.Model):
    user = models.ForeignKey( 'auth.User', related_name='users', on_delete=models.CASCADE)
    is_private = models.BooleanField(default=False)
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    username = models.CharField(max_length=300)
    business_name = models.CharField(max_length=300, default='intern')
    business_brand = models.CharField(max_length=300, default='intern')
    mobile_number = models.CharField(max_length=300)
    email = models.EmailField()
    tech_school_you_graduated_from = models.CharField(max_length=300, default='company')
    tech_skill = models.CharField(max_length=300, default='company')
    certificate_earn = models.ImageField(upload_to = settings.MEDIA_ROOT, default='company') 
    why_should_we_onboard_you = models.TextField(max_length=300, default='company')
    what_can_we_offer = models.TextField(max_length=300, default='intern')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
      return self.first_name
    
    #class Meta:
      ordering['created_at']