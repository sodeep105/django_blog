from django.db.models.signals import post_save
from django.contrib.auth.models import User #signal sender
from django.dispatch import receiver
from .models import Profile

#user profile to be created for each new user.
#reciever receives the signal generated when user is created
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance,  **kwargs):
    instance.profile.save()