from django.db import models
from django.db.models.fields import related


# Create your models here.

class Message(models.Model):
    text = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    from_user = models.ForeignKey('account.User', on_delete=models.CASCADE, related_name='messages_from_user')
    to_user = models.ForeignKey('account.User', on_delete=models.CASCADE, related_name='messages_to_user')
    viewed = models.BooleanField(default=False)


class Chat(models.Model):
    messages = models.ManyToManyField(Message)
    task = models.ForeignKey('task.Task', on_delete=models.CASCADE)
    time_started = models.DateTimeField(auto_now_add=True)
