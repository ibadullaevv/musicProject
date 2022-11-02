from django.contrib.auth.models import User
from django.core.files import File
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile = Profile()
        profile.user = instance
        path_image = 'static/default_image.jpg'
        profile.save()
        profile.avatar.save(content=File(open(path_image, 'rb')), name=f'{instance.username}.jpg', save=True)


