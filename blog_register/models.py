from django.db import models
from django import forms

# Create your models here.
GENDER_CHOICES = (
   ('M', 'Male'),
   ('F', 'Female')
)
CATEGORY=(
    ('G','General'),
    ('S','Sports'),
    ('T','Trending'),
    ('P','Politics')
)
class Blog(models.Model):
    title= models.CharField(max_length=100)
    description= models.TextField()
    auth_name= models.CharField(max_length=100)
    img= models.ImageField(upload_to='images/',null=True,blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=128)
    category = models.CharField(max_length=6, choices=CATEGORY, default='None')
    created_at = models.DateTimeField(auto_now_add=True)