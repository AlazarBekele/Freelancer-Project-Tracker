from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .models import Profile, ProfilePicture


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_related_objects(sender, instance, created, **kwargs):
    if created:
        # Create Profile automatically
        Profile.objects.create(user=instance)

<<<<<<< HEAD
        # Create empty ProfilePicture automatically
        ProfilePicture.objects.create(user=instance)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_user_related_objects(sender, instance, **kwargs):
    instance.profile.save()
    instance.profilepicture.save()
=======
        Profiles.objects.create(user=instance)

def save_user_profile (sender, instance, created, **kwargs):

    instance.profiles.save()
>>>>>>> New-Code
