from django.db.models.signals import post_save
from .models import Profile
from django.dispatch import receiver
from django.conf import settings


@receiver(post_save, sender =settings.AUTH_USER_MODEL )
def create_profile(instance,sender, created,**kwargs):
    if created:
        Profile.objects.create(user = instance)
@receiver(post_save, sender = settings.AUTH_USER_MODEL)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()