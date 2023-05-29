from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    bio = models.CharField(max_length=50, blank=True)
    location = models.CharField(
        max_length=100, default="No location", blank=True)
    website = models.URLField(blank=True, null=True)
    phone = models.CharField(max_length=14, blank=True)
    birth_date = models.DateField(blank=True, null=True)
    follows = models.ManyToManyField(
        'self', blank=True, symmetrical=False, related_name='twitter_user_follows')
    followers = models.ManyToManyField(
        'self', blank=True, symmetrical=False, related_name='twitter_user_followers')
    AbstractUser.is_superuser = True

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.username


class Tweet(models.Model):

    text = models.CharField(max_length=50, default="something...", blank=False)
    user_tweet = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user")
    location = models.CharField(
        max_length=100, default="no location of tweet registered", blank=True)
    created = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(
        User, related_name='tweet_likes', blank=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.text
