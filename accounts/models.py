from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

# Create your models here.



class Profile(models.Model):
    user = models.OneToOneField(User,related_name='user_profile', on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
        return self.user.username
    

@receiver(post_save,sender=User,)
def Create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user = instance)  


@receiver(post_delete, sender=Profile)
def delete_user_with_profile(sender, instance, **kwargs):
    user = instance.user
    user.delete()          