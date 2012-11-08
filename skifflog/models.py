from django.db import models
import timedelta

class Block(models.Model):
    start = models.DateTimeField()
    duration = timedelta.fields.TimedeltaField()