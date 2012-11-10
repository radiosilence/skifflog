from django.db import models
from django.contrib.auth.models import User
import timedelta
from model_utils import Choices

PLANS = Choices(
    ('mates', 'Mates'),
    ('roaming', 'Roaming Mates'),
    ('regular', 'Regular Mates'),
    ('key', 'Key Mates'),
    ('smalldesk', 'Small Desk Mates'),
    ('desk', 'Desk Mates'),
)

class Block(models.Model):
    user = models.ForeignKey(User, related_name='blocks')
    start = models.DateTimeField()
    duration = timedelta.fields.TimedeltaField()
    comment = models.TextField(blank=True, null=True)

    @property
    def duration_rounded(self):
        return duration


class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    membership = models.CharField(max_length=20,
        choices=PLANS,
        default=PLANS.mates,
        verbose_name='Which type of mate you are (affects total time)'
    )
    round_up = models.FloatField(null=True, blank=True,
        verbose_name='How much you want to round up time, contributed to total, so'
            + ' as not to take the metaphorical piss (in hours)')
    current_visit = models.DateTimeField(null=True, blank=True)

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
