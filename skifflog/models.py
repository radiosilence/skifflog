import datetime
from django.db import models
from django.contrib.auth.models import User
import timedelta
from model_utils import Choices
from skifflog.utils import month_range

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


class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    membership = models.CharField(max_length=20,
        choices=PLANS,
        default=PLANS.mates,
        verbose_name='Which type of mate you are (affects total time)'
    )
    round_up = models.FloatField(default=24.0,
        verbose_name='How much you want to round up time, contributed to total, so'
            + ' as not to take the metaphorical piss (in hours)')
    current_visit = models.DateTimeField(null=True, blank=True)

    @property
    def month_blocks(self):
        begin, end = month_range()
        return self.user.blocks.filter(start__range=(begin, end)).order_by(
            'start')

    @property
    def max_use(self):
        return datetime.timedelta(days={
            PLANS.mates: 2,
            PLANS.roaming: 5,
            PLANS.regular: 12,
            PLANS.key: 0,
            PLANS.smalldesk: 0,
            PLANS.desk: 0,
        }[self.membership])

    @property
    def used_time(self):
        def floored(delta):
            if self.round_up:
                floor = datetime.timedelta(hours=self.round_up)
            else:
                floor = datetime.timedelta(0)
            if delta < floor:
                return floor
            else:
                return delta
        total = datetime.timedelta(0)
        date_total = datetime.timedelta(0)
        date = None
        for block in self.month_blocks:
            if date != block.start.date() and not date is None:
                total += floored(date_total)
                date = block.start.date()
                date_total = datetime.timedelta(0)
            date_total += block.duration
        total += floored(date_total)
        return total



User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
