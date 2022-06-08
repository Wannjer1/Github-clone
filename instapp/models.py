
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Image(models.Model):
    '''Model to display image posts'''
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=255, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    caption = models.TextField()
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)
    

class Profile(models.Model):
    '''model to display users profile'''
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    photo = models.ImageField(default='default.jpg', upload_to='avatars/')
    bio = models.TextField(max_length=500,blank=True,null=True, default=f'Hello, I am new here!')