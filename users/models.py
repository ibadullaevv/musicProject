from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name='User', related_name='profile', on_delete=models.CASCADE)
    avatar = models.ImageField(default='default.jpg', upload_to='images/profile/')
    birthday = models.DateField(auto_now_add=True)

    # balance = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        db_table = 'profile'
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        return self.user.username
