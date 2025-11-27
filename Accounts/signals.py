from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .models import Profiles, ProfilePicture


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_related_objects(sender, instance, created, **kwargs):
    if created:
        # Create Profile automatically

        Profiles.objects.create(user=instance)

def save_user_profile (sender, instance, created, **kwargs):

    instance.profiles.save()
