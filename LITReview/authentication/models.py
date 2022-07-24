from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    profile_photo = models.ImageField(null=True, blank=True, upload_to='media')
    follows = models.ManyToManyField(
        'self',
        symmetrical=False,
        verbose_name='suit',
    )

