
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from cloudinary.models import CloudinaryField
from datetime import datetime

# Create your models here.
class Image(models.Model):
    image =  CloudinaryField('Pics')
    img_name = models.CharField(max_length=200, blank=True)
    imge_caption = models.CharField(max_length=200,blank=True)
    date_posted = models.DateTimeField(auto_now_add=True,blank=True)
    likes=models.IntegerField(default=0)
    # keeping the default=0 in the likes means that likes will start from 0
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def total_likes(self):
        return self.likes.count()

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()
    
    def __str__(self):
        return self.img_name
 
class Profile(models.Model):
    name = models.CharField(max_length=200, blank=True)
    username = models.CharField(max_length=200, blank=True)
    profile_photo = models.ImageField(upload_to='pics/',blank=True)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, null=True,blank=True)
    bio = models.TextField(max_length=200,blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.username

    def save_profile(self):
        '''method to save profile'''
        self.save()

    def delete_profile(self):
        '''method to delete profile'''
        self.delete()

    def update_bio(self, new_bio):
        '''method to update user bio'''
        self.bio = new_bio
        self.save()

    def update_image(self,user_id, new_image):
        '''method to update a users profile image'''
        self.photo = new_image
        self.save()
 

class Likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='user_likes')
    image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='image_likes')

class Comment(models.Model):
    post = models.ForeignKey(Image,on_delete=models.CASCADE,related_name='comments',null=True,blank=True)
    poster = models.ForeignKey(User,on_delete=models.CASCADE,related_name='poster',null=True,blank=True)
    comment=models.TextField(null=True,blank=True)
    date_posted= models.DateTimeField(auto_now_add=True,blank=True,null=True)

    def save_comment(self):
        '''method to save a comment'''
        self.save()

    def delete_comment(self):
        '''method to delete a comment'''
        self.delete()

    def __str__(self): 
        return self.comment


class Relation(models.Model):
    ''' model for user relations: follower-following system'''
    followers = models.ForeignKey('Profile', related_name='following', on_delete=models.CASCADE)
    following = models.ForeignKey('Profile', related_name='followers', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('followers', 'following')

    def __str__(self):
        return '{self.followers} follows {self.following}'

    