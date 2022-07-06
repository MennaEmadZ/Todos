from django.db import models
from django.contrib.auth.models import User
from unixtimestampfield.fields import UnixTimeStampField


# Create your models here.
class ToDo(models.Model):
    title = models.CharField(max_length=225)
    description = models.TextField()
    due = UnixTimeStampField()
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
