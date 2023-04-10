from django.db import models
from django.contrib.auth.models import AbstractUser

from utils import user_get_default_avatar
from utils.slug import slugify


# Create your models here.

class UserNotification(models.Model):
    title = models.CharField(max_length=200)
    time = models.DateTimeField(auto_now_add=True)


class UserSkills(models.Model):
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.slug)
        super().save(*args, **kwargs)


class UserPortfolio(models.Model):
    title = models.CharField(max_length=500, default="Пользователь пока ничего не написал в портфолио")


class UserProfile(models.Model):
    description = models.TextField(null=True, blank=True)


class UserRating(models.Model):
    score = models.FloatField(default=0)


class User(AbstractUser):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=25)
    email = models.CharField(max_length=255)
    photo = models.TextField()

    is_customer = models.BooleanField(default=False)

    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    rating = models.ForeignKey(UserRating, on_delete=models.CASCADE)
    portfolio = models.ForeignKey(UserPortfolio, on_delete=models.CASCADE)
    skills = models.ManyToManyField(UserSkills)
    notification = models.ManyToManyField(UserNotification)

    chats = models.ManyToManyField('chat.Chat')

    def save(self, *args, **kwargs):
        self.username = 'user' + str(self.profile.id)
        if not self.photo:
            self.photo = user_get_default_avatar.get()
        super().save(*args, **kwargs)
