from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Image(models.Model):
    '''Model to display image posts'''
    image = models.ImageField(upload_to='images/')
    created_on = models.DateTimeField(auto_now_add=True)
    caption = models.TextField()
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)
