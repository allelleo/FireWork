from django.db import models
from unicodedata import category

from utils.slug import slugify


# Create your models here.
class TaskCategory(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()
    deadlines = models.CharField(max_length=200)
    place = models.CharField(max_length=300)

    category = models.ManyToManyField(TaskCategory)
    slug = models.CharField(max_length=200)

    time = models.DateTimeField(auto_now_add=True)
    from_customer = models.ForeignKey('account.User', on_delete=models.CASCADE, related_name='from_customer')
    executor = models.ForeignKey('account.User', on_delete=models.CASCADE, related_name='executor', null=True,
                                 blank=True)
    photo = models.TextField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.slug)
        super().save(*args, **kwargs)
