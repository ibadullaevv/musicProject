from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name='User', related_name='profile', on_delete=models.CASCADE)
    avatar = models.ImageField()
    birthday = models.DateField()
    balance = models.DecimalField()

    class Meta:
        db_table = 'profile'
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        return self.user.username
