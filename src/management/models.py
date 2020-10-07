from django.db import models
from django.contrib.auth import get_user_model

from django.db.models.signals import post_save
from django.dispatch import receiver

User = get_user_model()



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    
    def __str__(self):
        return self.user.username



@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()



class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    title = models.CharField(max_length=100)
    minutes = models.IntegerField()
    description = models.TextField()
    approved = models.BooleanField(default=False)

    
    def __str__(self):
        return self.title

    
