from django.contrib.auth import get_user_model
from django.db import models

class Profile(models.Model):
    user = models.ForeignKey(get_user_model(), related_name='profile', on_delete=models.CASCADE, verbose_name='User', blank=True, null=True)
    avatar = models.ImageField(null=True, blank=True, upload_to='user_pics', verbose_name='Avatar')
    

    def __str__(self):
        return self.user.get_full_name() + "'s Profile"

    class Meta:
        db_table = 'profiles'
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
