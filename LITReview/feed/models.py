from django.contrib.auth.models import User, AbstractUser
from django.db import models
from authentication.models import User
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator



class Ticket(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=2048, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to='image')
    time_created = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=True)


    def __str__(self):
        return self.title


# Review

class Review(models.Model):
    ticket = models.ForeignKey(Ticket, related_name="reviews", on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(max_length=1024, validators=[MinValueValidator(0), MaxValueValidator(5)])
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    headline = models.CharField(max_length=128)
    body = models.TextField(max_length=8192)
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.ticket.title, self.headline)


class UserFollows(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    followed_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followed_by')

    class Meta:
        unique_together = ('user', 'followed_user')
