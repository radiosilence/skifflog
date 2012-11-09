import datetime
import calendar

def month_range(today=None):
    if not today:
        today = datetime.date.today()
    begin = datetime.date(year=today.year, month=today.month, day=1)
    _, days = calendar.monthrange(year, month)
    delta = datetime.timedelta(days=days)
    return begin, begin + delta

def blocks_this_month(user):
    begin, end = month_range()
    return user.blocks.filter(start__range=(begin, end))