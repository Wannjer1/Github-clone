
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Image(models.Model):
    '''Model to display image posts'''
    image = models.ImageField(upload_to='images/', blank=True)
    name = models.CharField(max_length=255, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    caption = models.TextField()
    likes = models.IntegerField(default=0)
    # profile = models.ForeignKey('Profile', on_delete=models.CASCADE)

    # class Meta:
    #     ordering = ['?'] #order randomly on feed

    def __str__(self):
        return self.name
 

    def save_image(self):
        ''' method to save an image post instance '''
        self.save()

    def delete_image(self):
        '''method to delete an image post instance '''
        self.delete()

    def update_caption(self, new_caption):
        ''' method to update an image's caption '''
        self.caption = new_caption
        self.save()

    def total_likes(self):
        '''method to get the total likes'''
        return self.likes.count()
        
    @classmethod    
    def get_user_images(cls, user_id):
        ''' method to retrieve all images'''
        img = Image.objects.filter(profile=user_id).all()
        sort = sorted(img, key=lambda t: t.created_on)
        return sort
    

class Profile(models.Model):
    '''model to display users profile'''
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    photo = models.ImageField(default='default.jpg', upload_to='avatars/')
    bio = models.TextField(max_length=500,blank=True,null=True, default=f'Hello, I am new here!')


    def __str__(self):
        return f'{self.user.username}'

    def save_profile(self):
        ''' method to save a user's profile '''
        self.save()

    def delete_profile(self):
        '''method to delete a user's profile '''
        self.delete()

    def update_bio(self, new_bio):
        ''' method to update a users profile bio '''
        self.bio = new_bio
        self.save()

    def update_image(self, user_id, new_image):
        ''' method to update a users profile image '''
        user = User.objects.get(id=user_id)
        self.photo = new_image
        self.save()

            
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Likes(models.Model):
    user = models.ForeignKey(User,   on_delete=models.CASCADE,related_name='user_likes')
    image = models.ForeignKey(Image,  on_delete=models.CASCADE, related_name='image_likes')