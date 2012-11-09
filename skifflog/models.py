from django.db import models
from django.contrib.auth.models import User
import timedelta

class Block(models.Model):
    user = models.ForeignKey(User, related_name='blocks')
    start = models.DateTimeField()
    duration = timedelta.fields.TimedeltaField()
    comment = models.TextField(blank=True, null=True)
